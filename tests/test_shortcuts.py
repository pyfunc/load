"""
Tests for shortcuts
"""

import pytest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from load import shortcuts

class TestShortcuts:
    def test_numpy_shortcut(self):
        """Test numpy shortcut"""
        try:
            np = shortcuts.np()
            # If numpy is available, check it
            if np:
                assert hasattr(np, 'array')
        except ImportError:
            # Numpy not installed - OK for test
            pass

    def test_stdlib_shortcuts(self):
        """Test shortcuts for stdlib modules"""
        # These should always work
        json_lib = shortcuts.load('json')
        assert hasattr(json_lib, 'loads')

if __name__ == "__main__":
    pytest.main([__file__])
