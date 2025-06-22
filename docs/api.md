# 🔧 API Reference

## 📚 Main Functions

### `load(name, alias=None, install=True, force=False)`

The main function to load modules. Can be used directly or as a callable.

```python
# These are equivalent
import load
json1 = load('json')
json2 = load.load('json')
```

Load a module with various options:

- `name` (str): Module name or path
- `alias` (str, optional): Alias to use for the module
- `install` (bool): Whether to install if not found (default: True)
- `force` (bool): Force reload from source (default: False)
- `**kwargs`: Additional arguments passed to the underlying import system

### `__call__(name, alias=None, install=True, force=False, **kwargs)`

Makes the module callable, equivalent to `load()`. This allows using the module directly as a function.

```python
import load

# These are equivalent
json1 = load('json')
json2 = load.load('json')
```

```python
import load

# Basic usage
json_lib = load.load('json')

# With alias
pd = load.load('pandas', alias='pd')

# Force reload
fresh_module = load.load('module', force=True)
```

### `info()`

Get information about the current state, including cache status and loaded modules.

```python
info = load.info()
print(f"Cached modules: {info['cache_size']}")
print(f"Modules: {info['cached_modules']}")

# Example output:
# {
#   'cache_size': 5,
#   'cached_modules': ['os', 'sys', 'json', 'pandas', 'numpy'],
#   'auto_print': True,
#   'print_limit': 1000
# }
```

### `enable_auto_print(limit=1000)`

Enable automatic result display with optional character limit.

```python
# Enable with default 1000 character limit
load.enable_auto_print()

# Or specify a custom limit
load.enable_auto_print(limit=500)
```

### `disable_auto_print()`

Disable automatic result display.

```python
load.disable_auto_print()
```

### `set_print_limit(limit)`

Set character limit for auto-print output.

```python
load.set_print_limit(1000)  # Show up to 1000 characters
```

### `configure_private_registry(name, index_url, **kwargs)`

Configure a private package registry.

```python
load.configure_private_registry(
    name="company",
    index_url="https://pypi.company.com/simple/",
    # Optional authentication
    username="user",
    password="pass"
)
```

Parameters:
- `name` (str): Registry name
- `index_url` (str): Base URL of the package index
- `**kwargs`: Additional arguments passed to pip's install command

## 📦 Registry Management

### `add_registry(name, url, **kwargs)`

Add a new package registry with optional authentication.

```python
# Basic usage
load.add_registry("github", "https://github.com")


# With authentication
load.add_registry(
    "private",
    "https://private.pypi.org/simple/",
    username="user",
    password="pass"
)
```

### `remove_registry(name)`

Remove a configured registry.

```python
load.remove_registry("github")
```

### `list_registries()`

List all configured registries and their configurations.

```python
registries = load.list_registries()
# Returns: [{'name': 'pypi', 'url': 'https://pypi.org/simple'}, ...]
```

## 🛠️ Configuration

### `set_cache_size(size)`

Set the maximum number of modules to keep in the cache.

```python
load.set_cache_size(100)  # Keep up to 100 modules in cache
```

### `clear_cache()`

Clear all cached modules.

```python
load.clear_cache()
```

### `install(package, version=None, upgrade=False, **kwargs)`

Install a package programmatically.

```python
# Basic installation
load.install('requests')


# Specific version
load.install('numpy', '1.21.0')


# Upgrade existing package
load.install('pandas', upgrade=True)


# With additional pip options
load.install('private-package', \
    index_url='https://pypi.company.com/simple/',
    extra_index_url='https://pypi.org/simple/'
)
```

### `uninstall(package, **kwargs)`

Uninstall a package.

```python
load.uninstall('package-name')
```

## 🔍 Utility Functions

### `is_installed(package)`

Check if a package is installed.

```python
if load.is_installed('numpy'):
    print('NumPy is installed')
```

### `get_version(package)`

Get the installed version of a package.

```python
version = load.get_version('numpy')
print(f'NumPy version: {version}')
```

## 🎯 Decorators

### `@load_decorator(*packages, **options)`

Decorator to automatically install and import packages before function execution.

```python
from load import load_decorator as load

@load('numpy', 'pandas', alias={'pandas': 'pd'})
def analyze_data():
    import numpy as np
    import pandas as pd
    # Your code here
```

Options:
- `alias`: Dict of package aliases
- `silent`: Suppress output (default: False)
- `force`: Force reinstallation (default: False)

Set maximum cache size in bytes:

```python
load.set_cache_size(100 * 1024 * 1024)  # 100MB
```

### `load.set_auto_install(enable)`

Enable/disable automatic package installation:

```python
load.set_auto_install(True)
```

### `load.set_install_timeout(seconds)`

Set timeout for package installation:

```python
load.set_install_timeout(30)  # 30 seconds
```

## 📁 File Loading Functions

### `load.load_file(path, alias=None)`

Load a Python file:

```python
utils = load.load_file('./utils.py')
```

### `load.load_module(name, path)`

Load a module from a specific path:

```python
module = load.load_module('my_module', '/path/to/module')
```

## 📊 Cache Management Functions

### `load.clear_cache()`

Clear the entire cache:

```python
load.clear_cache()
```

### `load.invalidate_cache(name)`

Invalidate cache for a specific module:

```python
load.invalidate_cache('requests')
```

## 🔄 Environment Variables

Load supports several environment variables for configuration:

- `LOAD_CACHE_SIZE`: Maximum cache size in bytes
- `LOAD_AUTO_PRINT`: Enable/disable auto-print globally (1/0)
- `LOAD_PRINT_LIMIT`: Character limit for auto-print
- `LOAD_NO_INSTALL`: Disable automatic package installation (1/0)

## 📚 Magic Import Syntax

The following syntaxes are supported:

```python
import load

# Standard library
load.json          # Standard library
load.os            # Standard library
load.sys           # Standard library
load.time          # Standard library
load.math          # Standard library

# External packages
load.requests      # PyPI package
load.numpy         # PyPI package
load.pandas        # PyPI package

# GitHub repositories
load.github.user/repo  # GitHub repository

# Local files
load.load('./file.py')  # Local Python file
```

## 🔗 Related Resources

- [Main Documentation](./index.md)
- [Installation Guide](./installation.md)
- [Usage Examples](./usage.md)
- [Development Guide](./development.md)
- [Example Files](https://github.com/pyfunc/load/tree/main/examples)
- [GitHub Repository](https://github.com/pyfunc/load)
- [API Reference](https://github.com/pyfunc/load/blob/main/docs/api.md)
