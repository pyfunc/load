# 📦 Core Features

Load offers several powerful features that make Python imports more intuitive and efficient:

## 🚀 Magic Import

- Access modules through simple dot notation
- Automatic loading of standard library modules
- Intelligent package installation for external packages
- Works seamlessly with both standard and external packages

## 📊 Auto-Print

- Shows results automatically like in Jupyter notebooks
- Configurable verbosity levels
- Can be enabled/disabled globally or per-session
- Customizable character limits

## 💾 RAM Caching

- Fast repeated module loading
- Configurable cache size
- Automatic cache management
- Force reload option available

## 🔧 Auto-Installation

- Automatic detection of missing packages
- Smart installation from multiple sources
- Works with PyPI, GitHub, and private registries
- Configurable installation behavior

## 🎯 Smart Detection

- Automatic detection of package types
- Smart resolution of package names
- Support for multiple package formats
- Intelligent error handling

## 📁 Local File Support

- Seamless loading of local Python files
- Support for relative and absolute paths
- Custom alias support
- Automatic module reloading

## 📦 Multiple Registries

- Support for multiple package sources:
  - PyPI (default)
  - GitHub repositories
  - GitLab repositories
  - Private PyPI registries
  - Direct URLs
  - Local files

## 🔒 Security Features

- Configurable package installation
- Package source verification
- Environment isolation options
- Security-focused defaults

## 📈 Performance Optimizations

- Intelligent caching strategy
- Optimized import paths
- Lazy loading support
- Memory-efficient design

## 🔄 Configuration Options

Load provides several configuration options:

```python
import load

# Configure cache
load.set_cache_size(100 * 1024 * 1024)  # 100MB

# Configure auto-print
load.set_print_limit(1000)  # 1000 characters
load.enable_auto_print()

# Configure package installation
load.set_auto_install(True)
load.set_install_timeout(30)  # 30 seconds
```
