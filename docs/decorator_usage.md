# Using the @load Decorator

The `@load` decorator provides a convenient way to ensure that required dependencies are loaded before a function executes. This is particularly useful for scripts where you want to manage dependencies at the function level.

## Basic Usage

```python
from load import load_decorator as load

@load('numpy', 'pandas')
def analyze_data():
    # numpy and pandas are guaranteed to be available here
    import numpy as np
    import pandas as pd
    
    data = np.random.rand(10, 3)
    df = pd.DataFrame(data, columns=['A', 'B', 'C'])
    return df.describe()
```

## Using Aliases

You can specify aliases for your imports:

```python
@load('np=numpy', 'pd=pandas', 'plt=matplotlib.pyplot')
def create_plot():
    # Use the aliases directly
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    
    plt.figure(figsize=(8, 6))
    plt.plot(x, y)
    plt.title('Sine Wave')
    plt.show()
```

## Silencing Import Messages

To suppress import messages, set `silent=True`:

```python
@load('numpy', 'pandas', silent=True)
def silent_imports():
    import numpy as np
    print("No import messages will be shown")
```

## Cache Inspection

You can inspect the module cache using `test_cache_info()`:

```python
from load import test_cache_info

test_cache_info()
```

This will display information about currently cached modules and cache settings.

## Real-world Example

Here's a more complete example showing how you might use the decorator in a data analysis script:

```python
from load import load_decorator as load

@load('np=numpy', 'pd=pandas', 'sns=seaborn', 'plt=matplotlib.pyplot')
def analyze_dataset(filepath):
    """Load and analyze a dataset."""
    # Load data
    df = pd.read_csv(filepath)
    
    # Basic statistics
    print("\n📊 Dataset Info:")
    print(df.info())
    
    print("\n📈 Basic Statistics:")
    print(df.describe())
    
    # Plot correlation matrix
    print("\n📊 Plotting correlation matrix...")
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
    plt.title('Feature Correlation')
    plt.show()
    
    return df

if __name__ == "__main__":
    # The required modules will be loaded when the function is called
    df = analyze_dataset("data.csv")
```

## Best Practices

1. **Be Explicit**: List all required dependencies in the decorator to make them visible
2. **Use Aliases**: Make your code more readable by using consistent aliases
3. **Group Related Imports**: Keep related imports together in the decorator
4. **Document Dependencies**: Consider adding a docstring that lists required packages

## Notes

- The decorator only loads the modules when the decorated function is called, not at import time
- Modules are cached, so subsequent calls to the same function won't reload them
- The decorator works with both the standard library and third-party packages
- For production code, consider adding error handling for missing dependencies
