import pandas as pd

def calculate_z_scores(df: pd.DataFrame, column: str) -> pd.Series:
    mean, std = df[column].mean(), df[column].std()
    return pd.Series([0] * len(df), index=df.index) if std == 0 else (df[column] - mean) / std

def calculate_vwap(df: pd.DataFrame) -> float:
    total_volume = df['volume'].sum()
    return (df['price'] * df['volume']).sum() / total_volume if total_volume != 0 else 0
