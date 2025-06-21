"""
Shortcuts for popular libraries
"""

from .core import load

def requests():
    return load("requests")

def numpy():
    return load("numpy")

def pandas():
    return load("pandas")

def matplotlib():
    return load("matplotlib")

def torch():
    return load("torch")

def tensorflow():
    return load("tensorflow")

def cv2():
    return load("opencv-python", "cv2")

def PIL():
    return load("pillow", "PIL")

def sklearn():
    return load("scikit-learn", "sklearn")

# Aliases
def np():
    return load("numpy", "np")

def pd():
    return load("pandas", "pd")

def plt():
    return load("matplotlib.pyplot", "plt")

def tf():
    return load("tensorflow", "tf")
