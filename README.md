# 📊 Outlier Analysis Automation with Power BI Dashboard

## 📌 Project Overview

This project demonstrates a fully automated data analytics pipeline combined with an interactive Power BI dashboard.  
The system processes raw retail transaction data, performs automated data cleaning, detects outliers using statistical methods, generates visual reports, and produces business-ready dashboards.

The objective is to build a scalable and reusable analytics workflow that improves data quality and enables business decision-making.

---

# 🎯 Project Objectives

- Automate raw data processing
- Clean and validate transactional data
- Detect and remove statistical outliers
- Generate automated charts
- Create summary and data quality reports
- Build interactive Power BI dashboards
- Extract meaningful business insights

---

# 🛠 Tools & Technologies Used

## Programming

- Python
- Pandas
- NumPy
- Matplotlib
- YAML Configuration

## Data Visualization

- Power BI
- DAX (Data Analysis Expressions)
- Data Modeling
- Interactive Dashboard Design

---

# ⚙️ Automated Pipeline Workflo
Raw Data
↓
Data Cleaning
↓
Outlier Detection
↓
Chart Generation
↓
Report Generation
↓
Processed Data
↓
Power BI Dashboard

---

# 📂 Project Structure

Outlier-Analysis-Automation/

│
├── config/
│ └── config.yaml
│
├── data/
│ ├── raw/
│ ├── processed/
│ └── archive/
│
├── logs/
│
├── models/
│ (Reserved for future ML models)
│
├── notebooks/
│ ├── 00_run_pipeline.ipynb
│ ├── 02_data_cleaning.ipynb
│ ├── 03_outlier_analysis.ipynb
│ └── 04_visualization.ipynb
│
├── outputs/
│ ├── charts/
│ └── reports/
│
├── powerbi/
│ └── Retail_Sales_Dashboard.pbix
│
├── src/
│ ├── pipeline.py
│ ├── data_loader.py
│ ├── data_cleaning.py
│ ├── outlier_detection.py
│ ├── visualization.py
│ ├── report_generator.py
│ ├── data_quality.py
│ └── utils/
│
├── requirements.txt
├── run_pipeline.py
└── README.md

---

# 📓 Jupyter Notebooks Description

The project includes modular notebooks for each stage of processing:

### 00_run_pipeline.ipynb

Runs the full automated pipeline:

- Loads raw data
- Cleans dataset
- Removes outliers
- Generates charts
- Creates reports
- Saves cleaned dataset

---

### 02_data_cleaning.ipynb

Handles data preparation tasks:

- Remove duplicate records
- Fill missing values
- Remove negative values
- Validate dataset structure

---

### 03_outlier_analysis.ipynb

Applies statistical outlier detection:

- Uses IQR method
- Identifies extreme values
- Removes statistical anomalies
- Improves data reliability

---

### 04_visualization.ipynb

Generates automated visual outputs:

- Boxplots
- Histograms
- Distribution charts
- Data trend visuals

---

# 📊 Power BI Dashboard Overview

The project includes a multi-page interactive dashboard.
"C:\Users\Debolina\OneDrive\Desktop\outlier analysis.pbix"

## Page 1 — Sales Overview Dashboard

Includes: Dasboard - <img width="1600" height="884" alt="Sales_dashboard" src="https://github.com/user-attachments/assets/d7e2a3eb-d139-4cc9-a46a-917dbe08d40e" />



- Total Revenue KPI
- Total Orders KPI
- Total Quantity KPI
- Total Customers KPI
- Country Count KPI
- Revenue Trend Over Time
- Top Countries by Revenue
- Top Products by Revenue
- Top Customers by Revenue

---

## Page 2 — Product Analysis Dashboard

Includes: Dshboard - <img width="1549" height="883" alt="Product_analysis" src="https://github.com/user-attachments/assets/927ce9ca-a4bd-4e1a-9344-3bb7b763d44f" />


- Product Revenue Distribution
- Monthly Quantity Trends
- Product Performance Insights
- Top Product Analysis

---

