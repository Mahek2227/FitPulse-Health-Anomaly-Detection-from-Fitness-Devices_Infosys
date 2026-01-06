# Milestone 3: Anomaly Detection and Visualization

## Introduction
In this milestone, anomaly detection was performed on fitness device data
to identify unusual health patterns. The work is based on the forecasting
and clustering models developed in Milestone 2. The main focus of this
milestone is to detect abnormal behavior, label it clearly, and visualize
the results using time-series plots.

## Methodology
The Prophet time-series model from Milestone 2 was reused to generate
predicted values for heart rate and sleep data. Residuals were calculated
by finding the difference between the actual and predicted values. Large
residuals were considered as potential anomalies.

In addition to residual analysis, domain-based rules were applied.
Heart rate values below 50 bpm or above 100 bpm were marked as abnormal.
Sleep duration values below 5 hours or above 9 hours were also treated
as anomalies. DBSCAN clustering results from Milestone 2 were used to
support the identification of unusual behavior patterns.

## Anomaly Labeling
Each data point was labeled as normal or anomalous based on the residual
and domain-based conditions. If any one of the conditions was satisfied,
the data point was marked as an anomaly. This helped in clearly separating
normal observations from abnormal ones.

## Visualization
Time-series plots were created for heart rate and sleep data. Anomalies
were highlighted using colored markers to make them easily visible.
Date labels were formatted properly to avoid overlap and improve readability.

## Observations
A limited number of anomalies were detected in the dataset. This indicates
that the fitness data is mostly stable with occasional abnormal patterns.
The detected anomalies can represent irregular sleep behavior or unusual
heart rate values.

## Conclusion
This milestone successfully demonstrates anomaly detection using residual
analysis, domain knowledge, and clustering support. The visualizations
clearly highlight abnormal patterns over time and help in understanding
health-related deviations in fitness data.
