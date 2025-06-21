"""
Tests for registry functionality
"""

import pytest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from load.registry import LoadRegistry, REGISTRIES, PRIVATE_REGISTRIES

class TestLoadRegistry:
    def test_parse_source_pypi(self):
        """Test parsing PyPI source"""
        source_type, source_name = LoadRegistry.parse_source('requests')
        assert source_type == 'pypi'
        assert source_name == 'requests'

    def test_parse_source_github(self):
        """Test parsing GitHub source"""
        source_type, source_name = LoadRegistry.parse_source('user/repo')
        assert source_type == 'github'
        assert source_name == 'user/repo'

    def test_parse_source_local(self):
        """Test parsing local file source"""
        source_type, source_name = LoadRegistry.parse_source('./test.py')
        assert source_type == 'local'
        assert source_name == './test.py'

    def test_parse_source_url(self):
        """Test parsing URL source"""
        source_type, source_name = LoadRegistry.parse_source('https://example.com/lib.py')
        assert source_type == 'url'
        assert source_name == 'https://example.com/lib.py'

if __name__ == "__main__":
    pytest.main([__file__])
