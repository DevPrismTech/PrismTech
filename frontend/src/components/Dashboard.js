import React, { useState, useEffect } from "react";

const Dashboard = () => {
  const [tokens, setTokens] = useState([]);
  const [loading, setLoading] = useState(true);

  // Fonction pour récupérer les données depuis l'API
  const fetchTokenData = async () => {
    try {
      const response = await fetch("http://localhost:8000/api/tokens"); // Appelle ton backend ou une API externe
      const data = await response.json();
      setTokens(data); // Met à jour les données du tableau
      setLoading(false);
    } catch (error) {
      console.error("Error fetching token data:", error);
    }
  };

  // Récupération des données à intervalle régulier
  useEffect(() => {
    fetchTokenData(); // Appelle l'API une fois au chargement
    const interval = setInterval(fetchTokenData, 5000); // Mets à jour toutes les 5 secondes
    return () => clearInterval(interval); // Nettoie l'intervalle quand le composant est démonté
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
