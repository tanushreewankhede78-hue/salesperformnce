import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load data
df = pd.read_csv("sales.csv")

# Step 2: Clean data
df = df.dropna()

# Step 3: Create total sales column
df["Total_Sales"] = df["Quantity"] * df["Price"]

# Step 4: Total revenue
total_revenue = df["Total_Sales"].sum()
print("Total Revenue:", total_revenue)

# Step 5: Product-wise sales
product_sales = df.groupby("Product")["Total_Sales"].sum()
print("\nProduct-wise Sales:")
print(product_sales)

# Step 6: Region-wise sales
region_sales = df.groupby("Region")["Total_Sales"].sum()
print("\nRegion-wise Sales:")
print(region_sales)

# Step 7: Monthly trend
df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.month
monthly_sales = df.groupby("Month")["Total_Sales"].sum()

# Step 8: Visualization
product_sales.plot(kind="bar", title="Product Wise Sales")
plt.show()

monthly_sales.plot(kind="line", marker="o", title="Monthly Sales Trend")
plt.show() 