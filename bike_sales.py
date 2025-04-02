import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data
file_path = "bike_sales_india.csv"
df = pd.read_csv(file_path)

# Rename columns for consistency
df.columns = [col.strip().replace(" ", "_").replace("(km/l)", "km_per_l").replace("(cc)", "cc").replace("(INR)", "INR") for col in df.columns]

# Handle missing values
df.dropna(inplace=True)  # Drop rows with missing values

# Convert categorical columns to lowercase for consistency
df = df.apply(lambda x: x.str.lower() if x.dtype == "object" else x)

# Summary Statistics
print("\n📌 Data Summary:")
print(df.describe())

# Price Distribution
plt.figure(figsize=(8, 5))
sns.histplot(df['Price_INR'], bins=30, kde=True, color='blue')
plt.title('Distribution of Bike Prices')
plt.xlabel('Price (INR)')
plt.ylabel('Frequency')
plt.show()

# Fuel Type Count
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='Fuel_Type', palette='viridis')
plt.title('Bike Fuel Type Distribution')
plt.xlabel('Fuel Type')
plt.ylabel('Count')
plt.show()

# Average Price by Brand
plt.figure(figsize=(12, 6))
brand_prices = df.groupby('Brand')['Price_INR'].mean().sort_values(ascending=False)
sns.barplot(x=brand_prices.index, y=brand_prices.values, palette='coolwarm')
plt.xticks(rotation=90)
plt.title('Average Bike Price by Brand')
plt.xlabel('Brand')
plt.ylabel('Average Price (INR)')
plt.show()

# Export cleaned data for Tableau
df.to_csv("cleaned_bike_sales.csv", index=False)
print("✅ Cleaned Data Saved for Tableau!")
