"""
Auto-print examples for Load
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))


def auto_print_examples():
    """Auto-print examples"""
    print("📊 Load Auto-Print Examples")
    print("=" * 50)

    import load

    # Test auto-print controls
    print("\n🎛️  Testing auto-print controls:")

    # Enable auto-print
    load.enable_auto_print()

    # This should auto-print module info
    print("\n📦 Loading with auto-print enabled:")
    json_lib = load.load("json")  # Should auto-print

    # Change print limit
    print("\n📏 Changing print limit:")
    load.set_print_limit(50)

    # Load another module
    os_lib = load.load("os")  # Should auto-print with limit

    # Disable auto-print
    print("\n🔇 Disabling auto-print:")
    load.disable_auto_print()

    # This should be silent
    sys_lib = load.load("sys")  # Should NOT auto-print
    print("✅ Silent loading completed")

    # Re-enable for final test
    print("\n🔊 Re-enabling auto-print:")
    load.enable_auto_print()

    # Final test
    time_lib = load.load("time")  # Should auto-print again

    print("\n✅ Auto-print examples completed")


def test_smart_print():
    """Test smart print functionality"""
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


def test_cache_info():
    """Test cache information display"""
    print("\n💾 Testing cache info:")

    import load

    # Load several modules
    modules = ["json", "os", "sys", "time", "math"]
    for module_name in modules:
        load.load(module_name, silent=True)

    # Get cache info
    cache_info = load.info()

    print(f"\n📊 Cache Statistics:")
    print(f"   Total cached modules: {cache_info['cache_size']}")
    print(f"   Auto-print enabled: {cache_info['auto_print']}")
    print(f"   Print limit: {cache_info['print_limit']}")
    print(f"   Cached modules: {', '.join(cache_info['cached_modules'])}")

    print("✅ Cache info test completed")


def demo_real_usage():
    """Demo real-world usage scenarios"""
    print("\n🌍 Real-world usage demo:")

    import load

    # Enable auto-print for demo
    load.enable_auto_print()

    print("\n1️⃣  Data analysis simulation:")
    # Simulate data analysis workflow
    json_lib = load.json
    data = {"sales": [100, 200, 150], "months": ["Jan", "Feb", "Mar"]}
    json_str = json_lib.dumps(data)
    print(f"   JSON data: {json_str[:50]}...")

    print("\n2️⃣  File operations simulation:")
    os_lib = load.os
    current_path = os_lib.getcwd()
    print(f"   Current directory: {Path(current_path).name}")

    print("\n3️⃣  System information:")
    sys_lib = load.sys
    print(
        f"   Python version: {sys_lib.version_info.major}.{sys_lib.version_info.minor}"
    )
    print(f"   Platform: {sys_lib.platform}")

    print("\n✅ Real-world demo completed")


if __name__ == "__main__":
    try:
        auto_print_examples()
        test_smart_print()
        test_cache_info()
        demo_real_usage()
        print("\n🎉 All auto-print examples completed successfully!")
    except Exception as e:
        print(f"\n❌ Error in auto-print examples: {e}")
        import traceback

        traceback.print_exc()
        sys.exit(1)
