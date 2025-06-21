#!/usr/bin/env python3
"""
Example script demonstrating proper usage of the load module.

This shows both the recommended usage pattern and workarounds for the
star-import limitation with dynamic modules.
"""

import os
import sys

# Add the src directory to the Python path
project_root = os.path.abspath(os.path.dirname(__file__))
src_dir = os.path.join(project_root, 'src')
if src_dir not in sys.path:
    sys.path.insert(0, src_dir)
    print(f"✅ Added {src_dir} to Python path")

def print_section(title):
    """Print a section header."""
    print(f"\n{'='*80}\n{title}\n{'='*80}")

print_section("Load Module Example Script")
print("This script demonstrates various ways to use the load module.")
print("Note: Some examples may be skipped if optional dependencies are not installed.")

# Import the load module functions
try:
    from load import import_aliases, enable_auto_print, set_print_limit, load
    print("✅ Successfully imported load module functions")
except ImportError as e:
    print(f"❌ Failed to import load module: {e}")
    sys.exit(1)

# Enable auto-print for demonstration
print("\n🔧 Enabling auto-print and setting print limit to 100 characters")
enable_auto_print()
set_print_limit(100)

# Method 1: Using the import_aliases helper function
print_section("Method 1: Using import_aliases")
print("This method imports multiple modules at once with optional aliases.")

try:
    # Try to import common data science modules
    np, pd, plt, requests = import_aliases(
        'numpy', 'pandas', 'plt=matplotlib.pyplot', 'requests'
    )
    print("✅ Successfully imported modules using import_aliases")
except ImportError as e:
    print(f"⚠️  Could not import all modules: {e}")
    print("Some examples will be skipped.")
    # Set default values to prevent NameError
    np = pd = plt = requests = None

# Now you can use these modules directly
if np is not None:
    try:
        print(f"📊 Using NumPy {np.__version__}")
        print(f"Random array: {np.random.rand(3, 3)}")
    except Exception as e:
        print(f"❌ Error using NumPy: {e}")
else:
    print("ℹ️  NumPy not available, skipping NumPy example")

# Test requests if available
if requests is not None:
    print("\n🌐 Testing requests module:")
    try:
        response = requests.get('https://api.github.com', timeout=5)
        print(f"✅ GitHub API status: {response.status_code}")
    except Exception as e:
        print(f"❌ Error making request: {e}")
else:
    print("\nℹ️  Requests not available, skipping HTTP request example")

# Demonstrate using the plotting modules if available
if pd is not None and plt is not None:
    print("\n📈 Testing pandas and matplotlib integration:")
    try:
        # Create a simple DataFrame
        df = pd.DataFrame({
            'x': range(5),  # Smaller range for demo
            'y': [i**2 for i in range(5)]
        })
        print("Created DataFrame:")
        print(df)
        
        # Create a simple plot
        plt.figure(figsize=(6, 3))  # Smaller figure for demo
        plt.plot(df['x'], df['y'], 'b-o')
        plt.title('Simple Plot')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.grid(True)
        
        # Save the plot to a file instead of showing it
        plot_file = 'example_plot.png'
        plt.savefig(plot_file)
        print(f"✅ Plot saved to {plot_file}")
    except Exception as e:
        print(f"❌ Error with pandas/matplotlib: {e}")
else:
    print("\nℹ️  pandas or matplotlib not available, skipping plotting example")

# Method 2: Using the load function directly for more control
print_section("Method 2: Using the load function")
print("This method shows how to load and use individual modules.")

try:
    # Load the json module (should always be available in stdlib)
    json = load('json')
    print(f"✅ Successfully loaded json module")
    
    # Example of using the loaded module
    data = {'name': 'Example', 'value': 42, 'active': True}
    json_str = json.dumps(data, indent=2)
    print(f"JSON example:\n{json_str}")
except Exception as e:
    print(f"❌ Error with json module: {e}")

# Method 3: Dynamic loading of system modules
print_section("Method 3: Dynamic system information")
print("This method demonstrates loading and using standard library modules.")

for name in ['os', 'sys', 'time']:
    try:
        module = load(name)
        if name == 'os':
            print(f"📂 Current working directory: {module.getcwd()}")
        elif name == 'sys':
            print(f"🐍 Python version: {module.version.split()[0]}")
            print(f"📦 Python path: {sys.path[:2]}...")
        elif name == 'time':
            print(f"⏰ Current time: {module.ctime()}")
    except Exception as e:
        print(f"⚠️  Could not load {name}: {e}")

print_section("Script Complete")
print("✅ Example script completed successfully!")
print("\n💡 Tip: Install optional dependencies to see all examples:")
print("pip install numpy pandas matplotlib requests")
