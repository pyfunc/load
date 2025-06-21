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
    set_print_limit
)

from .shortcuts import (
    requests, numpy, pandas, torch, tensorflow,
    np, pd, plt, tf, cv2, PIL, sklearn
)

from .registry import (
    add_registry,
    list_registries,
    configure_private_registry,
    REGISTRIES,
    PRIVATE_REGISTRIES
)

__version__ = "1.0.0"
__author__ = "Your Name"
__email__ = "your.email@example.com"

# Magic import dla `import load`
import sys
from .magic import LoadModule
sys.modules[__name__] = LoadModule()

__all__ = [
    'load', 'load_github', 'load_pypi', 'load_url', 'load_local',
    'requests', 'numpy', 'pandas', 'torch', 'tensorflow',
    'np', 'pd', 'plt', 'tf', 'cv2', 'PIL', 'sklearn',
    'add_registry', 'list_registries', 'configure_private_registry',
    'enable_auto_print', 'disable_auto_print', 'set_print_limit',
    'REGISTRIES', 'PRIVATE_REGISTRIES'
]
