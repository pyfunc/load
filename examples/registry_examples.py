"""
Registry examples for Load
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

def registry_examples():
    """Registry examples"""
    print("🔧 Load Registry Examples")
    print("=" * 50)

    import load

    # Test basic load functionality first
    print("\n📦 Testing basic loading:")
    json_lib = load.load('json', silent=True)
    print("✅ JSON loaded successfully")

    # Test different source detection
    print("\n🎯 Testing source detection:")

    # Standard module
    os_lib = load.load('os', silent=True)
    print("✅ Standard module (os) loaded")

    # Test local file loading (create a temp file)
    import tempfile
    with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
        f.write('''
# Temporary test module
TEST_VALUE = "Hello from temp module"

def greet():
    return "Hello from temporary module!"
''')
        temp_path = f.name

    try:
        temp_module = load.load(temp_path, silent=True)
        print(f"✅ Local file loaded: {temp_module.TEST_VALUE}")
        print(f"✅ Function works: {temp_module.greet()}")
    except Exception as e:
        print(f"⚠️  Local file loading: {e}")
    finally:
        Path(temp_path).unlink()

    # Show cache status
    print(f"\n💾 Cache status:")
    cache_info = load.info()
    print(f"   Cached modules: {cache_info['cache_size']}")
    print(f"   Module list: {cache_info['cached_modules']}")

    print("\n✅ Registry examples completed")

def test_magic_import():
    """Test magic import functionality"""
    print("\n🪄 Testing magic import:")

    import load

    try:
        # Test magic import
        json_via_magic = load.json
        os_via_magic = load.os
        sys_via_magic = load.sys

        print("✅ Magic import works for stdlib modules")

        # Test that they're the same as regular imports
        json_regular = load.load('json', silent=True)
        assert json_via_magic is json_regular, "Magic import should use same cache"
        print("✅ Magic import uses same cache")

    except Exception as e:
        print(f"❌ Magic import error: {e}")

def test_error_handling():
    """Test error handling"""
    print("\n🚨 Testing error handling:")

    import load

    # Test nonexistent module
    try:
        load.load('definitely_does_not_exist_12345', install=False, silent=True)
        print("❌ Should have raised ImportError")
    except ImportError:
        print("✅ ImportError raised correctly for nonexistent module")

    # Test nonexistent file
    try:
        load.load('./nonexistent_file.py', silent=True)
        print("❌ Should have raised ImportError")
    except ImportError:
        print("✅ ImportError raised correctly for nonexistent file")

if __name__ == "__main__":
    try:
        registry_examples()
        test_magic_import()
        test_error_handling()
        print("\n🎉 All registry examples completed successfully!")
    except Exception as e:
        print(f"\n❌ Error in registry examples: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)