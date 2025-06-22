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

from load import (
    load,
    enable_auto_print,
    disable_auto_print,
    set_print_limit,
    smart_print,
    info,
    PRINT_LIMIT
)

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
    enable_auto_print()

    # This should auto-print module info
    print("\n📦 Loading with auto-print enabled:")
    json_lib = load('json')
    version = json_lib.__version__ if hasattr(json_lib, "__version__") else "unknown"
    print(f"✅ JSON module loaded (version: {version})")

    # Change print limit
    print("\n📏 Changing print limit:")
    set_print_limit(50)  # Show only first 50 characters
    print(f"📏 Print limit: {PRINT_LIMIT} characters")

    # This should respect the new print limit
    os_lib = load('os')
    cwd = os_lib.getcwd()
    print(f"✅ OS module loaded (cwd: {cwd})")

    # Disable auto-print
    print("\n🔇 Disabling auto-print:")
    disable_auto_print()

    # This should not print anything
    load('time', silent=True)
    print("✅ Silent loading completed")

    # Re-enable auto-print
    print("\n🔊 Re-enabling auto-print:")
    enable_auto_print()

    # This should print again
    time_lib = load('time')
    current_time = time_lib.ctime()
    print(f"✅ Time module loaded (current time: {current_time})")

    print("\n✅ Auto-print examples completed")


def test_smart_print() -> None:
    """Test smart print functionality.

    Demonstrates how smart printing handles different types of objects
    including strings, lists, dictionaries, and modules.
    """
    print("\n🧠 Testing smart print:")

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
    cache_info = info()

    print("📊 Cache Statistics:")
    print(f"   Total cached modules: {cache_info['cache_size']}")
    print(f"   Auto-print enabled: {cache_info['auto_print']}")
    print(f"   Print limit: {cache_info['print_limit']}")
    cached = ", ".join(cache_info["cached_modules"])
    print(f"   Cached modules: {cached}")

    print("✅ Cache info test completed")


def demo_real_usage() -> None:
    """Demonstrate real-world usage scenarios for the Load module.

    Shows practical examples of using the Load module in common programming
    tasks such as JSON handling, file operations, and system information
    retrieval.
    """
    print("\n🌍 Real-world usage demo:")

    # Enable auto-print for demo
    enable_auto_print()

    print("\n1️⃣  Data analysis simulation:")
    # Simulate data analysis workflow
    json_lib = load('json')
    data = {"sales": [100, 200, 150], "months": ["Jan", "Feb", "Mar"]}
    json_str = json_lib.dumps(data)
    print(f"   JSON data: {json_str[:50]}...")

    print("\n2️⃣  File operations simulation:")
    os_lib = load('os')
    current_path = os_lib.getcwd()
    print(f"   Current directory: {Path(current_path).name}")

    print("\n3️⃣  System information:")
    sys_lib = load('sys')  # noqa: F401, F841

    version = f"{sys_lib.version_info.major}.{sys_lib.version_info.minor}"
    print(f"   Python version: {version}")
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
