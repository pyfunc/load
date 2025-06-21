"""
Magic import functionality
"""

from .core import load


class LoadModule:
    """Magic module - everything through dot notation with auto-print"""

    def __getattr__(self, name):
        # Popular aliases mapping
        aliases = {
            "np": "numpy",
            "pd": "pandas",
            "plt": "matplotlib.pyplot",
            "tf": "tensorflow",
            "torch": "torch",
            "cv2": "opencv-python",
            "PIL": "pillow",
            "sklearn": "scikit-learn",
        }

        # Check if it's an alias
        if name in aliases:
            result = load(aliases[name], alias=name)
        else:
            result = load(name)

        # Auto-print for chainable calls
        if hasattr(result, "__call__"):
            # Wrap function to show results
            original_func = result

            def wrapped_func(*args, **kwargs):
                result = original_func(*args, **kwargs)
                from .utils import smart_print

                smart_print(result, f"{name}()")
                return result

            return wrapped_func

        return result
