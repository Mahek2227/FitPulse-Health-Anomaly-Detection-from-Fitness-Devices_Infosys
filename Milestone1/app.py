import streamlit as st
import pandas as pd
import io
from preprocess import preprocess_pipeline

st.set_page_config(page_title="FitPulse Anamoly Detection", layout="centered")

st.title("FitPulse Anamoly Detection: Data Collection & Preprocessing")

uploaded = st.file_uploader("Upload CSV or JSON file", type=["csv", "json"])

if uploaded:
    bytes_data = uploaded.read()

    st.success(f"Loaded file: {uploaded.name}")

    # Try showing a raw preview
    try:
        raw_df = pd.read_csv(io.BytesIO(bytes_data))
    except:
        try:
            raw_df = pd.read_json(io.BytesIO(bytes_data), lines=True)
        except:
            raw_df = None

    if raw_df is not None:
        st.subheader("Raw preview (first 5 rows)")
        st.dataframe(raw_df.head())

    st.sidebar.header("Preprocessing Options")

    timestamp_col = st.sidebar.text_input(
        "Timestamp column (leave blank to auto-detect)"
    )

    timezone_from = st.sidebar.text_input(
        "Source timezone (e.g. 'Asia/Kolkata')"
    )

    if st.button("Run preprocessing"):
        try:
            df_processed, out_csv = preprocess_pipeline(
                contents=bytes_data,
                filename=uploaded.name,
                timestamp_col=timestamp_col or None,
                timezone_from=timezone_from or None,
                to_utc=True,
                
                resample_freq="1T",
                resample_how="mean"
            )

            st.success("Preprocessing completed successfully")
            st.subheader("Processed preview (first 10 rows)")
            st.dataframe(df_processed.head(10))

            st.download_button(
                label="Download Cleaned CSV",
                data=out_csv,
                file_name=f"cleaned_{uploaded.name}",
                mime="text/csv"
            )

        except Exception as e:
            st.error("Preprocessing failed")
            st.warning(str(e))
            st.stop()

else:
    st.info("Upload a CSV or JSON file to begin.")