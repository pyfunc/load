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

from .registry import LoadRegistry
from .utils import smart_print

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
        source_type, source_name = LoadRegistry.parse_source(name)
        success = False

        if registry and registry in LoadRegistry.PRIVATE_REGISTRIES:
            success = LoadRegistry.install_from_pypi(source_name, registry)
        elif source_type == 'pypi':
            success = LoadRegistry.install_from_pypi(source_name)
        elif source_type == 'github':
            success = LoadRegistry.install_from_github(source_name)
        elif source_type == 'gitlab':
            token = LoadRegistry.PRIVATE_REGISTRIES.get('private_gitlab', {}).get('token')
            success = LoadRegistry.install_from_gitlab(source_name, token)
        elif source_type == 'url':
            success = LoadRegistry.install_from_url(source_name)

        if success:
            try:
                module_name = name.split('/')[-1] if '/' in name else name
                module = importlib.import_module(module_name)
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
