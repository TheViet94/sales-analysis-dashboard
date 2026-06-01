# Sales Analysis Dashboard

## 1. Project Overview

This project is a **Power BI Sales Analysis Dashboard** built to analyze sales performance across multiple business dimensions, including revenue trends, product performance, customer behavior, salesperson performance, and geographic revenue distribution.

The project follows a structured analytics workflow:

```text
Raw Data → Cleaned Data → Data Mart / Star Schema → Power BI Dashboard → Business Insights
```

The final dashboard helps support business decisions related to revenue monitoring, product strategy, customer segmentation, employee performance evaluation, and market performance analysis.

---

## 2. Business Objectives

This project focuses on five main business analysis scenarios:

1. **Revenue Trend **  
   Analyze actual revenue performance over time and identify monthly growth or decline patterns.

2. **Product Performance **  
   Rank products by revenue, identify best-selling and underperforming products, and evaluate product class performance.

3. **Customer Segmentation**  
   Segment customers based on purchase frequency and spending value, analyze repeat customers, AOV, and basket size.

4. **Salesperson Leaderboard**  
   Evaluate salesperson revenue contribution, identify top performers and underperformers, and track performance trends over time.

5. **Geographic Distributio**  
   Analyze revenue, order volume, customer distribution, and market performance by city and country.

---

## 3. Tools & Technologies

- **Power BI** — dashboard design and data visualization
- **DAX** — KPI measures, ranking, MoM growth, and business calculations
- **BigQuery** — data storage and transformation
- **Google Cloud Storage** — external storage for large exported datasets
- **GitHub** — project documentation and version control
- **CSV** — exported datasets for portfolio demonstration

---

## 4. Dataset Structure

The project data is organized into three layers:

```text
data/
├── raw/
├── processed/
└── mart/
```

### Raw Data

The `raw/` folder contains original source data before cleaning.

Example files:

```text
categories.csv
cities.csv
countries.csv
customers.csv
employees.csv
products.csv
sales_sample.csv
```

### Processed Data

The `processed/` folder contains cleaned and standardized data after preprocessing.

Example files:

```text
categories.csv
cities.csv
countries.csv
customers.csv
employees.csv
products.csv
sales_sample.csv
```

### Data Mart

The `mart/` folder contains the final dimensional model used for Power BI.

```text
dim_customer.csv
dim_date.csv
dim_employee.csv
dim_geography.csv
dim_product.csv
fact_sales_sample.csv
```

> Note: Full transaction tables such as `sales.csv` and `fact_sales.csv` are excluded from this repository because they exceed GitHub's file size limit. Sample versions are included for demonstration purposes.

---

## 5. Data Model

The final data mart follows a **star schema** structure.

### Fact Table

| Table | Description |
|---|---|
| `fact_sales` | Contains transactional sales data such as transaction number, customer, product, employee, geography, quantity, and actual revenue. |

### Dimension Tables

| Table | Description |
|---|---|
| `dim_date` | Date dimension used for monthly trend and MoM analysis. |
| `dim_product` | Product attributes such as product name, category, and class. |
| `dim_customer` | Customer information used for customer-level analysis. |
| `dim_employee` | Employee / salesperson information used for performance analysis. |
| `dim_geography` | City and country information used for geographic analysis. |

The data model supports analytical reporting across time, product, customer, employee, and geography dimensions.

---

## 6. Dashboard Pages

The Power BI dashboard contains six report pages.

### Page 1 — Executive Overview

Provides a high-level overview of business performance.

Main visuals:

- Total Revenue
- Total Orders
- Total Customers
- AOV
- Revenue by Month
- Revenue by Category
- Top 10 Cities by Revenue
- Top 5 Products by Revenue

---

### Page 2 — Revenue Trend Analysis

Analyzes monthly revenue performance and category contribution over time.

Main visuals:

- Total Revenue
- Current Month Revenue
- Revenue MoM %
- Monthly Revenue Trend
- Revenue MoM % by Month
- Revenue Trend by Category
- Category Revenue Share by Month

---

### Page 3 — Product Performance Analysis

Evaluates product performance and product class contribution.

Main visuals:

- Total Products
- Total Revenue
- Total Quantity
- Average Revenue per Product
- Top 5 Products by Revenue
- Bottom 5 Products by Revenue
- Product Revenue Ranking
- Quantity vs Revenue — Top 100 Products
- Revenue by Product Class

---

### Page 4 — Customer Behavior & Segmentation

Analyzes customer behavior and customer segments.

Main visuals:

- Repeat Rate
- Average Order Value
- Basket Size
- Customer Segmentation by Revenue and Frequency
- Repeat vs One-time Customers
- AOV Distribution
- Basket Size by Customer Segment

---

### Page 5 — Salesperson Performance Analysis

Evaluates salesperson performance and revenue contribution.

Main visuals:

- Total Orders
- Total Revenue
- Average Revenue per Salesperson
- Average Orders per Salesperson
- Top 5 Salespersons by Revenue
- Bottom 5 Salespersons by Revenue
- Revenue Trend by Top 5 Salespersons
- Salesperson Revenue Share by Month
- Salesperson Performance Summary Table