## Page 3 — Customer & Country Analysis

Includes: <img width="1489" height="857" alt="Country   Customer Analysis" src="https://github.com/user-attachments/assets/64bb74f7-8b91-4a3c-abe0-4032d27e952e" />


- Revenue by Country
- Customer Distribution
- Top Countries by Customers
- Geographic Performance

---

## Page 4 — Business Insights Summary
Dashboard - <img width="1421" height="949" alt="Business Insights" src="https://github.com/user-attachments/assets/2a25e9f9-dcdc-4565-9f00-9cce6e23f430" />


Key insights generated from analysis:

- United Kingdom contributes the highest revenue.
- Revenue trends indicate seasonal demand patterns.
- Top products contribute significantly to total revenue.
- Customer activity is concentrated across major countries.
- Data cleaning improved overall data reliability.

---

# 📈 Business Insights

Key observations derived from processed data:

- Revenue is highly concentrated among top-performing countries.
- Monthly trends show peak sales periods.
- Certain products dominate revenue generation.
- Customer distribution indicates regional dominance.
- Outlier removal improved statistical accuracy.

---

# 📊 Automated Outputs Generated

Each pipeline run automatically generates:

### Cleaned Dataset
data/processed/cleaned_data_TIMESTAMP.csv

---

### Charts

outputs/charts/ 

Includes:

- Quantity Boxplot      <img width="640" height="480" alt="quantity_boxplot_20260424_051639" src="https://github.com/user-attachments/assets/983a4ffc-a749-458e-844a-09ed3f044349" />

- Unit Price Histogram     <img width="640" height="480" alt="unitprice_histogram_20260424_051639" src="https://github.com/user-attachments/assets/2be5cf30-fa1c-4f70-838f-cea4504e0ec0" />


---

### Reports

outputs/reports/

Includes:

- Summary Report (.txt)
- Data Quality Report (.csv)

---

### Archive

Processed raw files automatically move to:

data/archive/

---

# 🚀 How to Run This Project

## Step 1 — Install Requirements

```bash
pip install -r requirements.txt
Step 2 — Add Raw Data

Place dataset inside:
data/raw/
Step 3 — Run Pipeline
python run_pipeline.py
Pipeline will automatically:

Process data
Generate charts
Create reports
Save cleaned dataset
Archive raw file
🔄 Automation Features

This project supports:

✔ Automatic file detection
✔ Automatic cleaning
✔ Automatic outlier removal
✔ Automatic chart generation
✔ Automatic report generation
✔ Automatic archiving
✔ Timestamp-based versioning
# ⭐ Project Highlights

✔ Built a fully automated data processing pipeline  

✔ Implemented statistical outlier detection using IQR method  

✔ Generated automated reports and visualizations  

✔ Designed a multi-page interactive Power BI dashboard  

✔ Improved data reliability through systematic cleaning  

✔ Created business-ready analytical insights

# 📂 Data Source

Dataset Name: Online Retail Dataset  

Source: UCI Machine Learning Repository  

Description:

This dataset contains transactional data for an online retail store, including invoice details, product information, customer IDs, quantities, prices, and countries.

Dataset Features:

- InvoiceNo — Unique invoice number  
- StockCode — Product code  
- Description — Product description  
- Quantity — Quantity purchased  
- InvoiceDate — Date of transaction  
- UnitPrice — Price per unit  
- CustomerID — Unique customer identifier  
- Country — Country of customer  

Source Link:  
https://archive.ics.uci.edu/ml/datasets/online+retail
# ⚠️ Dataset Usage Note

This dataset is used for educational and analytical purposes only.  
All transformations and visualizations were created as part of a data analytics learning project.
# 👤 Author

Name: Debolina Sorkhel  

Role: Data Analyst | Aspiring Data Scientist  

Skills:

- Python
- Power BI
- SQL
- Data Visualization
- Data Cleaning
- Outlier Detection
- Dashboard Development

GitHub: https://github.com/debolina696

LinkedIn: https://www.linkedin.com/in/debolina-sorkhel-91647526b/




