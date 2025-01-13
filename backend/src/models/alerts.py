from pydantic import BaseModel, Field, root_validator
from typing import Optional

class Alert(BaseModel):
    token: str = Field(..., description="Token symbol or address, e.g., 'SOL'")
    price_change: float = Field(..., gt=-100, lt=100, description="Percentage change in price (-100% to 100%)")
    liquidity_change: float = Field(..., ge=0, description="Change in liquidity (must be positive or zero)")
    category: str = Field(..., description="Type of alert, e.g., 'Price Spike', 'Liquidity Drop'")
    risk_score: Optional[float] = Field(None, ge=0, le=10, description="AI-assigned risk score (0 to 10)")
    timestamp: Optional[str] = Field(None, description="Timestamp of the alert in ISO 8601 format")
    message: Optional[str] = Field(None, description="Detailed explanation of the alert")

    @root_validator
    def validate_alert(cls, values):
        price_change = values.get("price_change")
        liquidity_change = values.get("liquidity_change")
        if abs(price_change) < 1 and liquidity_change < 1000:
            raise ValueError("The alert is not significant enough to trigger.")
        return values

    def is_high_risk(self) -> bool:
        """
        Determine if the alert qualifies as high risk based on price and liquidity changes.
        """
        return self.price_change > 50 or self.liquidity_change < 10000

    def format_message(self) -> str:
        """
        Generate a user-friendly alert message.
        """
        return (
            f"🚨 Alert for {self.token} 🚨\n"
            f"- Price Change: {self.price_change}%\n"
            f"- Liquidity Change: ${self.liquidity_change}\n"
            f"- Risk Score: {self.risk_score or 'N/A'}\n"
            f"- Category: {self.category}\n"
            f"- Timestamp: {self.timestamp or 'N/A'}\n"
        )
