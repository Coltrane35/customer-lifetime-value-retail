# Customer Lifetime Value (CLV) Prediction for E-commerce

Business-oriented data science project focused on customer segmentation and lifetime value prediction for e-commerce companies.

## Problem
E-commerce businesses need to identify high-value customers, prevent churn, and optimize marketing spend.

## Solution
An end-to-end CLV pipeline using:
- Transaction-level data
- RFM segmentation
- Machine Learning (CatBoost)

## Dataset
Online Retail transactional dataset (UK-based e-commerce).

## Pipeline
1. Data cleaning & feature engineering
2. RFM analysis (Recency, Frequency, Monetary)
3. Customer segmentation
4. CLV prediction using CatBoost
5. Business-ready outputs

## Model
- Algorithm: CatBoost Regressor
- Target: Customer Monetary Value (log-scaled)
- Metric: MAE ≈ 1200

## Key Outputs
- `rfm_segments.csv` – customer segmentation
- `customer_clv_predictions.csv` – predicted CLV per customer
- `top_10_customers.csv` – most valuable customers
- CLV model file (`.cbm`)

## Business Insights
- Champions show the highest predicted CLV
- At Risk customers have high CLV but increasing recency
- Lost customers represent churn recovery opportunities
- New customers require onboarding strategies

## Use Cases
- Customer retention strategies
- Marketing budget optimization
- Loyalty and VIP programs
- Revenue forecasting

## Tech Stack
Python, Pandas, NumPy, CatBoost, Matplotlib
