"""
Core functionality of Load
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

# Cache modułów w pamięci
_module_cache: Dict[str, Any] = {}

# Konfiguracja auto-print
AUTO_PRINT = True
PRINT_LIMIT = 1000
PRINT_TYPES = (str, int, float, list, dict, tuple)

def smart_print(obj, name=None):
    """Intelligent result printing"""
    if not AUTO_PRINT:
        return

    try:
        obj_name = name or getattr(obj, '__name__', type(obj).__name__)

        if hasattr(obj, 'status_code'):  # HTTP Response
            print(f"🌐 {obj_name}: {obj.status_code} - {obj.url}")
            if hasattr(obj, 'json'):
                try:
                    data = obj.json()
                    print(f"📄 JSON: {str(data)[:PRINT_LIMIT]}...")
                except:
                    print(f"📄 Text: {obj.text[:PRINT_LIMIT]}...")

        elif hasattr(obj, 'shape'):  # DataFrame/Array
            print(f"📊 {obj_name}: shape {obj.shape}")
            print(obj.head() if hasattr(obj, 'head') else str(obj)[:PRINT_LIMIT])

        elif hasattr(obj, '__len__') and len(obj) > 10:  # Long collections
            print(f"📋 {obj_name}: {len(obj)} items")
            print(f"First 5: {list(obj)[:5]}...")

        elif isinstance(obj, PRINT_TYPES):  # Basic types
            output = str(obj)
            if len(output) > PRINT_LIMIT:
                print(f"📝 {obj_name}: {output[:PRINT_LIMIT]}...")
            else:
                print(f"📝 {obj_name}: {output}")

        elif hasattr(obj, '__dict__'):  # Objects
            attrs = [attr for attr in dir(obj) if not attr.startswith('_')][:5]
            print(f"🔧 {obj_name}: {type(obj).__name__} with {attrs}...")

        else:
            print(f"✅ {obj_name}: {type(obj).__name__} loaded")

    except Exception as e:
        print(f"✅ {obj_name or 'Object'}: loaded ({type(obj).__name__})")

def install_package(name: str) -> bool:
    """Install package using pip"""
    try:
        print(f"📦 Installing {name} from pypi...")
        result = subprocess.run(
            [sys.executable, "-m", "pip", "install", name],
            capture_output=True,
            text=True,
            timeout=60
        )
        return result.returncode == 0
    except Exception:
        return False

def load(name: str, alias: str = None, registry: str = None,
         install: bool = True, force: bool = False, silent: bool = False) -> Any:
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
            smart_print(cached_obj, f"{cache_key} (cached)")
        return cached_obj

    # If local file
    if name.endswith('.py') or name.startswith('./') or name.startswith('../'):
        return _load_local_file(name, cache_key, silent)

    # Try to load as standard module
    try:
        module = importlib.import_module(name.replace('/', '.'))
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
                    smart_print(module, f"{cache_key} (installed)")
                return module
            except ImportError:
                pass

    raise ImportError(f"Cannot load {name}")

def _load_local_file(file_path: str, cache_key: str, silent: bool = False) -> Any:
    """Load local Python file"""
    path = Path(file_path)
    if not path.exists():
        raise ImportError(f"File {file_path} does not exist")

    spec = importlib.util.spec_from_file_location(path.stem, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot create spec for {file_path}")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    _module_cache[cache_key] = module
    if not silent:
        smart_print(module, cache_key)
    return module

# Shortcuts for different sources
def load_github(repo: str, alias: str = None) -> Any:
    """Shortcut for GitHub: load_github("user/repo")"""
    return load(repo, alias=alias)

def load_pypi(package: str, alias: str = None, registry: str = 'pypi') -> Any:
    """Shortcut for PyPI: load_pypi("package")"""
    return load(package, alias=alias, registry=registry)

def load_url(url: str, alias: str = None) -> Any:
    """Shortcut for URL: load_url("http://...")"""
    return load(url, alias=alias)

def load_local(path: str, alias: str = None) -> Any:
    """Shortcut for local files"""
    return load(path, alias=alias)

# Auto-print control functions
def enable_auto_print():
    """Enable automatic result display"""
    global AUTO_PRINT
    AUTO_PRINT = True
    print("✅ Auto-print enabled")

def disable_auto_print():
    """Disable automatic result display"""
    global AUTO_PRINT
    AUTO_PRINT = False
    print("❌ Auto-print disabled")

def set_print_limit(limit: int):
    """Set character limit for auto-print"""
    global PRINT_LIMIT
    PRINT_LIMIT = limit
    print(f"📏 Print limit: {limit} characters")

def info():
    """Show Load information"""
    return {
        'cache_size': len(_module_cache),
        'cached_modules': list(_module_cache.keys()),
        'auto_print': AUTO_PRINT,
        'print_limit': PRINT_LIMIT
    }