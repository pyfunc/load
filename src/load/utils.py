"""
Utility functions for Load
"""

from __future__ import absolute_import, division, print_function, unicode_literals

import importlib.util
import importlib.machinery
import importlib.abc
import os
import subprocess
import sys

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
            try:
                # Try to get length if it's a collection
                length = len(obj)
                if (length > 0 and PRINT_TYPES and 
                        not isinstance(obj, (str, bytes, bytearray))):
                    print(" {0}: {1} (length: {2})".format(
                        obj_name or 'Object', 
                        type(obj).__name__, 
                        length))
                else:
                    print(" {0}: {1}".format(obj_name or 'Object', type(obj).__name__))
            except (TypeError, AttributeError):
                # If we can't get length, just print type
                print(" {0}: {1}".format(obj_name or 'Object', type(obj).__name__))

        else:
            print(" {0}: {1} loaded".format(obj_name, type(obj).__name__))

    except Exception as e:
        print(" {0}: loaded ({1})".format(obj_name or 'Object', type(obj).__name__))


def install_package(name):
    """Install package using pip"""
    try:
        print("Installing {0} from pypi...".format(name))
        # For Python 2.7 compatibility, use Popen instead of subprocess.run
        process = subprocess.Popen(
            [sys.executable, "-m", "pip", "install", name],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        # Store but ignore stdout/stderr output
        process.communicate()
        return process.returncode == 0
    except (subprocess.SubprocessError, OSError) as e:
        print("Error installing package {0}: {1}".format(name, str(e)), file=sys.stderr)
        return False


def load(
    name,
    alias=None,
    registry=None,
    install=True,
    force=False,
    silent=False,
):
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


def import_aliases(*names):
    """Import multiple modules and return them as a tuple.

    Args:
        *names: Module names to import. Can include aliases using 'alias=module_name' syntax.

    Returns:
        A tuple containing the imported modules in the order they were requested.

    Example:
        # Import with default names
        np, pd = import_aliases('numpy', 'pandas')

        # Import with aliases
        plt, sns = import_aliases('plt=matplotlib.pyplot', 'sns=seaborn')
    """
    result = []
    for name in names:
        if "=" in name:
            alias, module_name = name.split("=", 1)
        else:
            module_name = name

        try:
            module = __import__(module_name.split(".")[0])
            # Handle submodules (e.g., matplotlib.pyplot)
            for part in module_name.split(".")[1:]:
                module = getattr(module, part)
            result.append(module)
        except ImportError as e:
            raise ImportError("Could not import {0}: {1}".format(module_name, e))

    return tuple(result) if len(result) > 1 else result[0] if result else None


def _load_local_file(file_path, cache_key, silent=False):
    """Load local Python file"""
    if not os.path.exists(file_path):
        raise ImportError("File {0} does not exist".format(file_path))

    try:
        module_name = os.path.splitext(os.path.basename(file_path))[0]
        
        # Use importlib to load the module
        spec = importlib.util.spec_from_file_location(module_name, file_path)
        if spec is None:
            raise ImportError("Could not load spec for {0}".format(file_path))
            
        module = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = module
        spec.loader.exec_module(module)
        
        _module_cache[cache_key] = module
        if not silent:
            smart_print(module, cache_key)
        return module
    except Exception as e:
        raise ImportError("Cannot load {0}: {1}".format(file_path, str(e)))
