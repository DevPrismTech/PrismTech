def liquidity_ratio(volume, liquidity):
    """Calculate liquidity ratio to evaluate token health."""
    if liquidity == 0:
        return None
    return volume / liquidity

def holder_distribution_score(top_1, top_10):
    """Score the distribution of token holders."""
    if top_1 > 50:
        return "High Risk"
    elif top_10 > 80:
        return "Moderate Risk"
    else:
        return "Low Risk"
