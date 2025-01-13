import React, { useState, useEffect } from "react";

const Dashboard = () => {
  const [tokens, setTokens] = useState([]);
  const [loading, setLoading] = useState(true);

  // Function to fetch real-time token data
  const fetchTokenData = async () => {
    try {
      const response = await fetch("http://localhost:8000/api/tokens"); // Connects to backend API
      const data = await response.json();
      setTokens(data); // Update the token list
      setLoading(false);
    } catch (error) {
      console.error("Error fetching token data:", error);
    }
  };

  // Fetch data on load and update every 5 seconds
  useEffect(() => {
    fetchTokenData(); // Fetch data initially
    const interval = setInterval(fetchTokenData, 5000); // Refresh data every 5 seconds
    return () => clearInterval(interval); // Clean up interval on unmount
  }, []);

  return (
    <div>
      <h1>PrismTech Dashboard</h1>
      {loading ? (
        <p>Loading...</p>
      ) : (
        <div>
          {tokens.map((token, index) => (
            <div key={index}>
              <p>
                {token.symbol}: ${token.price} | Market Cap: ${token.market_cap}
              </p>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default Dashboard;
