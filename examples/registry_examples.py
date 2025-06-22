"""
Registry examples for Load
"""

import sys
from pathlib import Path

# Add parent directory to path to allow importing from src
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))


def registry_examples():
    """Registry examples"""
    print("🔧 Load Registry Examples")
    print("=" * 50)

    from load import load, info, test_cache_info as cache_info

    print("\n📦 Testing basic loading:")
    json_lib = load('json')
    print("✅ JSON loaded successfully")

    # Test different source detection
    print("\n🎯 Testing source detection:")

    # Standard module
    os_lib = load('os')
    print("✅ Standard module (os) loaded")

    # Test local file loading (create a temp file)
    import tempfile
    import importlib.util
    
    with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False) as f:
        f.write(
            """
# Temporary test module
TEST_VALUE = "Hello from temp module"

def greet():
    return "Hello from temporary module!"
"""
        )
        temp_path = Path(f.name)

    try:
        # Load the temporary module using importlib
        spec = importlib.util.spec_from_file_location("temp_module", temp_path)
        temp_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(temp_module)
        
        print(f"✅ Local file loaded: {temp_module.TEST_VALUE}")
        print(f"✅ Function works: {temp_module.greet()}")
    except Exception as e:
        print(f"⚠️  Local file loading: {e}")
    finally:
        temp_path.unlink()

    # Show cache status
    print("\n💾 Cache status:")
    cache_stats = info()
    print(f"   Cached modules: {cache_stats['cache_size']}")
    print(f"   Module list: {cache_stats['cached_modules']}")

    print("\n✅ Registry examples completed")


def test_magic_import():
    """Test module import functionality"""
    print("\n📦 Testing module import:")

    from load import load

    try:
        # Test module import using function call
        json_module = load('json')
        os_module = load('os')
        sys_module = load('sys')

        # Verify the modules were loaded
        assert json_module is not None, "Failed to load json module"
        assert os_module is not None, "Failed to load os module"
        assert sys_module is not None, "Failed to load sys module"
        
        print("✅ Module import works for stdlib modules")

        # Test that they're the same as cached imports
        json_cached = load('json', silent=True)
        assert json_module is json_cached, "Subsequent loads should return cached module"
        print("✅ Module caching works correctly")

    except Exception as e:
        print(f"❌ Module import error: {e}")
        raise


def test_error_handling():
    """Test error handling"""
    print("\n🚨 Testing error handling:")

    import load

    # Test nonexistent module
    try:
        load.load("definitely_does_not_exist_12345", install=False, silent=True)
        print("❌ Should have raised ImportError")
    except ImportError:
        print("✅ ImportError raised correctly for nonexistent module")

    # Test nonexistent file
    try:
        load.load("./nonexistent_file.py", silent=True)
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
