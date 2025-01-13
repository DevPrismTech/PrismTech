import requests

def fetch_tokens_from_pumpfun():
    """
    Fetch token data from Pump.fun API (or other platform)
    """
    url = "https://api.pump.fun/tokens/latest"  # Exemple d'API
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data  # Tu peux aussi enregistrer dans la base de données ici
        else:
            print(f"Error fetching tokens: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error: {str(e)}")
        return None