---

### Page 6 — Geographic Revenue Analysis

Analyzes sales performance by geographic market.

Main visuals:

- Total Revenue
- Total Quantity
- Total Orders
- Total Customers
- Top 10 Cities by Revenue
- Top 10 Cities by Quantity
- Geographic Performance Summary
- Revenue Share by City

---

## 7. Dashboard Preview

Dashboard screenshots are stored in the `images/` folder.

```text
images/
├── executive_overview.png
├── revenue_trend_analysis.png
├── product_performance_analysis.png
├── customer_behavior_segmentation.png
├── salesperson_performance_analysis.png
└── geographic_revenue_analysis.png
```

---

## 8. Key Metrics

| Metric | Description |
|---|---|
| Total Revenue | Total actual revenue after discount |
| Total Orders | Total number of unique transactions |
| Total Customers | Total number of unique customers |
| Total Quantity | Total quantity of products sold |
| AOV | Average Order Value |
| Basket Size | Average quantity per order |
| Revenue MoM % | Month-over-month revenue growth percentage |
| Product Rank | Product ranking based on total revenue |
| Salesperson Rank | Salesperson ranking based on total revenue |
| Repeat Rate % | Percentage of customers who purchased more than once |

---

## 9. Key Insights

- Overall sales performance reached approximately **4.29bn total revenue**, with around **7M total orders** and **99K customers**.
- The overall **Average Order Value (AOV)** was **641.08**, showing the average revenue generated per transaction.
- Monthly revenue remained relatively stable from **2018-01 to 2018-04**, ranging from approximately **929M to 1,032M**, before dropping sharply to around **300M** in **2018-05**.
- The latest month revenue was around **299.83M**, indicating a significant decline compared with previous months.
- Category revenue share remained relatively stable across months, suggesting that the revenue decline affected multiple categories rather than one single category.
- The product portfolio included **452 products**, generating approximately **3,989.41M** in revenue and **81M** in quantity sold.
- Average revenue per product was around **8.83M**.
- Top products generated relatively similar revenue levels, indicating that sales performance was not overly dependent on one single product.
- Customer analysis showed a **100% repeat customer rate** because all customers had purchase frequency greater than one.
- The average basket size was **13.00 products per order**.
- Salesperson analysis showed approximately **4.29bn total revenue**, with average revenue per salesperson around **186.49M** and average orders per salesperson around **290.90K**.
- Salesperson revenue contribution was relatively evenly distributed across months, suggesting that revenue was not highly dependent on one individual salesperson.
- Geographic analysis showed approximately **87M total quantity**, **7M total orders**, and **99K customers** across city-level markets.
- Top cities by revenue had relatively close performance, indicating a fairly distributed market across major cities.

---

## 10. DAX Measures

Important DAX measures used in this dashboard are documented in:

```text
dax/measures.md
```

Examples of key measures:

- Total Revenue
- Total Orders
- Total Customers
- AOV
- Basket Size
- Revenue MoM %
- Product Rank
- Repeat Rate %
- Salesperson Revenue Share

---

## 11. Power BI File

The full Power BI `.pbix` file is not included directly in this repository because it exceeds GitHub's file size limit.

You can access the full Power BI dashboard file here:

[Download Power BI Dashboard](https://drive.google.com/file/d/15-GOytCaRdcQLPOf6vSSTx_NCTkLcNRF/view?usp=sharing)

---

## 12. How to Use

1. Clone this repository:

```bash
git clone https://github.com/TheViet94/sales-analysis-dashboard.git
```

2. Open the repository folder:

```bash
cd sales-analysis-dashboard
```

3. Review the dashboard screenshots in the `images/` folder.

4. Review the DAX logic in:

```text
dax/measures.md
```

5. Download the full Power BI file from the Google Drive link above if you want to open the dashboard in Power BI Desktop.

---

## 13. Project Structure

```text
sales-analysis-dashboard/
│
├── README.md
├── .gitignore
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── mart/
│
├── dax/
│   └── measures.md
│
├── images/
│   ├── executive_overview.png
│   ├── revenue_trend_analysis.png
│   ├── product_performance_analysis.png
│   ├── customer_behavior_segmentation.png
│   ├── salesperson_performance_analysis.png
│   └── geographic_revenue_analysis.png
│
└── powerbi/
```

---

## 14. Repository Notes

Large files are excluded from the repository due to GitHub file size limits:

```text
data/raw/sales.csv
data/processed/sales.csv
data/mart/fact_sales.csv
powerbi/*.pbix
```

Sample datasets and dashboard screenshots are included for portfolio demonstration.

---

## 15. Project Outcome

This project demonstrates the ability to:

- Build a complete Power BI dashboard from structured sales data
- Design a dimensional data model using fact and dimension tables
- Apply DAX measures for business KPIs, ranking, and growth analysis
- Analyze sales performance across time, product, customer, employee, and geography dimensions
- Present business insights in a clear and interactive dashboard format