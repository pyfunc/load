"""
Utility functions for Load
"""

from .core import AUTO_PRINT, PRINT_LIMIT, PRINT_TYPES

def smart_print(obj, name=None):
    """Intelligent result printing"""
    if not AUTO_PRINT:
        return

    try:
        obj_name = name or getattr(obj, '__name__', type(obj).__name__)

        if hasattr(obj, 'status_code'):  # HTTP Response
            print(f"🌐 {obj_name}: {obj.status_code} - {obj.url}")
            if hasattr(obj, 'json'):
                try:
                    data = obj.json()
                    print(f"📄 JSON: {str(data)[:PRINT_LIMIT]}...")
                except:
                    print(f"📄 Text: {obj.text[:PRINT_LIMIT]}...")

        elif hasattr(obj, 'shape'):  # DataFrame/Array
            print(f"📊 {obj_name}: shape {obj.shape}")
            print(obj.head() if hasattr(obj, 'head') else str(obj)[:PRINT_LIMIT])

        elif hasattr(obj, '__len__') and len(obj) > 10:  # Long collections
            print(f"📋 {obj_name}: {len(obj)} items")
            print(f"First 5: {list(obj)[:5]}...")

        elif isinstance(obj, PRINT_TYPES):  # Basic types
            output = str(obj)
            if len(output) > PRINT_LIMIT:
                print(f"📝 {obj_name}: {output[:PRINT_LIMIT]}...")
            else:
                print(f"📝 {obj_name}: {output}")

        elif hasattr(obj, '__dict__'):  # Objects
            attrs = [attr for attr in dir(obj) if not attr.startswith('_')][:5]
            print(f"🔧 {obj_name}: {type(obj).__name__} with {attrs}...")

        else:
            print(f"✅ {obj_name}: {type(obj).__name__} loaded")

    except Exception as e:
        print(f"✅ {obj_name or 'Object'}: loaded ({type(obj).__name__})")
