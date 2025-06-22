"""
Tests for Load core functionality
"""

import os
import sys
import tempfile

# Add src to path
src_dir = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', 'src')
)
sys.path.insert(0, src_dir)

import pytest  # noqa: E402

from load.core import load, _module_cache, info


class TestLoad:
    def setup_method(self):
        """Clear cache before each test"""
        _module_cache.clear()

    def test_load_stdlib_module(self):
        """Test loading stdlib module"""
        json_module = load("json", silent=True)
        assert hasattr(json_module, "loads")
        assert hasattr(json_module, "dumps")

    def test_load_with_alias(self):
        """Test loading with alias"""
        os_module = load("os", alias="operating_system", silent=True)
        assert hasattr(os_module, "path")
        assert "operating_system" in _module_cache

    def test_cache_functionality(self):
        """Test cache functionality"""
        # First load
        module1 = load("sys", silent=True)

        # Second load (from cache)
        module2 = load("sys", silent=True)

        # Should be same object from cache
        assert module1 is module2

    def test_force_reload(self):
        """Test forced reload"""
        # Load once
        load("time", silent=True)

        # Reload with force
        reloaded = load("time", force=True, silent=True)
        assert reloaded is not None

    def test_load_local_file(self):
        """Test loading local Python file"""
        # Create temporary Python file
        with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False) as f:
            f.write(
                """
TEST_VAR = "hello world"

def test_func():
    return "test function"
"""
            )
            temp_path = f.name

        try:
            # Load module from file
            temp_module = load(temp_path, silent=True)

            # Check contents
            assert hasattr(temp_module, "test_func")
            assert hasattr(temp_module, "TEST_VAR")
            assert temp_module.TEST_VAR == "hello world"
            assert temp_module.test_func() == "test function"

            # Test loading from relative path
            test_dir = os.path.join(
                os.path.dirname(__file__), "test_data"
            )
            test_file = os.path.join(test_dir, "test_module.py")

            # Create test directory if it doesn't exist
            if not os.path.exists(test_dir):
                os.makedirs(test_dir)

            with open(test_file, "w") as f:
                f.write("def test_func(): return 'test'")

            mod = load(test_file, silent=True)
            assert hasattr(mod, "test_func")
            assert mod.test_func() == "test"

            # Cleanup
            try:
                os.remove(test_file)
                os.rmdir(test_dir)
            except OSError:
                pass

        finally:
            # Clean up
            os.unlink(temp_path)

    def test_load_nonexistent_module(self):
        """Test loading nonexistent module without auto-install"""
        with pytest.raises(ImportError):
            load("definitely_nonexistent_module_12345", install=False, silent=True)

    def test_info_function(self):
        """Test info function"""
        # Load some modules first
        load("json", silent=True)
        load("os", silent=True)

        info_data = info()
        assert isinstance(info_data, dict)
        assert "cache_size" in info_data
        assert "cached_modules" in info_data
        assert info_data["cache_size"] >= 2
        assert "json" in info_data["cached_modules"]
        assert "os" in info_data["cached_modules"]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
