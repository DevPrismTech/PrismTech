const API_URL = "http://127.0.0.1:8000";

export const fetchAlerts = async () => {
  const response = await fetch(`${API_URL}/alerts`);
  return await response.json();
};
