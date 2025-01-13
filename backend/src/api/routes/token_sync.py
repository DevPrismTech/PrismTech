from fastapi import APIRouter
from src.services.sync_service import fetch_tokens_from_pumpfun

router = APIRouter()

@router.get("/sync-tokens")
async def sync_tokens():
    """
    Fetch and sync tokens from Pump.fun
    """
    tokens = fetch_tokens_from_pumpfun()
    if tokens:
        return {"status": "success", "tokens": tokens}
    else:
        return {"status": "error", "message": "Failed to fetch tokens"}
