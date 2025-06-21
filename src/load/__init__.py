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
        special_attrs = {
            "__path__", "__file__", "__spec__", "__loader__",
            "__package__", "__annotations__", "__all__", "__builtins__"
        }
        
        if name in special_attrs:
            if name == "__all__":
                return [
                    "load_github", "load_pypi", "load_url",
                    "load_local", "enable_auto_print",
                    "disable_auto_print", "set_print_limit",
                    "info", "load"
                ]
            return None

        # Popular aliases mapping
        aliases = {
            "np": ("numpy", "np"),
            "pd": ("pandas", "pd"),
            "plt": ("matplotlib.pyplot", "plt"),
            "tf": ("tensorflow", "tf"),
            "requests": ("requests", None),
            "json": ("json", None),
            "os": ("os", None),
            "sys": ("sys", None),
            "torch": ("torch", None),
            "cv2": ("opencv-python", "cv2"),
            "PIL": ("pillow", "PIL"),
            "sklearn": ("scikit-learn", "sklearn"),
        }

        # Check for auto-print functions
        if name in ["enable_auto_print", "disable_auto_print", "set_print_limit"]:
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
        from .core import enable_auto_print as _enable_auto_print
        _enable_auto_print()

    def disable_auto_print(self) -> None:
        """Disable automatic printing of results."""
        from .core import disable_auto_print as _disable_auto_print
        _disable_auto_print()

    def set_print_limit(self, limit: int) -> None:
        """Set the maximum number of items to print.

        Args:
            limit: Maximum number of items to print
        """
        from .core import set_print_limit as _set_print_limit
        _set_print_limit(limit)
        
    def __dir__(self) -> list[str]:
        """Return list of attributes for tab completion."""
        aliases = [
            "np", "pd", "plt", "tf", "requests", "json",
            "os", "sys", "torch", "cv2", "PIL", "sklearn"
        ]
        methods = [
            "load_github", "load_pypi", "load_url",
            "load_local", "enable_auto_print",
            "disable_auto_print", "set_print_limit",
            "info"
        ]
        attrs = set(aliases + methods + list(self.__dict__.keys()))
        return sorted(attrs)


# Create a type-safe module replacement
class LoadModuleWrapper(LoadModule):
    """Wrapper to maintain module attributes and type safety.
    
    This wrapper ensures proper type hints and module attributes
    are maintained when replacing the module with our custom class.
    """
    __version__: str = __version__
    __author__: str = __author__
    __email__: str = __email__
    __doc__: str = __doc__
    __file__: str
    __path__: list[str]
    __package__: str
    __spec__: Any
    __loader__: Any
    __annotations__: dict[str, Any]

# Store the original module before replacing it
_original_module = sys.modules[__name__]

# Create and configure the module wrapper
module_wrapper = LoadModuleWrapper()
module_wrapper.__file__ = _original_module.__file__ or __file__
module_wrapper.__path__ = _original_module.__path__ or []
module_wrapper.__package__ = _original_module.__package__ or __package__ or ""
module_wrapper.__spec__ = _original_module.__spec__
module_wrapper.__loader__ = _original_module.__loader__
module_wrapper.__annotations__ = _original_module.__annotations__

# Replace the module in sys.modules with our wrapper
# We're intentionally replacing the module with our custom class
sys.modules[__name__] = module_wrapper  # type: ignore[assignment]

__all__ = [
    "load_github",
    "load_pypi",
    "load_url",
    "load_local",
    "enable_auto_print",
    "disable_auto_print",
    "set_print_limit",
    "info",
    "load",
]
