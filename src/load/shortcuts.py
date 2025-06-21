"""
Shortcut functions for common packages
"""

from .core import load

# Shortcut functions
def load_pandas(alias='pd'):
    """Shortcut for loading pandas"""
    return load('pandas', alias=alias)

def load_numpy(alias='np'):
    """Shortcut for loading numpy"""
    return load('numpy', alias=alias)

def load_requests():
    """Shortcut for loading requests"""
    return load('requests')

def load_json():
    """Shortcut for loading json"""
    return load('json')

def load_os():
    """Shortcut for loading os"""
    return load('os')

def load_sys():
    """Shortcut for loading sys"""
    return load('sys')

def load_torch():
    """Shortcut for loading torch"""
    return load('torch')

def load_cv2():
    """Shortcut for loading OpenCV"""
    return load('opencv-python', alias='cv2')

def load_pil():
    """Shortcut for loading PIL"""
    return load('pillow', alias='PIL')

def load_sklearn():
    """Shortcut for loading scikit-learn"""
    return load('scikit-learn', alias='sklearn')

def load_matplotlib(alias='plt'):
    """Shortcut for loading matplotlib"""
    return load('matplotlib', alias=alias)

# Aliases
def np():
    """Alias for numpy"""
    return load_numpy()

def pd():
    """Alias for pandas"""
    return load_pandas()

def plt():
    """Alias for matplotlib"""
    return load_matplotlib()
    return load("matplotlib.pyplot", "plt")

def tf():
    return load("tensorflow", "tf")

# For testing - always available stdlib modules
def json():
    return load("json")

def os():
    return load("os")

def sys():
    return load("sys")