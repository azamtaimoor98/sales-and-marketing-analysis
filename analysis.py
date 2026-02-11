import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data/raw_sales_data.csv")

# Data Cleaning
df["Order_Date"] = pd.to_datetime(df["Order_Date"])
df.drop_duplicates(inplace=True)

# Create new metrics
df["ROI"] = (df["Sales"] - df["Marketing_Spend"]) / df["Marketing_Spend"]

# Save cleaned data
df.to_csv("data/cleaned_sales_data.csv", index=False)

# Monthly Sales Trend
df["Month"] = df["Order_Date"].dt.to_period("M")
monthly_sales = df.groupby("Month")["Sales"].sum()

plt.figure()
monthly_sales.plot(title="Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("monthly_sales_trend.png")
plt.close()

# Sales by Category
category_sales = df.groupby("Category")["Sales"].sum()

plt.figure()
category_sales.plot(kind="bar", title="Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("sales_by_category.png")
plt.close()

# ROI by Channel
roi_by_channel = df.groupby("Channel")["ROI"].mean()

plt.figure()
roi_by_channel.plot(kind="bar", title="Average ROI by Channel")
plt.xlabel("Channel")
plt.ylabel("ROI")
plt.tight_layout()
plt.savefig("roi_by_channel.png")
plt.close()

print("Analysis completed. Files generated:")
print("- cleaned_sales_data.csv")
print("- monthly_sales_trend.png")
print("- sales_by_category.png")
print("- roi_by_channel.png")
