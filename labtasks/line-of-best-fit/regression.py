import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def generate_synthetic_data(m=2.5, b=1.0, num_points=100, x_range=(0, 10), noise_std=2.0, filename="synthetic_data.csv"):
    # Generate num_points equally spaced x values within the specified x_range
    x_values = np.linspace(x_range[0], x_range[1], num_points)
    
    # Calculate the corresponding y values using the linear equation y = mx + b
    y_values = m * x_values + b
    
    # Add Gaussian noise to the y values
    noise = np.random.normal(loc=0.0, scale=noise_std, size=num_points)
    y_values_noisy = y_values + noise
    
    # Create a DataFrame for easy CSV export
    data = pd.DataFrame({'x': x_values, 'y': y_values_noisy})
    data.to_csv(filename, index=False)
    
    return x_values, y_values_noisy, m, b


def create_graph(filename="synthetic_data.csv", m=2.5, b=1.0):
    # Read the data from the CSV file
    df = pd.read_csv(filename)
    
    # Extract x and y values from the DataFrame
    x_values = df['x']
    y_values = df['y']
    
    # Plot the data
    plt.scatter(x_values, y_values, label='Synthetic Data', color='blue')
    plt.plot(x_values, x_values * m + b, label='Line of Best Fit', color='red')
    
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Synthetic Data Plot')
    plt.legend()
    plt.show()

# Example usage
x_values, y_values_noisy, m, b = generate_synthetic_data()
create_graph()
    