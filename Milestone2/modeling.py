from prophet import Prophet
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

def prophet_model(df):
    model = Prophet(daily_seasonality=True)
    model.fit(df)
    future = model.make_future_dataframe(periods=30)
    return model.predict(future)
