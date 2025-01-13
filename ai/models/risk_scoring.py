def calculate_risk_score(data):
    """
    Calculate a token's risk score based on multiple factors.

    Args:
        data (dict): Token data including liquidity, volume, holders, etc.

    Returns:
        float: Risk score (0 = low risk, 10 = high risk).
    """
    liquidity = data.get("liquidity", 0)
    volume = data.get("volume", 0)
    holders = data.get("holders", {})
    volatility = data.get("volatility", 0)

    def holder_concentration_score(holders):
        """Calculate a score based on the concentration of token holders."""
        top_1 = holders.get("top_1", 0)
        top_10 = holders.get("top_10", 0)
        return min(10, (top_1 * 0.7 + top_10 * 0.3) / 10)

    holder_score = holder_concentration_score(holders)
    liquidity_ratio = volume / liquidity if liquidity > 0 else 0

    # Weighted scoring
    score = (volatility * 0.4) + (holder_score * 0.4) + (liquidity_ratio * 0.2)
    return min(10, max(0, score))
