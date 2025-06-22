import os
import sys

# Add the src directory to the Python path
project_root = os.path.abspath(os.path.dirname(__file__))
src_dir = os.path.join(project_root, '..', 'src')
if src_dir not in sys.path:
    sys.path.insert(0, src_dir)

try:
    from load import load, enable_auto_print, disable_auto_print, set_print_limit, smart_print
    print("✅ Successfully imported load module")
except ImportError as e:
    print(f"❌ Failed to import load module: {e}")
    sys.exit(1)

def create_plot():
    # Load the required modules
    np = load('numpy')
    pd = load('pandas')
    plt = load('matplotlib.pyplot')
    
    # Use the loaded modules
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    
    plt.figure(figsize=(8, 6))
    plt.plot(x, y)
    plt.title('Sine Wave')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    create_plot()
