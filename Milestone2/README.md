# FitPulse – Health Anomaly Detection from Fitness Devices  
## Milestone 2: Feature Extraction and Modeling

### Objective
The objective of Milestone 2 is to extract meaningful features from fitness time-series data, analyze temporal trends, and identify behavioral patterns using unsupervised learning techniques. This milestone prepares the groundwork for anomaly detection in subsequent milestones.

---

### Dataset Description
The dataset contains time-series data collected from wearable fitness devices, including:
- User ID
- Timestamp
- Heart Rate
- Step Count
- Sleep Duration

The uploaded datasets are preprocessed to handle missing values, ensure numeric consistency, and prepare the data for feature extraction and modeling.

---

### Steps Performed

#### 1. Data Preprocessing
- Uploaded CSV files using Google Colaboratory
- Converted timestamps to datetime format
- Handled missing and non-numeric values
- Generated cleaned datasets suitable for analysis

#### 2. Feature Extraction
- Used **TSFresh** to automatically extract statistical and frequency-based features
- Extracted features such as mean, variance, entropy, energy, and Fourier-based characteristics
- Created a high-dimensional feature matrix for each user

#### 3. Trend Modeling
- Applied **Facebook Prophet** to model temporal trends in heart rate, steps, and sleep data
- Forecasted expected behavior and visualized trends with confidence intervals
- Observed deviations from forecasts that may indicate unusual behavior

#### 4. Behavioral Pattern Clustering
- Standardized extracted features using **StandardScaler**
- Reduced dimensionality using **Principal Component Analysis (PCA)** for visualization
- Applied **KMeans clustering** to group users based on behavioral similarity
- Applied **DBSCAN clustering** to identify dense behavioral patterns and potential outliers
- Visualized clustering results in 2D PCA space

---

### Tools and Libraries Used
- Python
- Pandas, NumPy
- TSFresh
- Facebook Prophet
- Scikit-learn
- Matplotlib
- Google Colaboratory

---

### Key Observations
- TSFresh generated a rich set of statistical features capturing user behavior
- Prophet effectively modeled temporal trends and seasonal patterns
- PCA helped reduce feature dimensionality for visualization
- KMeans grouped users into distinct behavioral clusters
- DBSCAN highlighted dense clusters and potential a typical behavior
- The results provide a strong foundation for anomaly detection in later milestones

