"""
Shortcut functions for common packages
"""

from .core import load

# Shortcut functions
def load_pandas(alias="pd"):
    """Shortcut for loading pandas"""
    return load("pandas", alias=alias)


def load_numpy(alias="np"):
    """Shortcut for loading numpy"""
    return load("numpy", alias=alias)


def load_requests():
    """Shortcut for loading requests"""
    return load("requests")


def load_json():
    """Shortcut for loading json"""
    return load("json")


def load_os():
    """Shortcut for loading os"""
    return load("os")


def load_sys():
    """Shortcut for loading sys"""
    return load("sys")


def load_torch():
    """Shortcut for loading torch"""
    return load("torch")


def load_cv2():
    """Shortcut for loading OpenCV"""
    return load("opencv-python", alias="cv2")


def load_pil():
    """Shortcut for loading PIL"""
    return load("pillow", alias="PIL")


def load_sklearn():
    """Shortcut for loading scikit-learn"""
    return load("scikit-learn", alias="sklearn")


def load_matplotlib(alias="plt"):
    """Shortcut for loading matplotlib"""
    return load("matplotlib", alias=alias)


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


def tf():
    return load("tensorflow", "tf")


def cv2():
    """Alias for OpenCV"""
    return load_cv2()


def PIL():
    """Alias for PIL"""
    return load_pil()


def sklearn():
    """Alias for scikit-learn"""
    return load_sklearn()


# Add module-level shortcuts
requests = load_requests
json = load_json
os = load_os
sys = load_sys
def sys():
    return load("sys")
