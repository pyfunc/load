"""
Core functionality of Load
"""

from typing import Dict, Any
from .config import _module_cache, AUTO_PRINT, PRINT_LIMIT, PRINT_TYPES
from .utils import load, smart_print, install_package

def load_github(repo: str, alias: str = None) -> Any:
    """Shortcut for GitHub: load_github("user/repo")"""
    return load(repo, alias=alias)

def load_pypi(name: str, alias: str = None) -> Any:
    """Shortcut for PyPI: load_pypi("package")"""
    return load(name, alias=alias)

def load_url(url: str, alias: str = None) -> Any:
    """Shortcut for URL: load_url("http://...")"""
    return load(url, alias=alias)

def load_local(path: str, alias: str = None) -> Any:
    """Shortcut for local files"""
    return load(path, alias=alias)

def enable_auto_print():
    """Enable automatic result display"""
    global AUTO_PRINT
    AUTO_PRINT = True

def disable_auto_print():
    """Disable automatic result display"""
    global AUTO_PRINT
    AUTO_PRINT = False

def set_print_limit(limit: int):
    """Set character limit for auto-print"""
    global PRINT_LIMIT
    PRINT_LIMIT = limit

def info() -> Dict[str, Any]:
    """Show Load information"""
    return {
        'cache_size': len(_module_cache),
        'cached_modules': list(_module_cache.keys())
    }

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