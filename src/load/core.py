# -*- coding: utf-8 -*-
"""
Core functionality of Load
"""

from __future__ import absolute_import, division, print_function, unicode_literals

# Import config and utils
from .config import _module_cache, AUTO_PRINT, PRINT_LIMIT
from .utils import load  # noqa: F401


# Shortcuts for different sources
def load_github(repo, alias=None):
    """Shortcut for GitHub: load_github("user/repo")"""
    return load(repo, alias=alias)


def load_pypi(package, alias=None, registry="pypi"):
    """Shortcut for PyPI: load_pypi("package")"""
    return load(package, alias=alias, registry=registry)


def load_url(url, alias=None):
    """Shortcut for URL: load_url("http://...")"""
    return load(url, alias=alias)


def load_local(path, alias=None):
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


def set_print_limit(limit):
    """Set character limit for auto-print"""
    global PRINT_LIMIT
    PRINT_LIMIT = limit
    print("📏 Print limit: {0} characters".format(limit))


def info():
    """Show Load information"""
    return {
        "cache_size": len(_module_cache),
        "cached_modules": list(_module_cache.keys()),
        "auto_print": AUTO_PRINT,
        "print_limit": PRINT_LIMIT,
    }
