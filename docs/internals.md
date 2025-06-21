# 🧠 Internals: How Load Works

This document explains the internal workings of the Load module, focusing on package loading, memory management, and the module's architecture.

## Table of Contents
- [Module Loading Flow](#module-loading-flow)
- [Memory Management](#memory-management)
- [Module Caching](#module-caching)
- [Lazy Loading](#lazy-loading)
- [Performance Considerations](#performance-considerations)
- [Troubleshooting](#troubleshooting)

## Module Loading Flow

When you use `load.package_name`, here's what happens under the hood:

1. **Attribute Access**
   - The `__getattr__` method in `LoadModule` is triggered
   - This is the entry point for all dynamic imports
   - [Source: `LoadModule.__getattr__` in `__init__.py`](cci:1://file:///home/tom/github/pyfunc/load/src/load/__init__.py:31:4-177:61)

2. **Module Resolution**
   - Checks if the module is already imported in `sys.modules`
   - If not, attempts to import it using Python's import system
   - [Source: Dynamic import in `core.py`](cci:1://file:///home/tom/github/pyfunc/load/src/load/core.py:0:0-0:0)

3. **Package Installation (if needed)**
   - If the module isn't found, attempts to install it
   - Supports PyPI, GitHub, and local packages
   - [Source: Package installation logic](cci:1://file:///home/tom/github/pyfunc/load/src/load/core.py:0:0-0:0)

## Memory Management

### Module Caching
- Loaded modules are cached in `sys.modules`
- Subsequent imports return the cached module instance
- This is standard Python behavior that Load leverages

### Garbage Collection
- Python's garbage collector automatically cleans up unused modules
- Modules remain in memory as long as there are references to them
- Use `del` to remove references when done with large modules

### Memory Profiling
To monitor memory usage:

```python
import sys
import psutil
import os

def get_memory_usage():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / 1024 / 1024  # MB

print(f"Memory before: {get_memory_usage():.2f} MB")
import numpy as np
print(f"Memory after numpy: {get_memory_usage():.2f} MB")
```

## Lazy Loading

Load implements lazy loading to minimize memory usage:

1. **On-Demand Loading**
   - Modules are only loaded when first accessed
   - This is handled by `__getattr__` in `LoadModule`
   - [Source: Lazy loading implementation](cci:1://file:///home/tom/github/pyfunc/load/src/load/__init__.py:31:4-177:61)

2. **Submodule Loading**
   - For packages like `matplotlib.pyplot`, submodules are loaded on-demand
   - This prevents loading unnecessary components
   - [Source: Submodule handling](cci:1://file:///home/tom/github/pyfunc/load/src/load/__init__.py:243:4-261:16)

## Performance Considerations

### Import Performance
- First import of a module is the most expensive
- Subsequent imports are nearly instant (from cache)
- Use `import_aliases()` for bulk imports:
  ```python
  from load import import_aliases
  np, pd, plt = import_aliases('numpy', 'pandas', 'plt=matplotlib.pyplot')
  ```

### Memory Optimization Tips
1. **Selective Importing**
   ```python
   # Instead of
   import numpy as np
   
   # Use
   from numpy import array, mean
   ```

2. **Unloading Modules**
   ```python
   import sys
   if 'numpy' in sys.modules:
       del sys.modules['numpy']
   ```

3. **Using Context Managers**
   ```python
   from contextlib import contextmanager
   
   @contextmanager
   def import_temporarily(module_name):
       module = __import__(module_name)
       try:
           yield module
       finally:
           if module_name in sys.modules:
               del sys.modules[module_name]
   
   with import_temporarily('numpy') as np:
       # Use numpy here
       result = np.array([1, 2, 3])
   # numpy is unloaded here
   ```

## Troubleshooting

### Common Issues

1. **Module Not Found**
   - Check if the package is installed
   - Verify the package name is correct
   - Check for typos in the module name

2. **Memory Leaks**
   - Large modules can consume significant memory
   - Use `del` to remove references when done
   - Monitor memory usage with `psutil`

3. **Import Errors**
   - Check Python version compatibility
   - Verify package dependencies
   - Look for naming conflicts

### Debugging Tips

1. **Verbose Loading**
   ```python
   import load
   load.enable_auto_print()  # Shows loading information
   ```

2. **Module Inspection**
   ```python
   import sys
   print(sys.modules.keys())  # Show all loaded modules
   ```

3. **Memory Profiling**
   ```bash
   # Install memory_profiler
   pip install memory_profiler
   
   # Create test_script.py
   from memory_profiler import profile
   
   @profile
   def test():
       import numpy as np
       return np.random.rand(1000, 1000)
   
   if __name__ == '__main__':
       test()
   
   # Run with memory profiler
   python -m memory_profiler test_script.py
   ```

## Conclusion

The Load module provides a powerful and flexible way to handle Python imports with intelligent memory management. By understanding its internals, you can optimize your application's performance and resource usage.
