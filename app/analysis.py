import pandas as pd
from app.utils import calculate_z_scores, calculate_vwap

def analyze_orderbook(df: pd.DataFrame, order_type: str):
    anomalies = {}

    z_scores = calculate_z_scores(df, 'volume')
    anomalies["volume_anomalies"] = df[abs(z_scores) > 3].to_dict(orient="records")

    vwap = calculate_vwap(df)
    anomalies["price_anomalies"] = df[(abs(df['price'] - vwap) / vwap) > 0.05].to_dict(orient="records") if vwap != 0 else []

    local_spikes = df[(df['volume'].shift(-1) * 5 < df['volume']) & (df['volume'].shift(1) * 5 < df['volume'])]
    anomalies["local_spikes"] = local_spikes.to_dict(orient="records")

    boundary_size = max(int(len(df) * 0.05), 1)
    boundary_anomalies = pd.concat([df.iloc[:boundary_size], df.iloc[-boundary_size:]])
    anomalies["boundary_anomalies"] = boundary_anomalies.to_dict(orient="records")

    return anomalies
