"""
Load - Modern alternative to Python import
Inspired by Go and Groovy simplicity
"""

import sys
from typing import Any

from .core import (
    load_github,
    load_pypi,
    load_url,
    load_local,
    enable_auto_print,
    disable_auto_print,
    set_print_limit,
    info,
    load,
)

__version__ = "1.0.0"
__author__ = "Tom Sapletta"
__email__ = "info@softreck.dev"


class LoadModule:
    """Magic module - everything through dot notation."""

    def __getattr__(self, name: str) -> Any:
        # Handle special module attributes needed for Python's import system
        special_attrs = (
            '__path__',
            '__file__',
            '__spec__',
            '__loader__',
            '__package__',
            '__annotations__'
        )
        if name in special_attrs:
            # Return None for special attributes to avoid infinite recursion
            return None
            
        # Popular aliases mapping
        aliases = {
            'np': ('numpy', 'np'),
            'pd': ('pandas', 'pd'),
            'plt': ('matplotlib.pyplot', 'plt'),
            'tf': ('tensorflow', 'tf'),
            'requests': ('requests', None),
            'json': ('json', None),
            'os': ('os', None),
            'sys': ('sys', None),
            'torch': ('torch', None),
            'cv2': ('opencv-python', 'cv2'),
            'PIL': ('pillow', 'PIL'),
            'sklearn': ('scikit-learn', 'sklearn')
        }

        # Check for auto-print functions
        if name in ['enable_auto_print', 'disable_auto_print', 'set_print_limit']:
            return getattr(self, name)

        # Check if it's an alias
        if name in aliases:
            module_name, alias = aliases[name]
            return load(module_name, alias=alias)
            
        # Import load function only when needed
        return load(name)

    # Auto-print functions
    def enable_auto_print(self) -> None:
        """Enable automatic printing of results."""
        enable_auto_print()

    def disable_auto_print(self) -> None:
        """Disable automatic printing of results."""
        disable_auto_print()

    def set_print_limit(self, limit: int) -> None:
        """Set the maximum number of items to print.

        Args:
            limit: Maximum number of items to print
        """
        set_print_limit(limit)


# Store the original module before replacing it
_original_module = sys.modules[__name__]

# Create a new module instance that will handle the magic imports
sys.modules[__name__] = LoadModule()

# Make sure the original module's attributes are still accessible
sys.modules[__name__].__dict__.update({
    '__version__': __version__,
    '__author__': __author__,
    '__email__': __email__,
    '__doc__': __doc__,
    '__file__': _original_module.__file__,
    '__path__': _original_module.__path__,
    '__package__': _original_module.__package__,
    '__spec__': _original_module.__spec__,
    '__loader__': _original_module.__loader__,
    '__annotations__': _original_module.__annotations__,
})

__all__ = [
    'load_github', 'load_pypi', 'load_url', 'load_local',
    'enable_auto_print', 'disable_auto_print', 'set_print_limit',
    'info', 'load'
]