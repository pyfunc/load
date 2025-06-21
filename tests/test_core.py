"""
Tests for Load core functionality
"""

import pytest
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from load.core import load, _module_cache

class TestLoad:
    def test_load_stdlib_module(self):
        """Test loading stdlib module"""
        json_module = load('json', silent=True)
        assert hasattr(json_module, 'loads')
        assert hasattr(json_module, 'dumps')

    def test_load_with_alias(self):
        """Test loading with alias"""
        os_module = load('os', alias='operating_system', silent=True)
        assert hasattr(os_module, 'path')
        assert 'operating_system' in _module_cache

    def test_cache_functionality(self):
        """Test cache functionality"""
        # First load
        module1 = load('sys', silent=True)

        # Second load (from cache)
        module2 = load('sys', silent=True)

        # Should be same object from cache
        assert module1 is module2

    def test_force_reload(self):
        """Test forced reload"""
        # Load once
        load('time', silent=True)

        # Reload with force
        reloaded = load('time', force=True, silent=True)
        assert reloaded is not None

if __name__ == "__main__":
    pytest.main([__file__])
