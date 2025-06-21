"""
Basic usage examples for Load
"""

import sys
from pathlib import Path

# Add src to path for development
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

def basic_examples():
    """Basic Load examples"""
    print("🔥 Load Basic Examples")
    print("=" * 50)

    # Import Load
    import load

    # Load stdlib modules - these always work
    print("\n📚 Loading standard library modules:")
    json_lib = load.json
    print("✅ JSON loaded")

    os_lib = load.os
    print("✅ OS loaded")

    sys_lib = load.sys
    print("✅ SYS loaded")

    # Test basic functionality
    print(f"\n🧪 Testing functionality:")
    data = {"test": "data"}
    json_str = json_lib.dumps(data)
    parsed = json_lib.loads(json_str)
    print(f"✅ JSON dumps/loads: {parsed}")

    current_dir = os_lib.getcwd()
    print(f"✅ OS getcwd: {current_dir}")

    python_version = sys_lib.version_info
    print(f"✅ SYS version: {python_version.major}.{python_version.minor}")

    # Show cache info
    print(f"\n💾 Cache info:")
    cache_info = load.info()
    print(f"   Cached modules: {cache_info['cache_size']}")
    print(f"   Modules: {cache_info['cached_modules']}")

    print(f"\n✅ Basic examples completed successfully!")

def test_auto_print():
    """Test auto-print functionality"""
    print("\n📊 Testing auto-print:")

    import load

    # Enable auto-print
    load.enable_auto_print()

    # This should auto-print
    time_lib = load.load('time', silent=False)

    # Disable auto-print
    load.disable_auto_print()

    # This should be silent
    math_lib = load.load('math', silent=False)

    print("✅ Auto-print test completed")

def test_aliases():
    """Test alias functionality"""
    print("\n🏷️  Testing aliases:")

    import load

    # Load with alias
    operating_system = load.load('os', alias='operating_system', silent=True)
    time_module = load.load('time', alias='time_utils', silent=True)

    print("✅ Alias loading completed")

    # Check cache
    cache_info = load.info()
    print(f"   Aliases in cache: {[m for m in cache_info['cached_modules'] if '_' in m]}")

if __name__ == "__main__":
    try:
        basic_examples()
        test_auto_print()
        test_aliases()
        print("\n🎉 All basic examples completed successfully!")
    except Exception as e:
        print(f"\n❌ Error in basic examples: {e}")
        sys.exit(1)