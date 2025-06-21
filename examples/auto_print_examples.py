"""
Auto-print examples for Load

This module demonstrates the auto-print functionality of the Load module,
showing how to enable/disable auto-printing and demonstrating smart printing
of different Python objects.
"""

import sys
from pathlib import Path

# Add parent directory to path to allow importing from src
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

# Constants
DEFAULT_PRINT_LIMIT = 50  # Default number of items to show in truncated output


def auto_print_examples() -> None:
    """Demonstrate auto-print functionality with various modules.

    This function shows how to enable/disable auto-printing and demonstrates
    the effect on module loading and printing behavior.
    """
    print("📊 Load Auto-Print Examples")
    print("=" * 50)

    import load

    # Test auto-print controls
    print("\n🎛️  Testing auto-print controls:")

    # Enable auto-print
    load.enable_auto_print()

    # This should auto-print module info
    print("\n📦 Loading with auto-print enabled:")
    # Load and use the module to avoid unused variable warning
    json_lib = load.load("json")  # Should auto-print
    if json_lib is None:  # For type checking
        print("Warning: Failed to load json module")

    # Change print limit
    print("\n📏 Changing print limit:")
    load.set_print_limit(DEFAULT_PRINT_LIMIT)

    # Load another module and use it
    os_lib = load.load("os")  # Should auto-print with limit
    if os_lib is not None:  # For type checking and usage
        _ = os_lib.getcwd()  # Use the module to avoid unused variable warning

    # Disable auto-print
    print("\n🔇 Disabling auto-print:")
    load.disable_auto_print()

    # This should be silent
    sys_lib = load.load("sys")  # Should NOT auto-print
    assert sys_lib is not None, "Failed to load sys module"
    print("✅ Silent loading completed")

    # Re-enable for final test
    print("\n🔊 Re-enabling auto-print:")
    load.enable_auto_print()

    # Final test - use the module to avoid unused variable warning
    time_lib = load.load("time")  # Should auto-print again
    if time_lib is not None:  # For type checking
        _ = time_lib.time()  # Use the module

    print("\n✅ Auto-print examples completed")


def test_smart_print() -> None:
    """Test smart print functionality.

    Demonstrates how smart printing handles different types of objects
    including strings, lists, dictionaries, and modules.
    """
    print("\n🧠 Testing smart print:")

    from load.core import smart_print

    # Test different object types
    print("\n📝 Testing different object types:")

    # Basic types
    smart_print("Hello World", "string_test")
    smart_print([1, 2, 3, 4, 5], "list_test")
    smart_print({"key": "value", "number": 42}, "dict_test")

    # Long list
    long_list = list(range(20))
    smart_print(long_list, "long_list_test")

    # Module
    import json

    smart_print(json, "json_module")

    print("✅ Smart print tests completed")


def test_cache_info() -> None:
    """Test and display cache information.

    Shows how to retrieve and display information about the module cache,
    including the number of cached modules and cache statistics.
    """
    print("\n💾 Testing cache info:")

    import load

    # Load several modules and use them to avoid unused variable warnings
    modules = ["json", "os", "sys", "time", "math"]
    for module_name in modules:
        mod = load.load(module_name, silent=True)
        if mod is None:  # For type checking
            print(f"Warning: Failed to load {module_name}")

    # Get cache info
    cache_info = load.info()

    print("📊 Cache Statistics:")
    print(f"   Total cached modules: {cache_info['cache_size']}")
    print(f"   Auto-print enabled: {cache_info['auto_print']}")
    print(f"   Print limit: {cache_info['print_limit']}")
    print("   Cached modules: " + ", ".join(cache_info['cached_modules']))

    print("✅ Cache info test completed")


def demo_real_usage() -> None:
    """Demonstrate real-world usage scenarios for the Load module.

    Shows practical examples of using the Load module in common programming
    tasks such as JSON handling, file operations, and system information
    retrieval.
    """
    print("\n🌍 Real-world usage demo:")

    import load

    # Enable auto-print for demo
    load.enable_auto_print()

    print("\n1️⃣  Data analysis simulation:")
    # Simulate data analysis workflow
    json_lib = load.load("json")
    data = {"sales": [100, 200, 150], "months": ["Jan", "Feb", "Mar"]}
    json_str = json_lib.dumps(data)
    print(f"   JSON data: {json_str[:50]}...")

    print("\n2️⃣  File operations simulation:")
    os_lib = load.load("os")
    current_path = os_lib.getcwd()
    print(f"   Current directory: {Path(current_path).name}")

    print("\n3️⃣  System information:")
    sys_lib = load.load("sys")
    print(
        f"   Python version: {sys_lib.version_info.major}.{sys_lib.version_info.minor}"
    )
    print(f"   Platform: {sys_lib.platform}")

    print("\n✅ Real-world demo completed")


def main() -> int:
    """Run all example functions and return exit code."""
    try:
        print("🚀 Starting Load auto-print examples...")
        
        # Run all example functions
        auto_print_examples()
        test_smart_print()
        test_cache_info()
        demo_real_usage()
        
        print("\n🎉 All auto-print examples completed successfully!")
        return 0
        
    except ImportError as e:
        print(f"\n❌ Import error: {e}")
        print("Please make sure all required dependencies are installed.")
    except Exception as e:
        print(f"\n❌ Error in auto-print examples: {e}")
        import traceback
        traceback.print_exc()
    
    return 1


if __name__ == "__main__":
    sys.exit(main())
