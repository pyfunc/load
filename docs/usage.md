# 💪 Basic Usage

Load provides a modern and intuitive way to import Python packages. Here are the basic usage patterns:

## 📚 Magic Import

The core feature of Load is its magic import system:

```python
import load

# Standard library modules
json_lib = load.json
os_lib = load.os
sys_lib = load.sys

# External packages (auto-install if available)
requests_lib = load.requests  # Automatically installs requests
pandas_lib = load.pd         # Automatically installs pandas
```

## 📁 Local File Loading

Load can also load local Python files:

```python
import load

# Load local Python files
utils = load.load('./utils.py')
config = load.load('../config/settings.py')

# With aliases
my_tools = load.load('./tools.py', alias='tools')
```

## 🎯 Auto-Print

Load includes an auto-print feature that shows results like Jupyter notebooks:

```python
import load

# Enable auto-print
load.enable_auto_print()

# Now loading shows information
time_lib = load.time  # Output: ✅ time: module loaded

# Control print verbosity
load.set_print_limit(100)  # Set character limit
load.disable_auto_print()  # Disable auto-print
```

## 📊 Cache Management

Load uses RAM caching to speed up repeated module loading:

```python
import load

# Check cache status
info = load.info()
print(f"Cached modules: {info['cache_size']}")
print(f"Modules: {info['cached_modules']}")

# Force reload
fresh_module = load.load('some_module', force=True)
```

## 📦 Package Installation

Load automatically installs missing packages when possible:

```python
import load

# Automatically installs and loads packages
requests_lib = load.requests  # Installs requests if not present
numpy_lib = load.np           # Installs numpy if not present
```

## 🛠️ Advanced Usage

### Registry Configuration

Load supports multiple package registries:

```python
import load

# Configure private registry
load.configure_private_registry(
    "company",
    index_url="https://pypi.company.com/simple/"
)

# Load from private registry
company_lib = load.load("company/package-name")
```

### Custom Aliases

Create custom aliases for commonly used modules:

```python
import load

# Create alias
load.alias("np", "numpy")

# Use alias
np = load.np  # Loads numpy
```

### Error Handling

Load provides detailed error messages when loading fails:

```python
import load

try:
    non_existent = load.load("non_existent_module")
except load.LoadError as e:
    print(f"Error: {e}")
```

## 🔗 Related Resources

- [Main Documentation](./index.md)
- [Installation Guide](./installation.md)
- [API Reference](./api.md)
- [Development Guide](./development.md)
- [Example Files](https://github.com/pyfunc/load/tree/main/examples)
- [GitHub Repository](https://github.com/pyfunc/load)
