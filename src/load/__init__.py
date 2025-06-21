"""
Load - Modern alternative to Python import
Inspired by Go and Groovy simplicity
"""

from .core import (
    load_github,
    load_pypi,
    load_url,
    load_local,
    enable_auto_print,
    disable_auto_print,
    set_print_limit,
    info
)

# Import shortcuts to make them available
from . import shortcuts

__version__ = "1.0.0"
__author__ = "Tom Sapletta"
__email__ = "info@softreck.dev"

# Magic import functionality
class LoadModule:
    """Magic module - everything through dot notation"""

    def __getattr__(self, name):
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
        else:
            # Import load function only when needed
            from .core import load
            return load(name)

    # Auto-print functions
    def enable_auto_print(self):
        enable_auto_print()

    def disable_auto_print(self):
        disable_auto_print()

    def set_print_limit(self, limit: int):
        set_print_limit(limit)

# Replace this module with magic module
import sys
sys.modules[__name__] = LoadModule()

__all__ = [
    'load_github', 'load_pypi', 'load_url', 'load_local',
    'enable_auto_print', 'disable_auto_print', 'set_print_limit',
    'info'
]