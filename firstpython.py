import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Generate synthetic housing data
np.random.seed(42)
n = 500

# Simulate features
house_size = np.random.normal(1500, 300, n)  # in square feet
num_rooms = np.random.randint(2, 6, size=n)
age = np.random.randint(0, 50, size=n)       # building age in years
region = np.random.choice(['East', 'West', 'Midwest', 'South'], size=n)
price = 50000 + house_size * 120 + num_rooms * 10000 - age * 500 + np.random.normal(0, 10000, n)

# Assemble DataFrame
housing_df = pd.DataFrame({
    'HouseSize_sqft': house_size,
    'NumRooms': num_rooms,
    'Age_years': age,
    'Region': region,
    'Price_USD': price
})

# Summary statistics
summary = housing_df.describe()

# Create a scatter plot
plt.figure(figsize=(8, 5))
sns.scatterplot(data=housing_df, x='HouseSize_sqft', y='Price_USD', hue='Region', alpha=0.7)
plt.title('Simulated Housing Prices by Size and Region')
plt.xlabel('House Size (sqft)')
plt.ylabel('Price (USD)')
plt.tight_layout()
plt.savefig("/mnt/data/housing_price_scatter.png")

# Save data and code as CSV and description
housing_df.to_csv("/Users/Username/Desktop/data/simulated_housing_data.csv", index=False)

summary.head()

