from src.load.load import load

@load_decorator('np=numpy', 'pd=pandas', 'plt=matplotlib.pyplot')
def create_plot():
    # Use the aliases directly
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
