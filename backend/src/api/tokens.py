from fastapi import APIRouter
import requests

router = APIRouter()

@router.get("/tokens")
def get_tokens():
    try:
        # Fetch data from CoinGecko
        response = requests.get("https://api.coingecko.com/api/v3/coins/markets", params={
            "vs_currency": "usd",
            "order": "market_cap_desc",
            "per_page": 5,
            "page": 1,
        })
        data = response.json()

        # Extract relevant token data
        tokens = [
            {
                "symbol": token["symbol"].upper(),
                "price": token["current_price"],
                "market_cap": token["market_cap"],
                "price_change": token["price_change_percentage_24h"],
            }
            for token in data
        ]

        return tokens
    except Exception as e:
        return {"error": str(e)}
