import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the filtered dataset
df = pd.read_csv('labtasks/polynomial_fit/lead_information_100_years.csv')

# Split the data for the first 90 years
df_first_90_years = df[df['Year'] < (df['Year'].min() + 90)]

# Separate the years and lead prices for training
X_train = df_first_90_years['Year'].values
y_train = df_first_90_years['Lead'].values

# Fit polynomial to the first 90 years data (order 1)
coefficients = np.polyfit(X_train, y_train, 1)
linear_model = np.poly1d(coefficients)

# Predict lead prices for the next 10 years (up to 2030)
years_extended = np.arange(df['Year'].max() + 1, 2031)
y_pred_extended = linear_model(years_extended)

# Plot the actual data
plt.figure(figsize=(12, 6))
plt.plot(X_train, y_train, color='blue', label='Train Data (First 90 years)')
plt.plot(df['Year'], df['Lead'], color='green', label='Complete Data (Up to 2020)')

# Plot the prediction
plt.plot(years_extended, y_pred_extended, color='red', label='Extended Prediction to 2030')

plt.xlabel('Year')
plt.ylabel('Lead Prices')
plt.title('Lead Prices Prediction to 2030')
plt.legend()
plt.show()
