"""
Basic usage examples for Load
"""

import sys
from pathlib import Path
import types

# Add src to path for development
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))


def basic_examples():
    """Basic Load examples"""
    print("🔥 Load Basic Examples")
    print("=" * 50)

    from load import load, enable_auto_print, disable_auto_print, set_print_limit, smart_print, test_cache_info

    # Load stdlib modules - these always work
    print("\n📚 Loading standard library modules:")
    json = load('json')
    print(f" json: {type(json).__name__}")
    print("✅ JSON loaded")
    
    os = load('os')
    print(f" os: {type(os).__name__}")
    print("✅ OS loaded")
    
    sys = load('sys')
    print(f" sys: {type(sys).__name__}")
    print("✅ SYS loaded")

    # Test basic functionality
    print(f"\n🧪 Testing functionality:")
    data = {"test": "data"}
    json_str = json.dumps(data)
    parsed = json.loads(json_str)
    print(f"✅ JSON dumps/loads: {parsed}")

    current_dir = os.getcwd()
    print(f"✅ OS getcwd: {current_dir}")

    python_version = sys.version_info
    print(f"✅ SYS version: {python_version.major}.{python_version.minor}")

    # Show cache info
    print(f"\n💾 Cache info:")
    cache_info()

    print(f"\n✅ Basic examples completed successfully!")


def test_auto_print():
    """Test auto-print functionality"""
    print("\n📊 Testing auto-print:")

    # Enable auto-print
    enable_auto_print()

    # This should auto-print
    time_lib = load('time', silent=False)

    # Disable auto-print
    disable_auto_print()

    # This should be silent
    math_lib = load('math', silent=False)

    print("✅ Auto-print test completed")


def test_aliases():
    """Test alias functionality"""
    print("\n🏷️  Testing aliases:")

    # Load modules
    try:
        operating_system = load('os')
        print("✅ Successfully loaded os module")
        
        time_module = load('time')
        print("✅ Successfully loaded time module")
    except Exception as e:
        print(f"❌ Error loading modules: {e}")

    print("✅ Alias loading completed")

    # Check cache
    load.test_cache_info()


if __name__ == "__main__":
    try:
        basic_examples()
        test_auto_print()
        test_aliases()
        print("\n🎉 All basic examples completed successfully!")
    except Exception as e:
        print(f"\n❌ Error in basic examples: {e}")
        sys.exit(1)
