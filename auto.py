#!/usr/bin/env python3
"""Simple test script for the load module's dynamic imports."""

import os
import sys

# Add the src directory to the Python path
project_root = os.path.abspath(os.path.dirname(__file__))
src_dir = os.path.join(project_root, 'src')
if src_dir not in sys.path:
    sys.path.insert(0, src_dir)

print("Python path:", sys.path)
print("Current working directory:", os.getcwd())

# Import the load module
print("\nImporting load module...")
try:
    import load
    print(f"✅ Load module imported from: {os.path.dirname(load.__file__)}")
    
    # Import all from load
    print("\nImporting all from load...")
    from load import *
    
    # Test if requests is available
    print("\nTesting if 'requests' is available:")
    if 'requests' in globals():
        print("✅ 'requests' is in globals()")
        print(f"Type of 'requests': {type(requests).__name__}")
        
        # Test making a request
        print("\nTesting requests.get('https://api.github.com'):")
        try:
            response = requests.get('https://api.github.com')
            print(f"✅ Success! Status code: {response.status_code}")
        except Exception as e:
            print(f"❌ Error making request: {e}")
    else:
        print("❌ 'requests' is not in globals()")
        print("Available globals:", sorted([k for k in globals().keys() if not k.startswith('_')]))
    
except ImportError as e:
    print(f"❌ Failed to import load: {e}")
    sys.exit(1)

except Exception as e:
    print(f"❌ Unexpected error: {e}")
    raise
