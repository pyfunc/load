"""
Registry management for Load
"""

import os
import subprocess
import sys
import tempfile
import zipfile

# Import compatibility layer
from ._compat import import_module, Optional, urlretrieve, urlopen

# Registry configurations
REGISTRIES = {
    "pypi": {
        "install_cmd": [sys.executable, "-m", "pip", "install"],
        "description": "PyPI - Official Python Package Index",
    },
    "github": {
        "install_cmd": [
            sys.executable,
            "-m",
            "pip",
            "install",
            "git+https://github.com/",
        ],
        "description": "GitHub repositories",
    },
    "gitlab": {
        "install_cmd": [
            sys.executable,
            "-m",
            "pip",
            "install",
            "git+https://gitlab.com/",
        ],
        "description": "GitLab repositories",
    },
    "url": {"install_cmd": None, "description": "Direct URL download"},
    "local": {"install_cmd": None, "description": "Local files and directories"},
}

# Private registries
PRIVATE_REGISTRIES = {
    "company": {
        "index_url": "https://pypi.company.com/simple/",
        "install_cmd": [sys.executable, "-m", "pip", "install", "--index-url"],
        "description": "Company private PyPI",
    },
    "private_gitlab": {
        "base_url": "https://gitlab.company.com/",
        "token": os.getenv("GITLAB_TOKEN"),
        "install_cmd": None,
        "description": "Private GitLab with token",
    },
}


class LoadRegistry:
    """Registry manager for Load"""

    @staticmethod
    def parse_source(name: str):
        """Parse package source"""
        if "://" in name:
            return "url", name
        elif "/" in name:
            parts = name.split("/")
            # Check if the first part is a known private registry
            if parts[0] in PRIVATE_REGISTRIES:
                return parts[0], name
            # Check for GitHub/GitLab URLs
            elif "github.com" in name:
                return "github", name
            elif "gitlab.com" in name:
                return "gitlab", name
            # Default to GitHub for user/repo format
            elif len(parts) == 2 and "." not in parts[0]:
                return "github", name
            else:
                # If not matched above, treat as PyPI package with slash in name
                return "pypi", name
        elif name.endswith(".py") or name.startswith("./") or name.startswith("../"):
            return "local", name
        else:
            return "pypi", name

    @staticmethod
    def install_from_pypi(name, registry="pypi"):
        # type: (str, str) -> bool
        """Install from PyPI or private registry"""
        if registry in PRIVATE_REGISTRIES:
            config = PRIVATE_REGISTRIES[registry]
            cmd = config["install_cmd"].copy()
            if "index_url" in config:
                cmd.extend([config["index_url"], name])
            else:
                cmd.append(name)
        else:
            cmd = REGISTRIES["pypi"]["install_cmd"] + [name]

        print("📦 Installing {0} from {1}...".format(name, registry))
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.returncode == 0

    @staticmethod
    def install_from_github(self, repo):
        # type: (str) -> bool
        """Install from GitHub"""
        if not repo.startswith("https://"):
            repo = "https://github.com/{0}".format(repo)

        cmd = [sys.executable, "-m", "pip", "install", f"git+{repo}"]
        print("📦 Installing from GitHub: {0}".format(repo))
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.returncode == 0

    @staticmethod
    def install_from_gitlab(self, repo, token=None):
        # type: (str, Optional[str]) -> bool
        """Install from GitLab"""
        if not repo.startswith("https://"):
            repo = "https://gitlab.com/{0}".format(repo)

        if token:
            repo_with_token = repo.replace("https://", "https://oauth2:{0}@".format(token))
            cmd = [sys.executable, "-m", "pip", "install", "git+{0}".format(repo_with_token)]
        else:
            cmd = [sys.executable, "-m", "pip", "install", "git+{0}".format(repo)]

        print("📦 Installing from GitLab: {0}".format(repo))
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.returncode == 0

    def install_from_url(self, url):
        # type: (str) -> bool
        """Install package from URL"""
        try:
            # Download the file
            print("📦 Downloading from URL: {0}".format(url))
            filename = os.path.basename(url)
            filepath = os.path.join(self.temp_dir, filename)
            urllib.request.urlretrieve(url, filepath)

            # If it's a ZIP file
            if filepath.endswith(".zip"):
                with zipfile.ZipFile(filepath, "r") as zip_ref:
                    zip_ref.extractall(self.temp_dir)
                # Try to find and import the package
                for root, dirs, files in os.walk(self.temp_dir):
                    for file in files:
                        if file.endswith(".py"):
                            try:
                                spec = importlib.util.spec_from_file_location(
                                    os.path.splitext(file)[0], os.path.join(root, file)
                                )
                                if spec:
                                    module = importlib.util.module_from_spec(spec)
                                    spec.loader.exec_module(module)
                                    return True
                            except Exception:
                                continue

            # If it's a single Python file
            elif filepath.endswith(".py"):
                try:
                    spec = importlib.util.spec_from_file_location(
                        os.path.splitext(filename)[0], filepath
                    )
                    if spec:
                        module = importlib.util.module_from_spec(spec)
                        spec.loader.exec_module(module)
                        return True
                except Exception:
                    pass

            return True

        except Exception as e:
            print("❌ Error installing from URL: {0}".format(e))
            return False


def add_registry(name, config):
    # type: (str, dict) -> None
    """Add new registry"""
    PRIVATE_REGISTRIES[name] = config


def list_registries():
    # type: () -> None
    """List available registries"""
    print("🔧 Available registries:")
    print("\n📦 Public:")
    for name, config in REGISTRIES.items():
        print(f"  {name}: {config['description']}")

    print("\n🔒 Private:")
    for name, config in PRIVATE_REGISTRIES.items():
        print(f"  {name}: {config['description']}")


def configure_private_registry(name, index_url=None, token=None, base_url=None):
    # type: (str, Optional[str], Optional[str], Optional[str]) -> None
    """Quick private registry configuration"""
    config = {"description": "Private registry: {0}".format(name)}

    if index_url:
        config.update(
            {
                "index_url": index_url,
                "install_cmd": [sys.executable, "-m", "pip", "install", "--index-url"],
            }
        )

    if token:
        config["token"] = token

    if base_url:
        config["base_url"] = base_url

    PRIVATE_REGISTRIES[name] = config
    print("✅ Configured private registry: {0}".format(name))
