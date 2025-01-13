import pandas as pd
import numpy as np

def clean_data(data):
    """Clean raw data by removing NaN and outliers."""
    data = data.dropna()
    data = data[data['volume'] > 0]  # Remove zero-volume entries
    return data

def detect_outliers(data, column, threshold=3):
    """Detect and replace outliers using Z-score."""
    mean = data[column].mean()
    std = data[column].std()
    z_scores = (data[column] - mean) / std
    outliers = z_scores.abs() > threshold
    data.loc[outliers, column] = np.nan  # Replace outliers with NaN
    return data
