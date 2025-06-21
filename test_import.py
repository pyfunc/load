#!/usr/bin/env python3

import sys
import os

print("Python sys.path:")
for p in sys.path:
    print(f"  - {p}")

print("\nCurrent working directory:", os.getcwd())
print("__file__:", __file__)
print("__name__:", __name__)
print("__package__:", __package__)

print("\nAttempting to import load...")
try:
    import load
    print("✅ Successfully imported load")
    print(f"load.__file__: {getattr(load, '__file__', 'not found')}")
    print(f"load.__package__: {getattr(load, '__package__', 'not found')}")
    print(f"load.__path__: {getattr(load, '__path__', 'not found')}")
    print(f"load.__spec__: {getattr(load, '__spec__', 'not found')}")
except ImportError as e:
    print(f"❌ Failed to import load: {e}")
    print("\nTrying to import from src...")
    try:
        sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))
        import load
        print("✅ Successfully imported load from src/")
    except ImportError as e:
        print(f"❌ Still failed to import load: {e}")
