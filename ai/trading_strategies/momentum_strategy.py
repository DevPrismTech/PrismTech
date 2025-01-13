import pandas as pd

def momentum_strategy(prices, window=14):
    """
    Calculate momentum indicator and return a buy/sell signal.

    Args:
        prices (pd.Series): Series of token prices.
        window (int): Lookback period for momentum calculation.

    Returns:
        dict: Momentum value and action (Buy/Sell).
    """
    momentum = prices.diff(window).iloc[-1]
    action = "Buy" if momentum > 0 else "Sell"
    return {"momentum": momentum, "action": action}

def apply_strategy(prices):
    """
    Apply the momentum strategy on price data.

    Args:
        prices (pd.DataFrame): DataFrame with token price history.

    Returns:
        pd.DataFrame: DataFrame with signals appended.
    """
    prices['Momentum'] = prices['Close'].diff(14)
    prices['Signal'] = prices['Momentum'].apply(lambda x: "Buy" if x > 0 else "Sell")
    return prices
