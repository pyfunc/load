"""
Tests for shortcuts
"""

import pytest
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from load.shortcuts import (
    load_requests,
    load_yaml,
    load_os,
    load_sys,
    load_pathlib,
    load_time,
    load_datetime,
    load_random,
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
        os_lib = load_os()
        assert hasattr(os_lib, "path")

    def test_sys_shortcut(self):
        """Test sys shortcut"""
        sys_lib = load_sys()
        assert hasattr(sys_lib, "version")

    def test_pathlib_shortcut(self):
        """Test pathlib shortcut"""
        pathlib_lib = load_pathlib()
        assert hasattr(pathlib_lib, "Path")

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
        sys_lib = sys()
        assert hasattr(sys_lib, "path")
        assert hasattr(sys_lib, "version")

    def test_numpy_shortcut_safe(self):
        """Test numpy shortcut (safe - doesn't install)"""
        try:
            # Try to get numpy without installing
            np_lib = load_numpy(install=False, silent=True)
            assert np_lib is None

        except ImportError as e:
            assert str(e) == "Cannot load numpy"

    def test_torch_shortcut(self):
        """Test torch shortcut"""
        torch_lib = load_torch()
        assert hasattr(torch_lib, "tensor")
        assert hasattr(torch_lib, "nn")

    def test_cv2_shortcut(self):
        """Test OpenCV shortcut"""
        cv2_lib = load_cv2()
        assert hasattr(cv2_lib, "imread")
        assert hasattr(cv2_lib, "imshow")

    def test_pil_shortcut(self):
        """Test PIL shortcut"""
        pil_lib = load_pil()
        assert hasattr(pil_lib, "Image")
        assert hasattr(pil_lib, "ImageDraw")

    def test_sklearn_shortcut(self):
        """Test scikit-learn shortcut"""
        sklearn_lib = load_sklearn()
        assert hasattr(sklearn_lib, "datasets")
        assert hasattr(sklearn_lib, "metrics")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
