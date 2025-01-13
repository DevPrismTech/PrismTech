class PrismAgent:
    def __init__(self, wallet_address, slippage, max_risk_score):
        """
        Initialize the Prism agent with custom settings.

        Args:
            wallet_address (str): Wallet address linked to the agent.
            slippage (float): Maximum slippage tolerance for trades.
            max_risk_score (float): Maximum allowable risk score for tokens.
        """
        self.wallet_address = wallet_address
        self.slippage = slippage
        self.max_risk_score = max_risk_score
        self.rules = []

    def add_rule(self, condition, action):
        """
        Add a custom rule for the agent.

        Args:
            condition (str): Rule condition (e.g., "volume > 200k").
            action (str): Action to perform if the condition is met.
        """
        self.rules.append({"condition": condition, "action": action})

    def execute(self, market_data):
        """
        Execute the agent's rules on the provided market data.

        Args:
            market_data (dict): Real-time market data.
        """
        for rule in self.rules:
            if eval(rule["condition"], {}, market_data):
                print(f"Executing action: {rule['action']}")

    def show_config(self):
        """Display the agent's configuration."""
        return {
            "wallet_address": self.wallet_address,
            "slippage": self.slippage,
            "max_risk_score": self.max_risk_score,
            "rules": self.rules
        }
