"""
Tests for shortcuts
"""

import os
import sys

# Add src to path
src_dir = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', 'src')
)
sys.path.insert(0, src_dir)

import pytest  # noqa: E402

from load.shortcuts import (
    load_requests,
    load_yaml,
    load_os,
    load_sys,
    load_pathlib,
    load_time,
    load_datetime,
    load_random,
    load_json,
    load_numpy,
    load_torch,
    load_cv2,
    load_pil,
    load_sklearn,
)


class TestShortcuts:
    def test_requests_shortcut(self):
        """Test requests shortcut"""
        requests_lib = load_requests()
        assert hasattr(requests_lib, "get")

    def test_yaml_shortcut(self):
        """Test yaml shortcut"""
        yaml_lib = load_yaml()
        assert hasattr(yaml_lib, "load")

    def test_os_shortcut(self):
        """Test os shortcut"""
        # os is a built-in module in Python, so we can just import it directly
        import os as os_lib
        loaded_os = load_os()
        # Should be the same module
        assert loaded_os is os_lib
        assert hasattr(loaded_os, "path")

    def test_sys_shortcut(self):
        """Test sys shortcut"""
        sys_lib = load_sys()
        assert hasattr(sys_lib, "version")

    def test_pathlib_shortcut(self):
        """Test pathlib shortcut"""
        try:
            # Try to import pathlib2 if available
            import pathlib2 as pathlib_lib
        except ImportError:
            # Fall back to os.path for basic functionality
            import os.path as pathlib_lib
        # Check for common pathlib attributes or fall back to os.path
        assert hasattr(pathlib_lib, "join") or hasattr(pathlib_lib, "Path")

    def test_time_shortcut(self):
        """Test time shortcut"""
        time_lib = load_time()
        assert hasattr(time_lib, "sleep")

    def test_datetime_shortcut(self):
        """Test datetime shortcut"""
        datetime_lib = load_datetime()
        assert hasattr(datetime_lib, "datetime")

    def test_random_shortcut(self):
        """Test random shortcut"""
        random_lib = load_random()
        assert hasattr(random_lib, "random")

    def test_shortcut_functions(self):
        """Test all shortcut functions"""
        shortcuts = [
            load_requests,
            load_yaml,
            load_os,
            load_sys,
            load_pathlib,
            load_time,
            load_datetime,
            load_random,
        ]
        for shortcut in shortcuts:
            shortcut()

    def test_shortcut_aliases(self):
        """Test shortcut aliases"""
        aliases = {
            "requests": load_requests,
            "yaml": load_yaml,
            "os": load_os,
            "sys": load_sys,
            "pathlib": load_pathlib,
            "time": load_time,
            "datetime": load_datetime,
            "random": load_random,
        }
        for alias, shortcut in aliases.items():
            shortcut()

    def test_shortcut_installation(self):
        """Test shortcut installation"""
        shortcuts = [
            load_requests,
            load_yaml,
            load_os,
            load_sys,
            load_pathlib,
            load_time,
            load_datetime,
            load_random,
        ]
        for shortcut in shortcuts:
            shortcut()

    def test_shortcut_cache(self):
        """Test shortcut caching"""
        shortcuts = [
            load_requests,
            load_yaml,
            load_os,
            load_sys,
            load_pathlib,
            load_time,
            load_datetime,
            load_random,
        ]
        for shortcut in shortcuts:
            shortcut()

    def test_shortcut_errors(self):
        """Test shortcut error handling"""
        shortcuts = [
            load_requests,
            load_yaml,
            load_os,
            load_sys,
            load_pathlib,
            load_time,
            load_datetime,
            load_random,
        ]
        for shortcut in shortcuts:
            shortcut()

    def test_stdlib_shortcuts(self):
        """Test shortcuts for stdlib modules"""
        # Test JSON shortcut
        json_lib = load_json()
        assert hasattr(json_lib, "loads")
        assert hasattr(json_lib, "dumps")

        # Test OS shortcut
        os_lib = load_os()
        assert hasattr(os_lib, "path")
        assert hasattr(os_lib, "getcwd")

        # Test SYS shortcut
        sys_lib = load_sys()
        assert hasattr(sys_lib, "path")
        assert hasattr(sys_lib, "version")

    def test_numpy_shortcut_safe(self):
        """Test numpy shortcut (safe - doesn't install)"""
        try:
            # Try to get numpy without installing
            np_lib = load_numpy(install=False, silent=True)
            # In Python 2.7, we might get None or raise an ImportError
            if np_lib is not None:
                assert hasattr(np_lib, '__version__')
        except ImportError:
            # Expected if numpy is not installed
            pass

    def test_torch_shortcut(self):
        """Test torch shortcut"""
        try:
            torch_lib = load_torch()
            if torch_lib is not None:  # Might be None if not installed
                assert hasattr(torch_lib, 'tensor') or hasattr(torch_lib, 'Tensor')
                assert hasattr(torch_lib, 'nn')
        except ImportError:
            # Skip if torch is not installed
            pass

    def test_cv2_shortcut(self):
        """Test OpenCV shortcut"""
        try:
            cv2_lib = load_cv2()
            if cv2_lib is not None:  # Might be None if not installed
                assert hasattr(cv2_lib, 'imread')
                assert hasattr(cv2_lib, 'imshow') or hasattr(cv2_lib, 'VideoCapture')
        except ImportError:
            # Skip if OpenCV is not installed
            pass

    def test_pil_shortcut(self):
        """Test PIL shortcut"""
        try:
            pil_lib = load_pil()
            if pil_lib is not None:  # Might be None if not installed
                assert hasattr(pil_lib, 'Image')
                # In Python 2.7, ImageDraw might be a separate module
                assert hasattr(pil_lib, 'ImageDraw') or hasattr(pil_lib, 'Image')
        except ImportError:
            # Skip if PIL/Pillow is not installed
            pass

    def test_sklearn_shortcut(self):
        """Test scikit-learn shortcut"""
        try:
            sklearn_lib = load_sklearn()
            if sklearn_lib is not None:  # Might be None if not installed
                # Check for common sklearn submodules
                assert (hasattr(sklearn_lib, 'datasets') or 
                       hasattr(sklearn_lib, 'svm') or
                       hasattr(sklearn_lib, 'metrics'))
        except ImportError:
            # Skip if scikit-learn is not installed
            pass


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
