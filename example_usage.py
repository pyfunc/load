#!/usr/bin/env python3
"""
Example script demonstrating proper usage of the load module.

This shows both the recommended usage pattern and workarounds for the 
star-import limitation with dynamic modules.
"""

# Method 1: Recommended approach - import specific functions and use load()
from load import load, enable_auto_print, set_print_limit

# Enable auto-print for demonstration
enable_auto_print()
set_print_limit(100)  # Show first 100 chars of output

# Load and use modules with explicit assignment
requests = load('requests')
print(f"Using requests {requests.__version__}")

# Make a request
response = requests.get('https://api.github.com')
print(f"GitHub API status: {response.status_code}")

# Method 2: For interactive use, you can use this pattern
# to get multiple modules at once
np, pd, plt = map(load, ['numpy', 'pandas', 'matplotlib.pyplot'])

# Now you can use these modules directly
if np:
    print(f"NumPy version: {np.__version__}")
    print(f"Random array: {np.random.rand(3, 3)}")
else:
    print("NumPy not available")

# Method 3: For scripts, you can create a local namespace
# with all the modules you need
class Modules:
    pass

# Create a namespace with all the modules
modules = Modules()
for name in ['os', 'sys', 'json', 'time']:
    try:
        setattr(modules, name, load(name))
    except ImportError:
        print(f"Warning: Could not load {name}")

# Now use them with the modules namespace
print(f"Current working directory: {modules.os.getcwd()}")
print(f"Python version: {modules.sys.version.split()[0]}")
print(f"Current time: {modules.time.ctime()}")

print("\nExample script completed successfully!")
