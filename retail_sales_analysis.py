# Step 1: Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 2: Load Dataset
df = pd.read_csv("Superstore.csv", encoding='ISO-8859-1')
print("Top 5 rows:")
print(df.head())

# Step 3: Basic Info
print("\nInfo:")
print(df.info())
print("\nMissing Values:")
print(df.isnull().sum())

# Step 4: Clean Data
df = df.dropna()

# Step 5: Total Sales
total_sales = df['Sales'].sum()
print("\nTotal Sales:", total_sales)

# Step 6: Sales by Category
sales_by_category = df.groupby('Category')['Sales'].sum()
print("\nSales by Category:")
print(sales_by_category)

# Step 7: Profit by Category
profit_by_category = df.groupby('Category')['Profit'].sum()
print("\nProfit by Category:")
print(profit_by_category)

# Step 8: Top 5 States by Sales
top5_states = df.groupby('State')['Sales'].sum().sort_values(ascending=False).head(5)
print("\nTop 5 States by Sales:")
print(top5_states)

# Step 9: Graphs
plt.figure(figsize=(8,5))
sns.barplot(x=sales_by_category.index, y=sales_by_category.values)
plt.title("Sales by Category")
plt.show()

plt.figure(figsize=(8,5))
sns.barplot(x=profit_by_category.index, y=profit_by_category.values)
plt.title("Profit by Category")
plt.show()

plt.figure(figsize=(10,6))
sns.barplot(x=top5_states.index, y=top5_states.values)
plt.title("Top 5 States by Sales")
plt.show()