"""
Tests for Load registry functionality
"""

import pytest
import os
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from src.load.registry import LoadRegistry, REGISTRIES, PRIVATE_REGISTRIES
from src.load.registry import list_registries, add_registry, configure_private_registry


class TestRegistry:
    def test_list_registries(self):
        """Test listing available registries"""
        # Test public registries
        public_registries = list_registries()
        assert isinstance(public_registries, list)
        assert len(public_registries) > 0
        assert any("PyPI" in reg["description"] for reg in public_registries)
        assert any("GitHub" in reg["description"] for reg in public_registries)

        # Test private registries
        private_registries = list_registries(private=True)
        assert isinstance(private_registries, list)
        assert len(private_registries) > 0
        assert any(
            "Company private" in reg["description"] for reg in private_registries
        )

    def test_add_registry(self):
        """Test adding new registry"""
        test_name = "test_registry"
        test_config = {
            "description": "Test registry",
            "install_cmd": ["pip", "install"],
            "base_url": "https://test.registry.org",
        }

        add_registry(test_name, test_config)

        # Verify registry was added
        assert test_name in PRIVATE_REGISTRIES
        assert PRIVATE_REGISTRIES[test_name] == test_config

    def test_configure_private_registry(self):
        """Test configuring private registry"""
        test_name = "test_private"

        # Test PyPI-style private registry
        configure_private_registry(
            test_name, index_url="https://test.pypi.org/simple/", token="test-token"
        )

        assert test_name in PRIVATE_REGISTRIES
        assert (
            PRIVATE_REGISTRIES[test_name]["index_url"]
            == "https://test.pypi.org/simple/"
        )
        assert PRIVATE_REGISTRIES[test_name]["token"] == "test-token"

        # Test GitLab-style private registry
        configure_private_registry(
            test_name + "_gitlab",
            base_url="https://gitlab.test.org/",
            token="gitlab-token",
        )
        assert test_name + "_gitlab" in PRIVATE_REGISTRIES
        assert (
            PRIVATE_REGISTRIES[test_name + "_gitlab"]["base_url"]
            == "https://gitlab.test.org/"
        )
        assert PRIVATE_REGISTRIES[test_name + "_gitlab"]["token"] == "gitlab-token"

    def test_parse_source(self):
        """Test source parsing"""
        registry = LoadRegistry()

        # Test different source types
        assert registry.parse_source("requests") == ("pypi", "requests")
        assert registry.parse_source("user/repo") == ("github", "user/repo")
        assert registry.parse_source("https://github.com/user/repo") == (
            "url",
            "https://github.com/user/repo",
        )
        assert registry.parse_source("company/package") == (
            "company",
            "company/package",
        )
        assert registry.parse_source("private_gitlab/package") == (
            "private_gitlab",
            "private_gitlab/package",
        )
        assert registry.parse_source("http://example.com/package.zip") == (
            "url",
            "http://example.com/package.zip",
        )

    def test_install_from_pypi(self):
        """Test PyPI installation (mocked)"""
        registry = LoadRegistry()

        # Mock subprocess.run
        def mock_run(cmd, *args, **kwargs):
            return type("MockResult", (object,), {"returncode": 0})()

        import subprocess

        original_run = subprocess.run
        subprocess.run = mock_run

        try:
            # Test public PyPI
            assert registry.install_from_pypi("requests") is True

            # Test private registry
            assert registry.install_from_pypi("package", "company") is True

        finally:
            subprocess.run = original_run

    def test_install_from_github(self):
        """Test GitHub installation (mocked)"""
        registry = LoadRegistry()

        # Mock subprocess.run
        def mock_run(cmd, *args, **kwargs):
            return type("MockResult", (object,), {"returncode": 0})()

        import subprocess

        original_run = subprocess.run
        subprocess.run = mock_run

        try:
            assert registry.install_from_github("user/repo") is True
            assert registry.install_from_github("https://github.com/user/repo") is True

        finally:
            subprocess.run = original_run

    def test_install_from_gitlab(self):
        """Test GitLab installation (mocked)"""
        registry = LoadRegistry()

        # Mock subprocess.run
        def mock_run(cmd, *args, **kwargs):
            return type("MockResult", (object,), {"returncode": 0})()

        import subprocess

        original_run = subprocess.run
        subprocess.run = mock_run

        try:
            assert registry.install_from_gitlab("user/repo") is True
            assert (
                registry.install_from_gitlab(
                    "https://gitlab.com/user/repo", "test-token"
                )
                is True
            )

        finally:
            subprocess.run = original_run

    def test_install_from_url(self):
        """Test URL installation (mocked)"""
        registry = LoadRegistry()

        # Mock urllib.request.urlretrieve
        def mock_urlretrieve(url, filename):
            with open(filename, "w") as f:
                f.write("test content")
            return filename, None

        # Mock zipfile.ZipFile
        class MockZipFile:
            def __init__(self, *args, **kwargs):
                pass

            def extractall(self, *args, **kwargs):
                pass

            def __enter__(self):
                return self

            def __exit__(self, *args):
                pass

        import urllib.request
        import zipfile
        import tempfile
        import os

        # Create temporary directory
        with tempfile.TemporaryDirectory() as temp_dir:
            # Set temp directory
            registry.temp_dir = temp_dir

            original_urlretrieve = urllib.request.urlretrieve
            original_zipfile = zipfile.ZipFile

            urllib.request.urlretrieve = mock_urlretrieve
            zipfile.ZipFile = MockZipFile

            try:
                # Test ZIP installation
                assert (
                    registry.install_from_url("http://example.com/package.zip") is True
                )
                # Test single file installation
                assert registry.install_from_url("http://example.com/module.py") is True
            finally:
                # Restore original functions
                urllib.request.urlretrieve = original_urlretrieve
                zipfile.ZipFile = original_zipfile


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
