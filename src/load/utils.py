"""
Utility functions for Load
"""

import sys
import os
import importlib
import importlib.util
import subprocess
import tempfile
import urllib.request
import zipfile
from pathlib import Path
from typing import Dict, Any, Optional, List, Union

# Import from config to avoid circular imports
from .config import _module_cache, AUTO_PRINT, PRINT_LIMIT, PRINT_TYPES


def smart_print(obj, name=None):
    """Intelligent result printing"""
    if not AUTO_PRINT:
        return

    try:
        obj_name = name or getattr(obj, "__name__", type(obj).__name__)

        if hasattr(obj, "status_code"):  # HTTP Response
            print(" {0}: {1} - {2}".format(obj_name, obj.status_code, obj.url))
            if hasattr(obj, "json"):
                try:
                    data = obj.json()
                    print(" JSON: {0}...".format(str(data)[:PRINT_LIMIT]))
                except:
                    print(" Text: {0}...".format(obj.text[:PRINT_LIMIT]))

        elif hasattr(obj, "shape"):  # DataFrame/Array
            print(" {0}: shape {1}".format(obj_name, obj.shape))
            print(obj.head() if hasattr(obj, "head") else str(obj)[:PRINT_LIMIT])

        elif hasattr(obj, "__len__") and len(obj) > 10:  # Long collections
            print(" {0}: {1} items".format(obj_name, len(obj)))
            print("First 5: {0}...".format(list(obj)[:5]))

        elif isinstance(obj, PRINT_TYPES):  # Basic types
            output = str(obj)
            if len(output) > PRINT_LIMIT:
                print(" {0}: {1}...".format(obj_name, output[:PRINT_LIMIT]))
            else:
                print(" {0}: {1}".format(obj_name, output))

        elif hasattr(obj, "__dict__"):  # Objects
            attrs = [attr for attr in dir(obj) if not attr.startswith("_")][:5]
            print(" {0}: {1} with {2}...".format(obj_name, type(obj).__name__, attrs))

        else:
            print(" {0}: {1} loaded".format(obj_name, type(obj).__name__))

    except Exception as e:
        print(" {0}: loaded ({1})".format(obj_name or 'Object', type(obj).__name__))


def load(*args, **kwargs):
    from .core import load

    return load(*args, **kwargs)


def install_package(name: str) -> bool:
    """Install package using pip"""
    try:
        print(f"Installing {name} from pypi...")
        result = subprocess.run(
            [sys.executable, "-m", "pip", "install", name],
            capture_output=True,
            text=True,
            timeout=60,
        )
        return result.returncode == 0
    except Exception:
        return False


def load(
    name: str,
    alias: str = None,
    registry: str = None,
    install: bool = True,
    force: bool = False,
    silent: bool = False,
) -> Any:
    """
    Load module/package from various sources

    Examples:
        load("requests")                    # PyPI
        load("user/repo")                   # GitHub
        load("./my_module.py")              # Local file
        load("package", registry="company") # Private registry
    """
    cache_key = alias or name

    # Check cache (unless force)
    if not force and cache_key in _module_cache:
        cached_obj = _module_cache[cache_key]
        if not silent:
            smart_print(cached_obj, "{0} (cached)".format(cache_key))
        return cached_obj

    # If local file
    if name.endswith(".py") or name.startswith("./") or name.startswith("../"):
        return _load_local_file(name, cache_key, silent)

    # Try to load as standard module
    try:
        module = importlib.import_module(name.replace("/", "."))
        _module_cache[cache_key] = module
        if not silent:
            smart_print(module, cache_key)
        return module
    except ImportError:
        pass

    # Module not found - try to install
    if install:
        if install_package(name):
            try:
                module = importlib.import_module(name)
                _module_cache[cache_key] = module
                if not silent:
                    smart_print(module, "{0} (installed)".format(cache_key))
                return module
            except ImportError:
                pass

    raise ImportError("Cannot load {0}".format(name))


def _load_local_file(file_path: str, cache_key: str, silent: bool = False) -> Any:
    """Load local Python file"""
    path = Path(file_path)
    if not path.exists():
        raise ImportError("File {0} does not exist".format(file_path))

    spec = importlib.util.spec_from_file_location(path.stem, path)
    if spec is None or spec.loader is None:
        raise ImportError("Cannot create spec for {0}".format(file_path))

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    _module_cache[cache_key] = module
    if not silent:
        smart_print(module, cache_key)
    return module
