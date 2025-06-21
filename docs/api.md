# 🔧 API Reference

## 📚 Main Functions

### `load.load(name, alias=None, install=True, force=False)`

Load a module with various options:

- `name`: Module name or path
- `alias`: Optional alias for the module
- `install`: Whether to install if not found
- `force`: Force reload from source

```python
import load

# Basic usage
json_lib = load.load('json')

# With alias
pd = load.load('pandas', alias='pd')

# Force reload
fresh_module = load.load('module', force=True)
```

### `load.info()`

Get information about the current state:

```python
info = load.info()
print(f"Cached modules: {info['cache_size']}")
print(f"Modules: {info['cached_modules']}")
```

### `load.enable_auto_print()`

Enable automatic result display:

```python
load.enable_auto_print()
```

### `load.disable_auto_print()`

Disable automatic result display:

```python
load.disable_auto_print()
```

### `load.set_print_limit(limit)`

Set character limit for auto-print:

```python
load.set_print_limit(1000)
```

### `load.configure_private_registry(name, index_url)`

Configure private package registry:

```python
load.configure_private_registry(
    "company",
    index_url="https://pypi.company.com/simple/"
)
```

## 📦 Registry Functions

### `load.add_registry(name, url)`

Add a new package registry:

```python
load.add_registry("github", "https://github.com")
```

### `load.remove_registry(name)`

Remove a registry:

```python
load.remove_registry("github")
```

### `load.list_registries()`

List all configured registries:

```python
registries = load.list_registries()
```

## 🛠️ Configuration Functions

### `load.set_cache_size(size)`

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
