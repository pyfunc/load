"""
Load - Modern alternative to Python import
Inspired by Go and Groovy simplicity
"""

from .core import (
    load,
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

        # Check if it's an alias
        if name in aliases:
            module_name, alias = aliases[name]
            return load(module_name, alias=alias)
        else:
            return load(name)

# Replace this module with magic module
import sys
sys.modules[__name__] = LoadModule()

__all__ = [
    'load', 'load_github', 'load_pypi', 'load_url', 'load_local',
    'enable_auto_print', 'disable_auto_print', 'set_print_limit',
    'info'
]