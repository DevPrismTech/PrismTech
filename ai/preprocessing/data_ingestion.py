import requests

def fetch_token_data(symbols, vs_currency="usd"):
    """
    Fetch token data from CoinGecko API.

    Args:
        symbols (list): List of token symbols.
        vs_currency (str): The currency to compare against (default: USD).

    Returns:
        dict: Token data including price, volume, market cap.
    """
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": ",".join(symbols),
        "vs_currencies": vs_currency,
        "include_market_cap": "true",
        "include_24hr_vol": "true",
    }
    response = requests.get(url, params=params)
    return response.json()

def fetch_wallet_data(wallet_address):
    """
    Fetch transaction data for a specific wallet.

    Args:
        wallet_address (str): The wallet address.

    Returns:
        dict: Wallet transaction history and balances.
    """
    url = f"https://api.solscan.io/account/{wallet_address}"
    response = requests.get(url)
    return response.json()
