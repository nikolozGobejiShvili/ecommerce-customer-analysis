# Ecommerce Customer Analysis

A data analysis project focused on customer segmentation and behavioral insights using the **RFM (Recency, Frequency, Monetary)** model.  
Built with **Python**, this project identifies the most valuable customers, visualizes spending patterns, and provides an interactive dashboard.

---

## Features

- Data Cleaning: Removes missing values, duplicates, and invalid transactions.  
- RFM Analysis: Calculates Recency, Frequency, and Monetary metrics.  
- Customer Segmentation: Groups customers into actionable categories.  
- Visualization: Creates static and interactive charts to explore data.  
- Dash App: Interactive dashboard powered by Plotly Dash.

---

## RFM Overview

| Metric | Description |
|:-------|:-------------|
| Recency (R) | How recently a customer made a purchase |
| Frequency (F) | How often they purchase |
| Monetary (M) | How much money they spend |

Combining these gives an **RFM Score**, which helps identify:
- Champions (recent, frequent, high-spending)
- At Risk (used to buy often but not recently)
- Lost (haven’t purchased in a long time)

---

## Tech Stack

- Python 3.12  
- Pandas – data manipulation  
- Plotly / Dash – interactive visualization  
- Matplotlib / Seaborn – static visualization  
- VS Code – development & testing  

---

## Project Structure

ecommerce-customer-analysis/
│
├── data/
│ └── OnlineRetail.csv
│
├── output/
│ ├── rfm_results.csv
│ └── rfm_scatter.png
│
├── src/
│ ├── data_cleaning.py
│ ├── rfm_analysis.py
│ ├── visualize.py
│ └── app.py
│
├── main.py
├── requirements.txt
└── README.md



---

## How to Run Locally

1. Install dependencies:
```bash
pip install -r requirements.txt
