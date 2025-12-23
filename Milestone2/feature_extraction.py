from tsfresh import extract_features
from tsfresh.utilities.dataframe_functions import impute

def run_tsfresh(df, id_col, time_col):
    features = extract_features(
        df,
        column_id=id_col,
        column_sort=time_col
    )
    impute(features)
    return features
