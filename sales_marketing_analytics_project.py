# Sales & Marketing Analytics Project
# Project: Sales & Marketing Performance Dashboard
# Tech Stack: Python, Pandas, SQL (SQLite), Power BI-ready CSVs
# Author: Azam

# =============================
# 1. Project Structure
# =============================
# sales_marketing_project/
# ├── data/
# │   ├── sales_data.csv
# │   ├── marketing_data.csv
# ├── scripts/
# │   ├── data_generator.py
# │   ├── analysis.py
# │   ├── kpi_calculator.py
# ├── outputs/
# │   ├── cleaned_sales.csv
# │   ├── cleaned_marketing.csv
# │   ├── kpi_report.csv
# ├── README.md

# =============================
# 2. data_generator.py
# =============================
import pandas as pd
import random
from datetime import datetime, timedelta

random.seed(42)

# Generate Sales Data
sales_data = []
for i in range(500):
    sales_data.append({
        "order_id": i+1,
        "date": datetime(2025,1,1) + timedelta(days=random.randint(0,300)),
        "region": random.choice(["North","South","East","West"]),
        "product": random.choice(["CRM","Analytics","ERP","MobileApp"]),
        "revenue": random.randint(5000, 80000),
        "customer_type": random.choice(["New","Returning"])
    })

sales_df = pd.DataFrame(sales_data)
sales_df.to_csv("data/sales_data.csv", index=False)

# Generate Marketing Data
marketing_data = []
for i in range(500):
    marketing_data.append({
        "campaign_id": i+1,
        "date": datetime(2025,1,1) + timedelta(days=random.randint(0,300)),
        "channel": random.choice(["Google Ads","Facebook","Instagram","Email","SEO"]),
        "spend": random.randint(1000, 20000),
        "leads": random.randint(10, 500),
        "conversions": random.randint(1, 80)
    })

marketing_df = pd.DataFrame(marketing_data)
marketing_df.to_csv("data/marketing_data.csv", index=False)

print("Data Generated Successfully")

# =============================
# 3. analysis.py
# =============================
import pandas as pd

sales = pd.read_csv("data/sales_data.csv")
marketing = pd.read_csv("data/marketing_data.csv")

# Cleaning
sales.dropna(inplace=True)
marketing.dropna(inplace=True)

# Save cleaned data
sales.to_csv("outputs/cleaned_sales.csv", index=False)
marketing.to_csv("outputs/cleaned_marketing.csv", index=False)

# =============================
# 4. kpi_calculator.py
# =============================
import pandas as pd

sales = pd.read_csv("outputs/cleaned_sales.csv")
marketing = pd.read_csv("outputs/cleaned_marketing.csv")

# KPIs
total_revenue = sales['revenue'].sum()

total_spend = marketing['spend'].sum()
total_leads = marketing['leads'].sum()
total_conversions = marketing['conversions'].sum()

cac = total_spend / total_conversions
conversion_rate = (total_conversions / total_leads) * 100

kpi_data = {
    "Metric": ["Total Revenue","Total Marketing Spend","Total Leads","Total Conversions","CAC","Conversion Rate (%)"],
    "Value": [total_revenue,total_spend,total_leads,total_conversions,cac,conversion_rate]
}

kpi_df = pd.DataFrame(kpi_data)
kpi_df.to_csv("outputs/kpi_report.csv", index=False)

print("KPI Report Generated")

# =============================
# 5. README.md
# =============================
# Sales & Marketing Analytics Project

## Objective
Analyze sales and marketing data to measure performance, ROI, and business growth.

## KPIs
- Total Revenue
- Marketing Spend
- Customer Acquisition Cost (CAC)
- Conversion Rate
- Leads & Conversions

## Tools Used
- Python
- Pandas
- Power BI / Excel

## Outputs
- Cleaned datasets
- KPI report
- Dashboard-ready CSVs

## How to Run
1. python data_generator.py
2. python analysis.py
3. python kpi_calculator.py

## Dashboard
Use Power BI / Excel to visualize:
- Revenue by Region
- Campaign ROI
- Funnel Analysis
- Channel Performance

# =============================
# 6. SQL VERSION (FOR ANALYST ROLES)
# =============================

-- File: sales_marketing_analysis.sql
-- Database: SQLite / MySQL compatible

-- =============================
-- TABLE CREATION
-- =============================

CREATE TABLE sales_data (
    order_id INTEGER PRIMARY KEY,
    order_date DATE,
    region TEXT,
    product TEXT,
    revenue INTEGER,
    customer_type TEXT
);

CREATE TABLE marketing_data (
    campaign_id INTEGER PRIMARY KEY,
    campaign_date DATE,
    channel TEXT,
    spend INTEGER,
    leads INTEGER,
    conversions INTEGER
);

-- =============================
-- KPI QUERIES
-- =============================

-- 1. Total Revenue
SELECT SUM(revenue) AS total_revenue FROM sales_data;

-- 2. Revenue by Region
SELECT region, SUM(revenue) AS revenue
FROM sales_data
GROUP BY region
ORDER BY revenue DESC;

-- 3. Revenue by Product
SELECT product, SUM(revenue) AS revenue
FROM sales_data
GROUP BY product
ORDER BY revenue DESC;

-- 4. Total Marketing Spend
SELECT SUM(spend) AS total_marketing_spend FROM marketing_data;

-- 5. Cost per Acquisition (CAC)
SELECT 
    ROUND(SUM(spend) * 1.0 / SUM(conversions), 2) AS CAC
FROM marketing_data;

-- 6. Conversion Rate
SELECT 
    ROUND((SUM(conversions) * 100.0 / SUM(leads)), 2) AS conversion_rate
FROM marketing_data;

-- 7. Channel Performance
SELECT 
    channel,
    SUM(spend) AS total_spend,
    SUM(leads) AS total_leads,
    SUM(conversions) AS total_conversions,
    ROUND(SUM(spend) * 1.0 / SUM(conversions), 2) AS CAC
FROM marketing_data
GROUP BY channel
ORDER BY total_conversions DESC;

-- 8. Monthly Revenue Trend
SELECT 
    strftime('%Y-%m', order_date) AS month,
    SUM(revenue) AS monthly_revenue
FROM sales_data
GROUP BY month
ORDER BY month;

-- 9. New vs Returning Customers Revenue
SELECT 
    customer_type,
    SUM(revenue) AS revenue
FROM sales_data
GROUP BY customer_type;

-- =============================
-- BUSINESS INSIGHTS
-- =============================
-- Identify best-performing region and channel
-- Track ROI and growth trends
-- Support pricing and campaign decisions

