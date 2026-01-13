# 🏃 Health Anomaly Detection Dashboard – Project Summary

## 1. Project Overview
The **Health Anomaly Detection Dashboard** is an interactive web application developed using **Streamlit**. 
It allows users to **upload fitness data** (heart rate, steps, and sleep) and detect unusual patterns or anomalies in their activity. 
This helps users and healthcare professionals monitor health trends and identify irregularities early.

## 2. Objectives
- Detect anomalies in user fitness data using both **statistical and rule-based methods**.  
- Provide **visualizations** of trends and anomalies for easier interpretation.  
- Allow users to **download anomaly reports** for personal tracking or clinical use.  
- Enable **activity clustering** to understand patterns in user behavior.  

## 3. Key Features
1. **File Upload:** Users can upload CSV files containing fitness data, including timestamps, user IDs, heart rate, sleep, and steps.
2. **Data Cleaning:** Automatically handles missing values, converts timestamps, and ensures numeric data consistency.
3. **Filters:** Select **User ID** and **metric** (heart rate, sleep, steps).
4. **Activity Clustering:** Uses **PCA** and **DBSCAN** to cluster user activity data and visualize clusters.
5. **Anomaly Detection:** 
   - Statistical anomalies using rolling averages and standard deviation thresholds.  
   - Rule-based alerts for extreme heart rate, sleep, and steps.
6. **Visualization:** Time-series plots highlighting anomalies in red.
7. **Report Download:** Download detected anomalies as a **CSV file**.

## 4. Methodology
1. Data Preprocessing: Remove missing values, fill numeric columns with mean.  
2. Clustering: Standardize features, reduce dimensionality with PCA, apply DBSCAN.  
3. Anomaly Detection: Smooth data using rolling average, detect deviations >2.5 std, apply rule-based thresholds.  
4. Dynamic Adjustments: Rolling window adapts to dataset size for small datasets.

## 5. Tools and Libraries
- **Python**, **Streamlit**, **Pandas**, **NumPy**, **Matplotlib**, **Scikit-learn**

## 6. Usage Instructions
1. Run locally: `streamlit run app.py` or use deployed link.  
2. Upload CSV with fitness data.  
3. Select **User ID** and **metric**.  
4. Explore cluster plots and anomaly trends.  
5. Download anomaly report if needed.

## 7. Key Observations
- Small datasets handled dynamically without errors.  
- Anomalies highlighted clearly in plots and tables.  
- Both statistical and rule-based alerts ensure robust detection.

## 8. Conclusion
This dashboard offers a **user-friendly and insightful solution** for monitoring fitness data and detecting unusual patterns. 
It can be used for personal health tracking or by healthcare professionals to identify anomalies early and take preventive actions.


## Live Link Of Dashboard:
https://fitpulse-zb79zfzuph8fwz2xuwxrab.streamlit.app/
