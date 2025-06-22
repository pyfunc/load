# 📚 Comprehensive Examples

This document provides comprehensive examples of using the `load` module in various scenarios.

## Table of Contents
- [Basic Usage](#basic-usage)
- [Working with External Packages](#working-with-external-packages)
- [Local Module Imports](#local-module-imports)
- [Using the Decorator](#using-the-decorator)
- [Advanced Caching](#advanced-caching)
- [Error Handling](#error-handling)
- [Performance Optimization](#performance-optimization)

## Basic Usage

```python
# Basic module loading
import load

# Load standard library modules
json = load('json')
data = json.dumps({"key": "value"})

# Load with aliases
pd = load('pandas', alias='pd')
df = pd.DataFrame({'A': [1, 2, 3]})
```

## Working with External Packages

```python
# Install and load external packages if not available
plt = load('matplotlib.pyplot', alias='plt')
import numpy as np

# Create a simple plot
x = np.linspace(0, 10, 100)
plt.plot(x, np.sin(x))
plt.title('Sine Wave')
plt.show()
```

## Local Module Imports

```python
# Load a local module
config = load('./config/settings.py')

# Or from a package
utils = load('../utils/helpers')
```

## Using the Decorator

```python
from load import load_decorator as load

@load('numpy', 'pandas', 'matplotlib')
def analyze_data():
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    
    # Your analysis code here
    data = np.random.rand(10, 3)
    df = pd.DataFrame(data, columns=['A', 'B', 'C'])
    df.plot()
    plt.show()
```

## Advanced Caching

```python
import load

# Force reload a module
fresh_module = load('module_name', force=True)

# Check cache info
cache_info = load.info()
print(f"Cached modules: {cache_info['cached_modules']}")
```

## Error Handling

```python
try:
    # Try to load a non-existent module
    missing = load('nonexistent_package')
except ImportError as e:
    print(f"Failed to load module: {e}")
    
    # Install the package if needed
    if input("Install package? (y/n): ").lower() == 'y':
        load.install('nonexistent_package')
        missing = load('nonexistent_package')
```

## Performance Optimization

```python
# Disable auto-print for better performance in scripts
load.disable_auto_print()

# Load multiple modules at once
modules = load.many(['numpy', 'pandas', 'matplotlib'])
np, pd, plt = modules

# Enable auto-print for interactive use
load.enable_auto_print()
```

## Real-world Example: Data Analysis Pipeline

```python
@load('pandas', 'numpy', 'sklearn', 'matplotlib')
def analyze_dataset(filepath):
    import pandas as pd
    import numpy as np
    from sklearn.preprocessing import StandardScaler
    import matplotlib.pyplot as plt
    
    # Load data
    data = pd.read_csv(filepath)
    
    # Preprocess
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data.select_dtypes(include=[np.number]))
    
    # Plot
    plt.figure(figsize=(10, 6))
    plt.hist(scaled_data.flatten(), bins=50)
    plt.title('Distribution of Scaled Features')
    plt.show()
    
    return scaled_data
```

## Next Steps

- Explore more examples in the `examples/` directory
- Check out the [API Reference](api.md) for detailed documentation
- Read about [advanced features](features.md) for more use cases
