# 🎯 Using the @load Decorator

The `@load` decorator provides a powerful way to manage dependencies at the function level, ensuring all required packages are available before execution. This is particularly useful for:

- Making scripts more portable
- Simplifying dependency management
- Creating self-documenting functions with clear requirements
- Lazy-loading heavy dependencies

## 📦 Installation

First, ensure you have the latest version of `pyfunc-load` installed:

```bash
pip install -U pyfunc-load
```

## 🚀 Basic Usage

```python
from load import load_decorator as load

@load('numpy', 'pandas')
def analyze_data():
    """Analyze data using numpy and pandas.
    
    Dependencies:
    - numpy
    - pandas
    """
    # These imports are guaranteed to work
    import numpy as np
    import pandas as pd
    
    data = np.random.rand(10, 3)
    df = pd.DataFrame(data, columns=['A', 'B', 'C'])
    return df.describe()
```

## 🔄 Using Aliases

You can specify custom aliases for cleaner code:

```python
@load('np=numpy', 'pd=pandas', 'plt=matplotlib.pyplot')
def create_plot():
    """Create a simple sine wave plot.
    
    Dependencies:
    - numpy as np
    - pandas as pd
    - matplotlib.pyplot as plt
    """
    # Aliases are available in the function scope
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    
    plt.figure(figsize=(8, 6))
    plt.plot(x, y)
    plt.title('Sine Wave')
    plt.grid(True)
    plt.show()
    
    # Return the figure data
    return {'x': x.tolist(), 'y': y.tolist()}
```

### Dictionary-style Aliases

For more complex scenarios, use a dictionary for aliases:

```python
@load('numpy', 'pandas', alias={'pandas': 'pd', 'matplotlib.pyplot': 'plt'})
def analyze():
    import numpy as np  # No alias specified, use regular import
    import pandas as pd
    
    print(f"Using pandas version: {pd.__version__}")
    # ...
```

## 🔕 Silencing Import Messages

Control verbosity with these options:

```python
# Completely silent imports
@load('numpy', 'pandas', silent=True)
def silent_imports():
    import numpy as np
    print("No import messages will be shown")

# Only show errors
@load('numpy', 'pandas', verbose=False)
def quiet_imports():
    import numpy as np
    print("Only error messages will be shown")
```

## 🔄 Force Reinstallation

Force reinstallation of packages if needed:

```python
@load('numpy>=1.21.0', force=True)
def requires_specific_version():
    import numpy as np
    print(f"Using numpy version: {np.__version__}")
```

## 🎯 Lazy Loading

Delay imports until function execution:

```python
@load('numpy', 'pandas', lazy=True)
def lazy_loaded():
    # Modules are only imported when this function is called
    import numpy as np
    return np.array([1, 2, 3])
```

## 📊 Cache Management

Inspect and manage the module cache:

```python
import load

# Get cache information
cache_info = load.info()
print(f"Cached modules: {cache_info['cached_modules']}")

# Clear the cache
load.clear_cache()

# Check if a module is cached
if 'numpy' in load.info()['cached_modules']:
    print("NumPy is cached")
```

### Cache Statistics

```python
stats = load.cache_stats()
print(f"Hits: {stats['hits']}, Misses: {stats['misses']}")
print(f"Current size: {stats['size']}, Max size: {stats['max_size']}")
```

## 🌐 Web Scraping Example

```python
@load('requests', 'bs4.BeautifulSoup', 'pandas')
def scrape_website(url):
    """Scrape data from a website.
    
    Args:
        url (str): Website URL to scrape
        
    Returns:
        pandas.DataFrame: Extracted data
    """
    import requests
    from bs4 import BeautifulSoup
    import pandas as pd
    
    # Fetch the webpage
    response = requests.get(url)
    response.raise_for_status()
    
    # Parse HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract data (example: find all article titles)
    articles = []
    for article in soup.find_all('article'):
        title = article.find('h2').text.strip()
        link = article.find('a')['href']
        articles.append({'title': title, 'link': link})
    
    return pd.DataFrame(articles)
```

## 🔄 Chaining Decorators

You can chain `@load` with other decorators:

```python
import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} executed in {time.time() - start:.2f}s")
        return result
    return wrapper

@timer
@load('numpy', 'time')
def process_data():
    import numpy as np
    import time
    
    # Simulate processing
    time.sleep(1)
    return np.random.rand(1000, 1000).mean()
```

## 🛡️ Error Handling

Handle import errors gracefully:

```python
@load('nonexistent_package', 'numpy', on_error='warn')
def handle_errors():
    try:
        import numpy as np
        return np.array([1, 2, 3])
    except ImportError as e:
        print(f"Warning: {e}")
        return None
```

## 🏗️ Class Methods

Use with class methods:

```python
class DataAnalyzer:
    @classmethod
    @load('pandas', 'numpy')
    def analyze(cls, data):
        import pandas as pd
        import numpy as np
        # Analysis code here
        pass
```

## 🧪 Testing

Test functions with mocked dependencies:

```python
import pytest
from unittest.mock import MagicMock

def test_analysis():
    # Mock the dependencies
    mock_np = MagicMock()
    mock_np.array.return_value = [1, 2, 3]
    
    # Patch the imports
    with patch.dict('sys.modules', {'numpy': mock_np}):
        result = analyze_data()
        assert len(result) == 3
```

## 🏆 Best Practices

1. **Explicit Dependencies**
   - List all required packages in the decorator
   - Specify version constraints when needed (e.g., `'numpy>=1.21.0'`)
   - Document non-Python dependencies in your project's requirements

2. **Consistent Aliasing**
   - Use standard aliases (e.g., `np` for numpy, `pd` for pandas)
   - Document any non-standard aliases in function docstrings

3. **Performance Considerations**
   - Use `lazy=True` for rarely used heavy dependencies
   - Be mindful of cache size in long-running applications
   - Clear cache when memory usage is a concern

4. **Error Handling**
   - Use `on_error` parameter to control behavior on import failures
   - Provide meaningful error messages for missing dependencies
   - Consider fallback implementations when possible

5. **Documentation**
   - Document all dependencies in function docstrings
   - Include example usage with common parameter values
   - Note any platform-specific requirements

## 📚 See Also

- [API Reference](api.md) - Complete API documentation
- [Examples](examples.md) - More usage examples
- [Auto-Print](autoprint.md) - Automatic output display
- [Features](features.md) - Overview of all features

## 🚀 Advanced Usage

### Custom Import Hooks

You can extend the import system with custom hooks:

```python
def custom_importer(name, **kwargs):
    if name == 'my_package':
        # Custom import logic
        return __import__('my_custom_package')
    raise ImportError(f"Can't import {name}")

@load('my_package', importer=custom_importer)
def use_custom_package():
    import my_package  # Will use custom_importer
    return my_package.do_something()
```

### Dynamic Dependencies

For dynamic dependency resolution:

```python
def get_dependencies():
    # Determine dependencies at runtime
    if some_condition:
        return ['pandas', 'numpy']
    return ['csv']

@load(*get_dependencies())
def dynamic_imports():
    # Will use either pandas+numpy or csv based on condition
    pass
```

### Environment-Specific Imports

```python
import os

@load(
    'pandas' if os.getenv('USE_PANDAS') else 'csv',
    'numpy' if os.getenv('USE_NUMPY') else None
)
def conditional_imports():
    # Imports change based on environment variables
    pass
```

## Notes

- The decorator only loads the modules when the decorated function is called, not at import time
- Modules are cached, so subsequent calls to the same function won't reload them
- The decorator works with both the standard library and third-party packages
- For production code, consider adding error handling for missing dependencies
