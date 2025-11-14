import pandas as pd
import matplotlib.pyplot as plt

# Read cleaned CSV
df = pd.read_csv("labtasks/asset_prices/nvidia_clean_data.csv")

# Convert 'Date' to datetime format
df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y')

# Plot data with a suitable figure size
plt.figure(figsize=(12, 6))  # Adjust the figure size for clarity

plt.plot(df['Date'], df['CloseClean'])

# Set date ticks and format for x-axis
plt.gca().xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%B'))  # Format for month names
plt.gca().xaxis.set_major_locator(plt.matplotlib.dates.MonthLocator())  # Locator for months

plt.xlabel('Month')
plt.ylabel('Close Price ($)')
plt.title('NVIDIA Stock Price Over One Year')

plt.xticks(rotation=45)
plt.tight_layout()  # Automatically adjust subplot parameters for better fit
plt.show()