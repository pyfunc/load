# 📝 Auto-Print Functionality

Load's auto-print feature provides automatic, intelligent display of loaded modules and objects, similar to Jupyter's rich output but working in any Python environment. This feature is particularly useful for interactive development and debugging.

## 🚀 Key Features

- Automatic display of module information on import
- Smart formatting for different data types
- Configurable output limits
- Works in any Python environment (not just Jupyter)
- Customizable display options

## Table of Contents
- [Overview](#overview)
- [Basic Usage](#basic-usage)
- [Configuration](#configuration)
- [Smart Printing](#smart-printing)
- [Customization](#customization)
- [Examples](#examples)
- [Advanced Usage](#advanced-usage)

## Overview

The auto-print functionality automatically displays information about loaded modules and objects, making it easier to work interactively. 
It's designed to be helpful without being intrusive.

## 🏁 Basic Usage

Auto-print is enabled by default. Here's how to use it:

```python
# Import Load (auto-print is enabled by default)
import load

# Standard imports with auto-print
numpy = load('numpy')  # Shows module information
pandas = load('pandas', alias='pd')  # With alias

# Standard imports also work
import json  # Will show module info if auto-print is enabled

# Load multiple modules
load('os', 'sys', 'math')  # Shows info for each module
```

## ⚙️ Configuration

Control the auto-print behavior with these functions:

```python
import load

# Check current auto-print status
print(f"Auto-print enabled: {load.info().get('auto_print', False)}")

# Enable auto-print with custom settings
load.enable_auto_print(limit=1500)  # Set character limit to 1500

# Disable auto-print
load.disable_auto_print()

# Change print limit without toggling
load.set_print_limit(2000)  # Increase to 2000 characters

# Get current print limit
current_limit = load.info().get('print_limit', 1000)
```

## 🧠 Smart Printing

The auto-print feature includes intelligent display for various types of objects:

| Object Type | Display Information | Example |
|-------------|---------------------|---------|
| **Modules** | Name, version, location | `✅ numpy v1.21.0` |
| **DataFrames** | Shape, columns, first 5 rows | `DataFrame[5x3]` |
| **NumPy Arrays** | Shape, dtype, sample values | `array[1000x1000] float64` |
| **HTTP Responses** | Status code, URL, headers | `200 OK https://api.example.com` |
| **Collections** | Length, first few items | `list[1000] [1, 2, 3, ...]` |
| **Custom Objects** | Available attributes | `CustomObject(attr1, method1, ...)` |

### Customizing Display

You can customize how objects are displayed by implementing the `__load_display__` method in your classes:

```python
class CustomData:
    def __init__(self, data):
        self.data = data
    
    def __load_display__(self):
        return f"CustomData with {len(self.data)} items"

# When loaded:
# ✅ CustomData with 42 items
```

## 🎨 Advanced Customization

### Context Manager for Temporary Changes

Use a context manager to temporarily modify auto-print settings:

```python
import load

with load.no_print():
    # Auto-print is disabled in this block
    import heavy_module  # No output
    
# Auto-print is automatically restored here
import another_module  # Will show output

# You can also use it to change settings temporarily
with load.print_settings(limit=500):
    # Temporary settings apply here
    pass
```

### Custom Print Handlers

Register custom handlers for specific types:

```python
import load

def custom_printer(obj, print_fn):
    if hasattr(obj, 'custom_display'):
        print_fn(f"✨ {obj.custom_display()}")
        return True
    return False

# Register the custom printer
load.register_printer(custom_printer)
```

### Environment Variables

Control auto-print behavior with environment variables:

```bash
# Disable auto-print by default
export LOAD_AUTO_PRINT=0

# Set default print limit
export LOAD_PRINT_LIMIT=2000
```

## 🚀 Examples

### Basic Interactive Usage

```python
import load

# Enable auto-print if not already enabled
load.enable_auto_print()

# Standard library imports

# DataFrames
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
# Prints: DataFrame: shape (3, 2)
#            A  B
#         0  1  4
#         1  2  5
#         2  3  6
```

### Working with Custom Objects

```python
class MyClass:
    def __init__(self):
        self.value = 42
        self.name = "Test"
        self.items = [1, 2, 3, 4, 5]

obj = MyClass()
# Prints: MyClass: MyClass with ['items', 'name', 'value']...
```

## Advanced Usage

### Integration with Jupyter

In Jupyter notebooks, the auto-print feature works alongside Jupyter's rich display system:

```python
# In Jupyter notebook
import load
import pandas as pd

# DataFrame will be displayed using Jupyter's rich display
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
```

### Customizing Output

You can extend the smart printing by modifying the `smart_print` function in `load/utils.py` to add support for additional types or customize the output format.

## Troubleshooting

### Disabling Auto-Print

If auto-print is causing issues:

```python
from load import disable_auto_print
disable_auto_print()
```

Or set the environment variable:
```bash
export LOAD_NO_AUTOPRINT=1
```

### Verbose Mode

For debugging, you can enable verbose mode:

```python
import os
os.environ['LOAD_DEBUG'] = '1'
import load
```

---

For more information, see the [main documentation](../README.md).
