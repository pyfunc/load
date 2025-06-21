"""
Tests for shortcuts
"""

import pytest
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from load.shortcuts import *
import pytest
from load.shortcuts import (
    load_pandas,
    load_numpy,
    load_requests,
    load_matplotlib,
    load_json,
    load_os,
    load_sys,
)
from load.shortcuts import np, pd, plt, requests, json, os, sys


class TestShortcuts:
    def test_shortcut_functions(self):
        """Test all shortcut functions"""
        # Test pandas shortcut
        pd = load_pandas()
        assert hasattr(pd, "DataFrame")
        assert hasattr(pd, "read_csv")

        # Test numpy shortcut
        np = load_numpy()
        assert hasattr(np, "array")
        assert hasattr(np, "mean")

        # Test requests shortcut
        requests = load_requests()
        assert hasattr(requests, "get")
        assert hasattr(requests, "post")

        # Test matplotlib shortcut
        plt = load_matplotlib()
        assert hasattr(plt, "plot")
        assert hasattr(plt, "show")

    def test_shortcut_aliases(self):
        """Test shortcut aliases"""
        # Test pandas alias
        pd = pd()
        assert hasattr(pd, "DataFrame")
        assert hasattr(pd, "read_csv")

        # Test numpy alias
        np = np()
        assert hasattr(np, "array")
        assert hasattr(np, "mean")

        # Test matplotlib alias
        plt = plt()
        assert hasattr(plt, "plot")
        assert hasattr(plt, "show")

    def test_shortcut_installation(self):
        """Test shortcut installation functionality"""

        # Mock the load function
        def mock_load(name, alias=None, install=True, force=False, silent=False):
            if name == "pandas":
                return type(
                    "MockPandas",
                    (object,),
                    {
                        "DataFrame": type("DataFrame", (object,), {}),
                        "read_csv": lambda: None,
                    },
                )()
            elif name == "numpy":
                return type(
                    "MockNumpy",
                    (object,),
                    {"array": lambda: None, "mean": lambda: None},
                )()
            elif name == "requests":
                return type(
                    "MockRequests",
                    (object,),
                    {"get": lambda: None, "post": lambda: None},
                )()
            return None

        from load.shortcuts import load

        original_load = load

        try:
            # Test pandas shortcut
            pd = load_pandas()
            assert hasattr(pd, "DataFrame")
            assert hasattr(pd, "read_csv")

            # Test numpy shortcut
            np = load_numpy()
            assert hasattr(np, "array")
            assert hasattr(np, "mean")

            # Test requests shortcut
            requests = load_requests()
            assert hasattr(requests, "get")
            assert hasattr(requests, "post")

        finally:
            load = original_load

    def test_shortcut_cache(self):
        """Test shortcut caching"""
        # First load
        pd1 = load_pandas()

        # Second load should return same object (cached)
        pd2 = load_pandas()
        assert pd1 is pd2

        # Test force reload
        pd3 = load_pandas(force=True)
        assert pd1 is not pd3

    def test_shortcut_errors(self):
        """Test error handling in shortcuts"""

        # Mock load to raise error
        def mock_load(name, alias=None, install=True, force=False, silent=False):
            raise ImportError(f"Cannot load {name}")

        from load.shortcuts import load

        original_load = load

        try:
            # Test error handling
            with pytest.raises(ImportError):
                load_pandas()
            with pytest.raises(ImportError):
                load_numpy()
            with pytest.raises(ImportError):
                load_requests()

        finally:
            load = original_load

    def test_stdlib_shortcuts(self):
        """Test shortcuts for stdlib modules"""
        # Test JSON shortcut
        json_lib = json()
        assert hasattr(json_lib, "loads")
        assert hasattr(json_lib, "dumps")

        # Test OS shortcut
        os_lib = os()
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
