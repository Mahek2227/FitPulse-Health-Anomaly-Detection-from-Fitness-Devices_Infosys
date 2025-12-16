import pandas as pd
import numpy as np
import io
from typing import Optional

COMMON_TIMESTAMP_NAMES = [
    "timestamp", "time", "datetime", "date", "ts",
    "start_time", "activityhour"
]


# ---------------------------
# Auto-detect timestamp column
# ---------------------------
def _find_timestamp_column(df: pd.DataFrame) -> Optional[str]:
    lower_cols = [c.lower() for c in df.columns]
    for c in COMMON_TIMESTAMP_NAMES:
        if c in lower_cols:
            return df.columns[lower_cols.index(c)]
    return None


# ---------------------------
# Load CSV or JSON
# ---------------------------
def load_file(contents: bytes, filename: str) -> pd.DataFrame:
    name = filename.lower()
    if name.endswith(".csv"):
        return pd.read_csv(io.BytesIO(contents))
    if name.endswith(".json") or name.endswith(".ndjson"):
        try:
            return pd.read_json(io.BytesIO(contents), lines=True)
        except ValueError:
            return pd.read_json(io.BytesIO(contents))
    raise ValueError("Unsupported file type. Upload CSV or JSON only.")


# ---------------------------
# Normalize timestamps to UTC
# ---------------------------
def normalize_timestamps(
    df: pd.DataFrame,
    timestamp_col: Optional[str] = None,
    timezone_from: Optional[str] = None,
    to_utc: bool = True
) -> pd.DataFrame:

    df = df.copy()

    if timestamp_col is None:
        timestamp_col = _find_timestamp_column(df)
        if timestamp_col is None:
            raise ValueError("No timestamp column found.")

    df[timestamp_col] = pd.to_datetime(
        df[timestamp_col], errors="coerce", dayfirst=True
    )

    if df[timestamp_col].isna().all():
        raise ValueError("Timestamp parsing failed.")

    if timezone_from:
        if timezone_from.lower() == "kolkata":
            timezone_from = "Asia/Kolkata"
        try:
            df[timestamp_col] = df[timestamp_col].dt.tz_localize(timezone_from)
        except TypeError:
            pass

    if to_utc:
        try:
            df[timestamp_col] = df[timestamp_col].dt.tz_convert("UTC")
        except TypeError:
            df[timestamp_col] = df[timestamp_col].dt.tz_localize("UTC")

    df = df.set_index(timestamp_col).sort_index()
    return df


# ---------------------------
# Resample to 1-minute
# ---------------------------
def resample_df(df: pd.DataFrame, freq="1T", how="mean") -> pd.DataFrame:
    if not isinstance(df.index, pd.DatetimeIndex):
        raise ValueError("Index must be DatetimeIndex.")

    agg = {"mean": "mean", "sum": "sum", "median": "median"}.get(how, "mean")
    return df.resample(freq).agg(agg)


# ---------------------------
# Handle missing values (Milestone logic)
# ---------------------------
def handle_missing(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    for col in df.columns:
        col_l = col.lower()

        if "step" in col_l or "calorie" in col_l:
            df[col] = df[col].fillna(0)

        elif "heart" in col_l:
            df[col] = df[col].interpolate(method="time")

        elif "sleep" in col_l:
            df[col] = df[col].fillna(method="ffill")

        else:
            df[col] = df[col].fillna(method="ffill")

    return df


# ---------------------------
# Full preprocessing pipeline
# ---------------------------
def preprocess_pipeline(
    contents: bytes,
    filename: str,
    timestamp_col: Optional[str] = None,
    timezone_from: Optional[str] = None,
    to_utc: bool = True,
    resample_freq: str = "1T",
    resample_how: str = "mean"
):

    df = load_file(contents, filename)
    df = normalize_timestamps(df, timestamp_col, timezone_from, to_utc)

    # Align to 1-minute frequency
    df = resample_df(df, resample_freq, resample_how)

    # Handle missing values AFTER resampling
    df = handle_missing(df)

    out_csv = df.reset_index().to_csv(index=False)
    return df, out_csv
