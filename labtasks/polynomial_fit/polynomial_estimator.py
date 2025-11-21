import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('labtasks/polynomial_fit/lead_information_100_years.csv')

# Split the data for the first 90 years and the last 10 years
df_first_90_years = df[df['Year'] < (df['Year'].min() + 90)]
df_last_10_years = df[df['Year'] >= (df['Year'].min() + 90)]

# Separate the years and lead prices for training and testing
X_train = df_first_90_years['Year'].values
y_train = df_first_90_years['Lead'].values
X_test = df_last_10_years['Year'].values
y_test = df_last_10_years['Lead'].values

# Try polynomial fits of different orders
orders = [1, 2, 3, 4, 5]
mse_values = []

plt.figure(figsize=(12, 8))

for order in orders:
    # Fit polynomial to the first 90 years
    coefficients = np.polyfit(X_train, y_train, order)
    polynomial = np.poly1d(coefficients)

    # Predict lead prices for the last 10 years
    y_pred = polynomial(X_test)

    # Calculate mean squared error for the predictions
    mse = np.mean((y_test - y_pred)**2)
    mse_values.append(mse)

    # Plot the polynomial fit
    plt.plot(X_test, y_pred, label=f'Order {order}: MSE = {mse:.2f}')

# Plot the actual data
plt.scatter(X_train, y_train, color='blue', label='Train Data (First 90 years)')
plt.scatter(X_test, y_test, color='green', label='Test Data (Last 10 years)')

plt.xlabel('Year')
plt.ylabel('Lead Prices')
plt.title('Polynomial Fit to Lead Prices')
plt.legend()
plt.show()

# Print MSE values for comparison
for order, mse in zip(orders, mse_values):
    print(f"Polynomial Order {order}: MSE = {mse:.2f}")