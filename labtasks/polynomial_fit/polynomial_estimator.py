import pandas as pd
import matplotlib.pyplot as plt

# Clean CSV

# df = pd.read_csv("labtasks/polynomial_fit/real-commodity-price-index-metals.csv")

# # Columns not needed
# columns_not_needed = [
#     "Entity", "Code", "Iron ore", "Bauxite", "Tin", "Zinc", "Steel",
#     "Manganese", "Aluminum", "Chromium", "Copper", "Nickel"
# ]

# # Drop unnecessary columns
# df.drop(columns=columns_not_needed, axis=1, inplace=True)

# # Drop rows where Year is less than 1920
# df = df[df["Year"] >= 1920]

# # Save the filtered DataFrame
# df.to_csv('labtasks/polynomial_fit/lead_information_100_years.csv', index=False)

df = pd.read_csv('labtasks/polynomial_fit/lead_information_100_years.csv')

plt.figure(figsize=(12, 6))

plt.plot(df['Year'], df['Lead'])

plt.xlabel('Year')
plt.ylabel('Lead Prices')
plt.title('Lead Prices Over 100 Years')

plt.xticks(rotation=45)
plt.tight_layout()  # Automatically adjust subplot parameters for better fit
plt.show()