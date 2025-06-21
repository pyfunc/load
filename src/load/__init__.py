"""
Load - Modern alternative to Python import
Inspired by Go and Groovy simplicity
"""

import sys
import types
from typing import Any, Dict, List

from .core import (
    load_github,
    load_pypi,
    load_url,
    load_local,
    enable_auto_print,
    disable_auto_print,
    set_print_limit,
    info as core_info,
    load,
)

__version__ = "1.0.0"
__author__ = "Tom Sapletta"
__email__ = "info@softreck.dev"


class LoadModule:
    """Magic module - everything through dot notation."""

    def __getattr__(self, name: str) -> Any:
        """Get attribute from the module.
        
        Handles special module attributes and provides dynamic imports.
        """
        # First check for special module attributes
        special_attrs = {
            "__path__", "__file__", "__spec__",
            "__loader__", "__package__", "__annotations__",
            "__all__", "__builtins__"
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
            
        # Then check for module-level methods
        if name in ["enable_auto_print", "disable_auto_print", 
                   "set_print_limit", "info"]:
            # Check if the method exists in the instance's __dict__
            if name in self.__dict__:
                return self.__dict__[name]
            return None
            
        # Handle common Python module aliases
        common_aliases = {
            # Data science
            "np": "numpy",
            "pd": "pandas",
            "plt": "matplotlib.pyplot",
            "sns": "seaborn",
            # Machine learning
            "tf": "tensorflow",
            "torch": "torch",
            "sklearn": "sklearn",
            # Web and data
            "requests": "requests",
            "json": "json",
            "yaml": "yaml",
            # System
            "os": "os",
            "sys": "sys",
            "pathlib": "pathlib",
            # Image processing
            "cv2": "opencv-python",
            "PIL": "PIL",
            # Utilities
            "time": "time",
            "datetime": "datetime",
            "random": "random"
        }
        
        if name in common_aliases:
            module_name = common_aliases[name]
            try:
                # Import the module
                module = __import__(module_name)
                # For submodules like matplotlib.pyplot
                if '.' in module_name:
                    for part in module_name.split('.')[1:]:
                        module = getattr(module, part)
                # Cache the module in the instance
                setattr(self, name, module)
                return module
            except ImportError:
                raise ImportError(f"Could not import {name}. Please install it with: pip install {module_name}")

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
        
    def __dir__(self) -> List[str]:
        """Return list of attributes for tab completion."""
        # Common Python aliases
        python_aliases = [
            # Data science
            "np", "pd", "plt", "sns",
            # Machine learning
            "tf", "torch", "sklearn",
            # Web and data
            "requests", "json", "yaml",
            # System
            "os", "sys", "pathlib",
            # Image processing
            "cv2", "PIL",
            # Utilities
            "time", "datetime", "random"
        ]
        
        # Module methods
        methods = [
            "load_github", "load_pypi", "load_url", "load_local",
            "enable_auto_print", "disable_auto_print", "set_print_limit",
            "info", "load"
        ]
        
        # Combine all attributes
        attrs = set(python_aliases + methods + list(self.__dict__.keys()))
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
    __path__: List[str]
    __package__: str
    __spec__: Any
    __loader__: Any
    __annotations__: Dict[str, Any]
    
    def __init__(self) -> None:
        """Initialize the module wrapper."""
        super().__init__()

# Store the original module before replacing it
_original_module = sys.modules[__name__]

# Common Python aliases that will be available with 'from load import *'
COMMON_ALIASES = {
    # Core modules
    'os': 'os',
    'sys': 'sys',
    'json': 'json',
    
    # Data science
    'np': 'numpy',
    'pd': 'pandas',
    'plt': 'matplotlib.pyplot',
    'sns': 'seaborn',
    
    # Web
    'requests': 'requests',
    'yaml': 'yaml',
    
    # Machine learning
    'tf': 'tensorflow',
    'torch': 'torch',
    'sklearn': 'sklearn',
    
    # Image processing
    'cv2': 'opencv-python',
    'PIL': 'PIL',
    
    # Utilities
    'time': 'time',
    'datetime': 'datetime',
    'random': 'random',
    'pathlib': 'pathlib',
}

def _import_common_aliases() -> None:
    """Import and inject common aliases into the module's globals."""
    import importlib
    import sys
    
    # Get the module's globals
    module = sys.modules[__name__]
    globals_dict = module.__dict__
    
    for alias, module_name in COMMON_ALIASES.items():
        if alias not in globals_dict:  # Don't override existing attributes
            try:
                # Import the module
                module = importlib.import_module(module_name.split('.')[0])
                
                # Handle submodules (e.g., matplotlib.pyplot)
                if '.' in module_name:
                    for part in module_name.split('.')[1:]:
                        module = getattr(module, part)
                
                # Add to globals
                globals_dict[alias] = module
            except ImportError:
                pass  # Silently skip if the module is not available

# Create and configure the module wrapper
module_wrapper = LoadModuleWrapper()
module_wrapper.__file__ = _original_module.__file__ or __file__
module_wrapper.__path__ = _original_module.__path__ or []  # type: ignore[assignment]
module_wrapper.__package__ = _original_module.__package__ or __package__ or ""
module_wrapper.__spec__ = _original_module.__spec__
module_wrapper.__loader__ = _original_module.__loader__
module_wrapper.__annotations__ = _original_module.__annotations__

# Create a new module and update it with our wrapper's attributes
new_module = types.ModuleType(__name__)
for key, value in module_wrapper.__dict__.items():
    setattr(new_module, key, value)

# Add module-level functions
new_module.enable_auto_print = module_wrapper.enable_auto_print
new_module.disable_auto_print = module_wrapper.disable_auto_print
new_module.set_print_limit = module_wrapper.set_print_limit
new_module.info = core_info  # Use the already imported core_info

# Import and inject common aliases
_import_common_aliases()

# Replace the module in sys.modules with our new module
sys.modules[__name__] = new_module

# Common Python aliases that will be available with 'from load import *'
__all__ = [
    # Core functions
    "load_github",
    "load_pypi",
    "load_url",
    "load_local",
    "enable_auto_print",
    "disable_auto_print",
    "set_print_limit",
    "info",
    "load",
    
    # Common data science aliases
    "np", "pd", "plt", "sns",
    
    # Machine learning
    "tf", "torch", "sklearn",
    
    # Web and data
    "requests", "json", "yaml",
    
    # System
    "os", "sys", "pathlib",
    
    # Image processing
    "cv2", "PIL",
    
    # Utilities
    "time", "datetime", "random"
]
