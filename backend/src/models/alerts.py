from pydantic import BaseModel

class Alert(BaseModel):
    token: str
    price_change: float
    liquidity_change: float
