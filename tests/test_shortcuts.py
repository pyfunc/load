"""
Tests for shortcuts
"""

import pytest
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from load.shortcuts import *
from load.core import load


class TestShortcuts:
    def test_shortcut_functions(self):
        """Test all shortcut functions"""
        # Test pandas shortcut
        pd = load_pandas()
        assert hasattr(pd, 'DataFrame')
        assert hasattr(pd, 'read_csv')
        
        # Test numpy shortcut
        np = load_numpy()
        assert hasattr(np, 'array')
        assert hasattr(np, 'mean')
        
        # Test requests shortcut
        requests = load_requests()
        assert hasattr(requests, 'get')
        assert hasattr(requests, 'post')
        
        # Test matplotlib shortcut
        plt = load_matplotlib()
        assert hasattr(plt, 'plot')
        assert hasattr(plt, 'show')
        
        # Test tensorflow shortcut
        tf = load_tensorflow()
        assert hasattr(tf, 'constant')
        assert hasattr(tf, 'Session')
        
        # Test torch shortcut
        torch = load_torch()
        assert hasattr(torch, 'tensor')
        assert hasattr(torch, 'nn')

    def test_shortcut_aliases(self):
        """Test shortcut aliases"""
        # Test pandas alias
        pd = load_pandas()
        assert pd.__name__ == 'pandas'
        
        # Test numpy alias
        np = load_numpy()
        assert np.__name__ == 'numpy'
        
        # Test requests alias
        requests = load_requests()
        assert requests.__name__ == 'requests'

    def test_shortcut_installation(self):
        """Test shortcut installation functionality"""
        # Mock the load function
        def mock_load(name, alias=None, install=True, force=False, silent=False):
            if name == 'pandas':
                return type('MockPandas', (object,), {
                    'DataFrame': type('DataFrame', (object,), {}),
                    'read_csv': lambda: None
                })()
            elif name == 'numpy':
                return type('MockNumpy', (object,), {
                    'array': lambda: None,
                    'mean': lambda: None
                })()
            elif name == 'requests':
                return type('MockRequests', (object,), {
                    'get': lambda: None,
                    'post': lambda: None
                })()
            return None
        
        from load.shortcuts import load_pandas, load_numpy, load_requests
        original_load = load
        load = mock_load
        
        try:
            # Test pandas installation
            pd = load_pandas()
            assert hasattr(pd, 'DataFrame')
            assert hasattr(pd, 'read_csv')
            
            # Test numpy installation
            np = load_numpy()
            assert hasattr(np, 'array')
            assert hasattr(np, 'mean')
            
            # Test requests installation
            requests = load_requests()
            assert hasattr(requests, 'get')
            assert hasattr(requests, 'post')
            
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
        assert pd3 is not pd1

    def test_shortcut_errors(self):
        """Test error handling in shortcuts"""
        # Mock load to raise error
        def mock_load(name, alias=None, install=True, force=False, silent=False):
            raise ImportError(f"Cannot load {name}")
        
        original_load = load
        load = mock_load
        
        try:
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
        json_lib = shortcuts.json()
        assert hasattr(json_lib, 'loads')
        assert hasattr(json_lib, 'dumps')

        # Test OS shortcut
        os_lib = shortcuts.os()
        assert hasattr(os_lib, 'getcwd')
        assert hasattr(os_lib, 'path')

        # Test SYS shortcut
        sys_lib = shortcuts.sys()
        assert hasattr(sys_lib, 'version')
        assert hasattr(sys_lib, 'path')

    def test_numpy_shortcut_safe(self):
        """Test numpy shortcut (safe - doesn't install)"""
        try:
            # Try to get numpy without installing
            np = shortcuts.load('numpy', install=False, silent=True)
            if np:
                assert hasattr(np, 'array')
        except ImportError:
            # Numpy not installed - this is OK for tests
            pass

if __name__ == "__main__":
    pytest.main([__file__, "-v"])