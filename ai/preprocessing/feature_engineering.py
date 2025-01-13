import pandas as pd
import numpy as np

def calculate_price_volatility(prices, window=10):
    """
    Calculate price volatility over a sliding window.

    Args:
        prices (pd.Series): Token price data.
        window (int): Number of periods for the sliding window.

    Returns:
        pd.Series: Volatility values.
    """
    return prices.rolling(window=window).std()

def holder_concentration_score(top_holders):
    """
    Calculate a score based on the concentration of token holders.

    Args:
        top_holders (dict): Distribution of top holders (%).

    Returns:
        float: Risk score (0 = low risk, 10 = high risk).
    """
    top_1 = top_holders.get("top_1", 0)
    top_10 = top_holders.get("top_10", 0)
    return min(10, (top_1 * 0.7 + top_10 * 0.3) / 10)
