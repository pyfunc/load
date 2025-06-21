"""
Compatibility layer for Python 2 and 3 support.
"""

import sys

# Python version check
PY2 = sys.version_info[0] == 2
PY3 = sys.version_info[0] == 3

# Import builtins
if PY2:
    import __builtin__ as builtins
    from io import open
    from urllib2 import urlopen
    from urllib import urlretrieve
    from urlparse import urlparse
    from StringIO import StringIO

    text_type = unicode
    binary_type = str
    string_types = (str, unicode)
    integer_types = (int, long)
    unicode = unicode
    basestring = basestring
    long = long
    FileNotFoundError = IOError
    PermissionError = IOError
else:
    import builtins
    from io import StringIO
    from urllib.request import urlopen, urlretrieve
    from urllib.parse import urlparse

    text_type = str
    binary_type = bytes
    string_types = (str,)
    integer_types = (int,)
    unicode = str
    basestring = (str, bytes)
    long = int
    FileNotFoundError = FileNotFoundError
    PermissionError = PermissionError

# Handle typing module
try:
    from typing import (
        Any,
        Dict,
        List,
        Tuple,
        Union,
        Optional,
        Type,
        TypeVar,
        Text,
        cast,
    )

    TYPE_CHECKING = False  # or True if you want to enable type checking at runtime
except ImportError:
    # Dummy implementations for Python < 3.5
    _T = TypeVar("_T") if "TypeVar" in globals() else "_T"

    def cast(typ, val):
        return val

    # Dummy type annotations
    class _DummyType(type):
        def __getitem__(self, item):
            return self

    # Create dummy types
    class _Dummy(object):
        __metaclass__ = _DummyType

    # Assign dummy types
    Any = _Dummy()
    Dict = _Dummy()
    List = _Dummy()
    Tuple = _Dummy()
    Union = _Dummy()
    Optional = _Dummy()
    Type = _Dummy()
    TypeVar = _Dummy()
    Text = _Dummy()
    TYPE_CHECKING = False

# Handle pathlib
try:
    from pathlib import Path
except ImportError:
    from pathlib2 import Path

# Handle builtins that were moved
if PY3:
    input = input
    range = range
    map = map
    zip = zip
else:
    input = raw_input
    range = xrange
    from itertools import imap, izip

    map = imap
    zip = izip


# Handle string and bytes
def to_bytes(s, encoding="utf-8", errors="strict"):
    """Convert string to bytes."""
    if isinstance(s, text_type):
        return s.encode(encoding, errors)
    elif isinstance(s, binary_type):
        return s
    else:
        return str(s).encode(encoding, errors)


def to_str(s, encoding="utf-8", errors="strict"):
    """Convert bytes to string."""
    if isinstance(s, binary_type):
        return s.decode(encoding, errors)
    elif isinstance(s, text_type):
        return s
    else:
        return str(s)


# Handle metaclasses
def with_metaclass(meta, *bases):
    """
    Create a base class with a metaclass.

    This is a simplified version of six.with_metaclass.
    """
    # This creates a new class with the specified metaclass and bases
    return meta("temporary_class", bases, {})


# Handle function annotations
def get_type_hints(obj):
    """Get type hints from a function or class."""
    if hasattr(obj, "__annotations__"):
        return obj.__annotations__
    return {}


# Handle importlib
try:
    import importlib
    import importlib.util
    import importlib.machinery

    def import_module(name, package=None):
        return importlib.import_module(name, package)

    def find_spec(name, package=None):
        return importlib.util.find_spec(name, package)

except (ImportError, AttributeError):
    # Python 2.7 fallback
    import imp

    def import_module(name, package=None):
        if package:
            name = "{0}.{1}".format(package, name)
        return __import__(name, fromlist=[""])

    def find_spec(name, package=None):
        # Simplified version for Python 2.7
        if package:
            name = "{0}.{1}".format(package, name)
        try:
            return imp.find_module(name)
        except ImportError:
            return None


# Handle contextlib.nullcontext
if PY3:
    from contextlib import nullcontext
else:

    class nullcontext(object):
        """Context manager that does nothing."""

        def __init__(self, enter_result=None):
            self.enter_result = enter_result

        def __enter__(self):
            return self.enter_result

        def __exit__(self, *args):
            pass


# Handle FileNotFoundError for Python 2
if PY2:

    class FileNotFoundError(IOError):
        pass


# Handle PermissionError for Python 2
if PY2:

    class PermissionError(IOError):
        pass
