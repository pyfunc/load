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

import load  # noqa: E402

# Constants
DEFAULT_PRINT_LIMIT = 50  # Default number of items to show in truncated output


def auto_print_examples() -> None:
    """Demonstrate auto-print functionality with various modules.

    This function shows how to enable/disable auto-printing and demonstrates
    the effect on module loading and printing behavior.
    """
    print("📊 Load Auto-Print Examples")
    print("=" * 50)

    # Enable auto-print
    load.enable_auto_print()

    # This should auto-print module info
    print("\n📦 Loading with auto-print enabled:")
    # Import the module - this will auto-print
    import json as _json  # noqa: F401
    version = _json.__version__ if hasattr(_json, '__version__') else 'unknown'
    print(f"✅ JSON module loaded (version: {version})")

    # Change print limit
    print("\n📏 Changing print limit:")
    load.set_print_limit(DEFAULT_PRINT_LIMIT)

    # Import another module - this will auto-print
    import os as _os  # noqa: F401
    print(f"✅ OS module loaded (cwd: {_os.getcwd()})")

    # Disable auto-print
    print("\n🔇 Disabling auto-print:")
    load.disable_auto_print()

    # This should be silent - we just want to test the import
    import sys as _  # noqa: F401, F841
    print("✅ Silent loading completed")

    # Re-enable for final test
    print("\n🔊 Re-enabling auto-print:")
    load.enable_auto_print()

    # Final test - import time module (should auto-print)
    import time as _time  # noqa: F401
    print(f"✅ Time module loaded (current time: {_time.ctime()})")

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
    print("\n🧪 Testing cache info...")

    # Import several modules (won't auto-print due to silent=True)
    modules = ["json", "os", "sys", "time", "math"]
    for module_name in modules:
        try:
            __import__(module_name)
        except ImportError:
            print(f"Warning: Failed to load {module_name}")

    # Get cache info
    cache_info = load.info()

    print("📊 Cache Statistics:")
    print(f"   Total cached modules: {cache_info['cache_size']}")
    print(f"   Auto-print enabled: {cache_info['auto_print']}")
    print(f"   Print limit: {cache_info['print_limit']}")
    cached = ", ".join(cache_info['cached_modules'])
    print(f"   Cached modules: {cached}")

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
    import json as json_lib
    data = {"sales": [100, 200, 150], "months": ["Jan", "Feb", "Mar"]}
    json_str = json_lib.dumps(data)
    print(f"   JSON data: {json_str[:50]}...")

    print("\n2️⃣  File operations simulation:")
    import os as os_lib
    current_path = os_lib.getcwd()
    print(f"   Current directory: {Path(current_path).name}")

    print("\n3️⃣  System information:")
    import sys as _  # noqa: F401, F841
    version = f"{_.version_info.major}.{_.version_info.minor}"
    print(f"   Python version: {version}")
    print(f"   Platform: {_.platform}")

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
