#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Test script for Python 2.7 compatibility
"""
from __future__ import print_function, unicode_literals

import sys
import os

print("Python version:", sys.version)
print("Python executable:", sys.executable)

# Add the current directory to the path
sys.path.insert(0, os.path.abspath('.'))

try:
    # Test basic import
    print("\nTesting basic import...")
    import load
    print("Successfully imported load module")
    print("Load version:", load.__version__)
    
    # Test basic functionality
    print("\nTesting basic functionality...")
    math = load('math')
    print("Imported math module:", math)
    print("math.sqrt(16) =", math.sqrt(16))
    
    # Test auto-print
    print("\nTesting auto-print...")
    load.enable_auto_print()
    result = load('math.sqrt(25)')
    print("Result of load('math.sqrt(25)'):", result)
    
    print("\nPython 2.7 compatibility tests completed successfully!")
    
except Exception as e:
    print("\nError during testing:", str(e))
    import traceback
    traceback.print_exc()
    sys.exit(1)
