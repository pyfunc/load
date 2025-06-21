# Auto-Print Functionality

Load's auto-print feature provides automatic, intelligent display of loaded modules and objects, similar to Jupyter's rich output but working in any Python environment.

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

## Basic Usage

Auto-print is enabled by default. When you import and use Load, it will automatically display information about loaded modules:

```python
# Import Load (auto-print is enabled by default)
import load

# Load modules - they will auto-print information
import numpy as np
import pandas as pd

# Load with aliases (also auto-printed)
np = load.np  # Same as import numpy as np
pd = load.pd  # Same as import pandas as pd
```

## Configuration

You can control the auto-print behavior with these functions:

```python
from load import enable_auto_print, disable_auto_print, set_print_limit

# Enable auto-print (enabled by default)
enable_auto_print()

# Disable auto-print
disable_auto_print()

# Set the maximum number of characters to print
set_print_limit(2000)  # Default is 1000
```

## Smart Printing

The auto-print feature includes intelligent display for various types of objects:

- **Modules**: Shows basic module information
- **DataFrames/Arrays**: Displays shape and preview
- **HTTP Responses**: Shows status code and URL
- **Collections**: Shows length and first few items
- **Custom Objects**: Displays available attributes

## Customization

### Print Limit

Control how much information is displayed:

```python
from load import set_print_limit

# Show more output
set_print_limit(5000)  # Increase to 5000 characters

# Show less output
set_print_limit(500)   # Decrease to 500 characters
```

### Selective Auto-Print

You can temporarily disable auto-print for specific imports:

```python
# Temporarily disable auto-print
from load import disable_auto_print, enable_auto_print

disable_auto_print()
import some_heavy_module  # Won't auto-print
enable_auto_print()
```

## Examples

### Basic Usage

```python
import load

# These will auto-print
import requests
import numpy as np
import pandas as pd

# HTTP requests
response = requests.get('https://api.github.com')
# Prints: Response 200 - https://api.github.com
#         JSON: {'current_user_url': 'https://api.github.com/user', ...}

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
