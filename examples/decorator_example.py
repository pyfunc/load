"""
Example demonstrating the @load decorator for function-level dependency management.

This example shows how to use the @load decorator to automatically handle
dependencies for specific functions.
"""

import sys
from pathlib import Path

# Add parent directory to path to allow importing from src
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

# Import the decorator (aliased to 'load' for convenience)
from load import load_decorator, load, enable_auto_print, disable_auto_print, set_print_limit, smart_print, info

# Example 1: Basic usage with numpy and pandas
@load_decorator('numpy', 'pandas', silent=True)
def analyze_data():
    """Example function that uses numpy and pandas.
    
    The @load decorator ensures these packages are available before execution.
    """
    np = load('numpy')
    pd = load('pandas')
    
    print("🔍 Analyzing data with numpy and pandas...")
    data = np.random.rand(5, 3)
    df = pd.DataFrame(data, columns=['A', 'B', 'C'])
    print("📊 Random DataFrame:")
    print(df)
    print("\n📈 Basic Statistics:")
    print(df.describe())
    return df

# Example 2: Using aliases for cleaner code
@load_decorator('numpy', 'matplotlib', silent=True)
def plot_sine_wave():
    """Example function that uses numpy and matplotlib with aliases."""
    # Use a non-interactive backend to avoid GUI issues
    import matplotlib
    matplotlib.use('Agg')  # Use the 'Agg' backend which doesn't require a display
    import numpy as np
    import matplotlib.pyplot as plt
    
    print("📈 Plotting a sine wave...")
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    
    plt.figure(figsize=(8, 4))
    plt.plot(x, y, 'b-', linewidth=2)
    plt.title('Sine Wave Example')
    plt.xlabel('x')
    plt.ylabel('sin(x)')
    plt.grid(True)
    plt.savefig('sine_wave.png')
    print("✅ Plot saved as 'sine_wave.png'")

# Example 3: Using multiple dependencies with silent mode
@load_decorator('requests', 'json', silent=True)
def fetch_data(url):
    """Example function that fetches and processes JSON data."""
    requests = load('requests')
    json = load('json')
    print(f"🌐 Fetching data from {url}...")
    response = requests.get(url)
    data = response.json()
    print(f"📥 Retrieved {len(data)} items")
    return data

if __name__ == "__main__":
    print("🚀 Starting decorator examples...\n")
    
    # Example 1: Basic usage
    print("=== Example 1: Basic Usage ===")
    df = analyze_data()
    
    # Example 2: Using aliases
    print("\n=== Example 2: Using Aliases ===")
    plot_sine_wave()
    
    # Example 3: Fetching data
    print("\n=== Example 3: Fetching Data ===")
    try:
        data = fetch_data('https://jsonplaceholder.typicode.com/todos/1')
        print(f"📝 Todo item: {data['title']} (ID: {data['id']})")
    except Exception as e:
        print(f"❌ Error fetching data: {e}")
    
    print("\n✅ All examples completed!")
