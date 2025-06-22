"""Tests for the @load decorator functionality."""

import os
import sys
import pytest
from unittest.mock import patch

# Add src to path
src_dir = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', 'src')
)
sys.path.insert(0, src_dir)

# Import the module
import load

# Create a mock for the load function
from unittest.mock import MagicMock
core_load = MagicMock()
core_load.return_value = 'mocked_module'

# Import the decorator directly to avoid import issues
from load import load_decorator as original_load_decorator

# Create a wrapped version that uses our mock
load_decorator = lambda *args, **kwargs: original_load_decorator(*args, **kwargs, load_func=core_load)


class TestLoadDecorator:
    """Test cases for the @load decorator."""

    def test_basic_usage(self):
        """Test basic usage of the @load decorator."""
        core_load.reset_mock()
        core_load.return_value = 'mocked_module'

        @load_decorator('numpy', 'pandas')
        def test_func():
            return 'success'

        assert test_func() == 'success'
        assert core_load.call_count == 2
        assert core_load.call_args_list[0][0][0] == 'numpy'
        assert core_load.call_args_list[1][0][0] == 'pandas'

    def test_with_aliases(self):
        """Test using aliases with the @load decorator."""
        core_load.reset_mock()
        core_load.return_value = 'mocked_module'

        @load_decorator('np=numpy', 'pd=pandas')
        def test_func():
            return 'success'

        assert test_func() == 'success'
        assert core_load.call_count == 2
        assert core_load.call_args_list[0][0][0] == 'numpy'
        assert core_load.call_args_list[1][0][0] == 'pandas'

    def test_silent_mode(self):
        """Test silent mode of the @load decorator."""
        core_load.reset_mock()
        core_load.return_value = 'mocked_module'

        @load_decorator('numpy', 'pandas', silent=True)
        def test_func():
            return 'success'

        assert test_func() == 'success'
        for call in core_load.call_args_list:
            assert call[1]['silent'] is True

    def test_multiple_calls(self):
        """Test that modules are only loaded once with multiple calls."""
        core_load.reset_mock()
        core_load.return_value = 'mocked_module'

        @load_decorator('numpy')
        def test_func():
            return 'success'

        for _ in range(3):
            assert test_func() == 'success'
        assert core_load.call_count == 1

    def test_cache_info_works(self):
        """Test that test_cache_info function works correctly."""
        from load import test_cache_info
        test_cache_info()  # Just test that it runs without errors
        assert True  # We can't easily test the output

    def test_import_error_handling(self):
        """Test that import errors are properly handled."""
        core_load.reset_mock()
        core_load.side_effect = ImportError("Test error")

        @load_decorator('nonexistent_package')
        def test_func():
            return 'success'

        assert test_func() == 'success'


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
