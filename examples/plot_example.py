"""
Example demonstrating plotting with the Load module.

This example shows how to use the Load module to load and use numpy and matplotlib
for creating and saving plots without requiring interactive display.
"""

import os
import sys
from pathlib import Path

# Add parent directory to path to allow importing from src
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

# Import the load function
from load import load

def create_plot():
    """Create and save a simple plot using numpy and matplotlib."""
    # Use a non-interactive backend to avoid GUI issues
    import matplotlib
    matplotlib.use('Agg')  # Use the 'Agg' backend which doesn't require a display
    
    # Load the required modules
    print("🔍 Loading required modules...")
    np = load('numpy')
    plt = load('matplotlib.pyplot')
    
    # Generate some data
    print("📊 Generating plot data...")
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    
    # Create the plot
    print("🎨 Creating plot...")
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, 'b-', linewidth=2, label='sin(x)')
    plt.title('Sine Wave Example', fontsize=14)
    plt.xlabel('X-axis', fontsize=12)
    plt.ylabel('Y-axis', fontsize=12)
    plt.legend()
    plt.grid(True)
    
    # Save the plot to a file
    output_file = 'sine_wave_plot.png'
    plt.savefig(output_file, bbox_inches='tight')
    print(f"✅ Plot saved as '{output_file}'")

if __name__ == "__main__":
    create_plot()
