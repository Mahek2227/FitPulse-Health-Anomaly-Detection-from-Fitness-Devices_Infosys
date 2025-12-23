import pandas as pd

def preprocess_csv(input_path, output_path):
    df = pd.read_csv(input_path)
    df.columns = df.columns.str.lower().str.replace(" ", "_")
    df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
    df = df.dropna()
    df.to_csv(output_path, index=False)
    return df
