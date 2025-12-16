# FitPulse Anomaly Detection – Milestone 1

Live Application URL:
https://huggingface.co/spaces/username/FitPulse-Anomaly-Detection

## Project Overview
FitPulse is a fitness data anomaly detection system.  
This milestone focuses on data collection and preprocessing using a Streamlit-based application.

The application ingests raw fitness data, performs timestamp normalization, resampling, and missing value handling, and produces a clean dataset suitable for further analysis.

## Milestone 1 Objectives
- Ingest fitness data in CSV or JSON format  
- Detect or manually specify timestamp columns  
- Normalize timestamps to UTC  
- Resample data to a 1-minute frequency  
- Handle missing values using domain-specific strategies  
- Generate a cleaned dataset for analysis  

## Application Output
The Streamlit application provides:

### Raw Data Preview
- Displays the first 5 rows of the uploaded dataset  
- Shows original values prior to preprocessing  

### Processed Data Preview
- Displays the first 10 rows after preprocessing  
- Data aligned to 1-minute intervals  
- Missing values handled appropriately  
- Timestamps converted to UTC  
- Cleaned dataset available for download  


## Dataset Description

### Raw Data
- Contains fitness-related attributes such as steps, calories burned, heart rate, and sleep duration  
- Timestamps may be irregular or incomplete  

### Processed Data
- Timestamps normalized to UTC  
- Data resampled to 1-minute granularity  
- Missing values handled according to preprocessing rules  
- Dataset ready for anomaly detection  

## Preprocessing Pipeline

### Data Ingestion
- Supports CSV and JSON file formats  
- Automatically detects file type  

### Timestamp Normalization
- Automatically detects timestamp column when not specified  
- Allows manual timestamp column input  
- Converts timestamps to UTC  
- Supports user-specified source timezone  

### Resampling
- Data resampled to 1-minute frequency  
- Aggregation method used: mean  

### Missing Value Handling
- Steps and calories are filled with zero  
- Heart rate values are interpolated using time-based interpolation  
- Sleep data is forward filled  
- Other columns are forward filled

 ## Sample Output
The following screenshots show the application output after loading a dataset:

- Raw data preview before preprocessing
- Processed data preview after preprocessing

## How to Run the Application

### Install Dependencies
```bash
pip install -r requirements.txt
