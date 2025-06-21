"""
Registry management for Load
"""

import sys
import os
import subprocess
import tempfile
import urllib.request
import zipfile
from pathlib import Path

# Registry configurations
REGISTRIES = {
    'pypi': {
        'install_cmd': [sys.executable, "-m", "pip", "install"],
        'description': 'PyPI - Official Python Package Index'
    },
    'github': {
        'install_cmd': [sys.executable, "-m", "pip", "install", "git+https://github.com/"],
        'description': 'GitHub repositories'
    },
    'gitlab': {
        'install_cmd': [sys.executable, "-m", "pip", "install", "git+https://gitlab.com/"],
        'description': 'GitLab repositories'
    },
    'url': {
        'install_cmd': None,
        'description': 'Direct URL download'
    },
    'local': {
        'install_cmd': None,
        'description': 'Local files and directories'
    }
}

# Private registries
PRIVATE_REGISTRIES = {
    'company': {
        'index_url': 'https://pypi.company.com/simple/',
        'install_cmd': [sys.executable, "-m", "pip", "install", "--index-url"],
        'description': 'Company private PyPI'
    },
    'private_gitlab': {
        'base_url': 'https://gitlab.company.com/',
        'token': os.getenv('GITLAB_TOKEN'),
        'install_cmd': None,
        'description': 'Private GitLab with token'
    }
}

class LoadRegistry:
    """Registry manager for Load"""

    @staticmethod
    def parse_source(name: str):
        """Parse package source"""
        if '://' in name:
            return 'url', name
        elif '/' in name and ('github.com' in name or name.count('/') >= 1):
            if 'github.com' in name:
                return 'github', name
            elif 'gitlab.com' in name:
                return 'gitlab', name
            else:
                return 'github', name
        elif name.endswith('.py') or name.startswith('./') or name.startswith('../'):
            return 'local', name
        else:
            return 'pypi', name

    @staticmethod
    def install_from_pypi(name: str, registry: str = 'pypi') -> bool:
        """Install from PyPI or private registry"""
        if registry in PRIVATE_REGISTRIES:
            config = PRIVATE_REGISTRIES[registry]
            cmd = config['install_cmd'].copy()
            if 'index_url' in config:
                cmd.extend([config['index_url'], name])
            else:
                cmd.append(name)
        else:
            cmd = REGISTRIES['pypi']['install_cmd'] + [name]

        print(f"📦 Installing {name} from {registry}...")
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.returncode == 0

    @staticmethod
    def install_from_github(repo: str) -> bool:
        """Install from GitHub"""
        if not repo.startswith('https://'):
            repo = f"https://github.com/{repo}"

        cmd = [sys.executable, "-m", "pip", "install", f"git+{repo}"]
        print(f"📦 Installing from GitHub: {repo}")
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.returncode == 0

    @staticmethod
    def install_from_gitlab(repo: str, token: str = None) -> bool:
        """Install from GitLab"""
        if not repo.startswith('https://'):
            repo = f"https://gitlab.com/{repo}"

        if token:
            repo_with_token = repo.replace('https://', f'https://oauth2:{token}@')
            cmd = [sys.executable, "-m", "pip", "install", f"git+{repo_with_token}"]
        else:
            cmd = [sys.executable, "-m", "pip", "install", f"git+{repo}"]

        print(f"📦 Installing from GitLab: {repo}")
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.returncode == 0

    @staticmethod
    def install_from_url(url: str) -> bool:
        """Download and install from URL"""
        print(f"📦 Downloading from URL: {url}")

        try:
            with tempfile.TemporaryDirectory() as temp_dir:
                if url.endswith('.zip'):
                    zip_path = Path(temp_dir) / "package.zip"
                    urllib.request.urlretrieve(url, zip_path)

                    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                        zip_ref.extractall(temp_dir)

                    for root, dirs, files in os.walk(temp_dir):
                        if 'setup.py' in files:
                            cmd = [sys.executable, "-m", "pip", "install", root]
                            result = subprocess.run(cmd, capture_output=True)
                            return result.returncode == 0

                elif url.endswith('.py'):
                    file_path = Path(temp_dir) / "module.py"
                    urllib.request.urlretrieve(url, file_path)

                    import site
                    user_site = site.getusersitepackages()
                    os.makedirs(user_site, exist_ok=True)

                    module_name = Path(url).stem
                    target_path = Path(user_site) / f"{module_name}.py"
                    file_path.rename(target_path)
                    return True

        except Exception as e:
            print(f"❌ Error downloading from URL: {e}")
            return False

        return False

def add_registry(name: str, config: dict):
    """Add new registry"""
    PRIVATE_REGISTRIES[name] = config

def list_registries():
    """List available registries"""
    print("🔧 Available registries:")
    print("\n📦 Public:")
    for name, config in REGISTRIES.items():
        print(f"  {name}: {config['description']}")

    print("\n🔒 Private:")
    for name, config in PRIVATE_REGISTRIES.items():
        print(f"  {name}: {config['description']}")

def configure_private_registry(name: str, index_url: str = None,
                             token: str = None, base_url: str = None):
    """Quick private registry configuration"""
    config = {'description': f'Private registry: {name}'}

    if index_url:
        config.update({
            'index_url': index_url,
            'install_cmd': [sys.executable, "-m", "pip", "install", "--index-url"]
        })

    if token:
        config['token'] = token

    if base_url:
        config['base_url'] = base_url

    PRIVATE_REGISTRIES[name] = config
    print(f"✅ Configured private registry: {name}")
