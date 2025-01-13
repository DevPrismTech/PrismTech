def detect_scam(contract_data):
    """
    Detect potential scams based on contract metadata.

    Args:
        contract_data (dict): Contract details including renouncement and holder distribution.

    Returns:
        dict: Scam detection analysis with risk level.
    """
    renounced = contract_data.get("renounced", False)
    holders = contract_data.get("holders", {})
    bot_activity = contract_data.get("bot_activity", False)

    def holder_concentration_score(holders):
        """Calculate a score based on holder concentration."""
        top_1 = holders.get("top_1", 0)
        top_10 = holders.get("top_10", 0)
        return min(10, (top_1 * 0.7 + top_10 * 0.3) / 10)

    holder_score = holder_concentration_score(holders)
    risk_level = "High" if holder_score > 7 or bot_activity else "Low"
    return {
        "renounced": renounced,
        "holder_score": holder_score,
        "risk_level": risk_level
    }
