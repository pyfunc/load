"""
Tests for the @load decorator functionality.
"""

import os
import sys
import pytest
from unittest.mock import patch, MagicMock

# Add src to path
src_dir = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', 'src')
)
sys.path.insert(0, src_dir)

from load import load_decorator as load, core


class TestLoadDecorator:
    """Test cases for the @load decorator."""
    
    def test_basic_usage(self):
        """Test basic usage of the @load decorator."""
        # This will be patched to avoid actual imports
        with patch('load.core.load') as mock_load:
            mock_load.return_value = 'mocked_module'
            
            @load('numpy', 'pandas')
            def test_func():
                return 'success'
            
            # The function should work
            assert test_func() == 'success'
            
            # Should have called load for each dependency
            assert mock_load.call_count == 2
            assert mock_load.call_args_list[0][0][0] == 'numpy'
            assert mock_load.call_args_list[1][0][0] == 'pandas'
    
    def test_with_aliases(self):
        """Test using aliases with the @load decorator."""
        with patch('load.core.load') as mock_load:
            mock_load.return_value = 'mocked_module'
            
            @load('np=numpy', 'pd=pandas')
            def test_func():
                return 'success'
            
            # The function should work
            assert test_func() == 'success'
            
            # Should have called load for each dependency
            assert mock_load.call_count == 2
            assert mock_load.call_args_list[0][0][0] == 'numpy'
            assert mock_load.call_args_list[1][0][0] == 'pandas'
    
    def test_silent_mode(self):
        """Test silent mode of the @load decorator."""
        with patch('load.core.load') as mock_load:
            mock_load.return_value = 'mocked_module'
            
            @load('numpy', 'pandas', silent=True)
            def test_func():
                return 'success'
            
            # The function should work
            assert test_func() == 'success'
            
            # Should have called load with silent=True
            for call in mock_load.call_args_list:
                assert call[1]['silent'] is True
    
    def test_multiple_calls(self):
        """Test that modules are only loaded once with multiple calls."""
        with patch('load.core.load') as mock_load:
            mock_load.return_value = 'mocked_module'
            
            @load('numpy')
            def test_func():
                return 'success'
            
            # Call multiple times
            for _ in range(3):
                assert test_func() == 'success'
            
            # Should have only called load once due to caching
            assert mock_load.call_count == 1
    
    def test_cache_info_works(self):
        """Test that test_cache_info function works correctly."""
        from load import test_cache_info
        
        # Just test that it runs without errors
        test_cache_info()
        
        # We can't easily test the output since it depends on the environment
        assert True
    
    def test_import_error_handling(self):
        """Test that import errors are properly handled."""
        with patch('load.core.load', side_effect=ImportError("Test error")) as mock_load:
            @load('nonexistent_package')
            def test_func():
                return 'success'
            
            # The function should still work even if imports fail
            assert test_func() == 'success'


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
