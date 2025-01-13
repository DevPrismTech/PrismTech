from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

def train_risk_model(data):
    """
    Train a model to predict token risk scores based on features.

    Args:
        data (pd.DataFrame): Dataset with token features and risk labels.

    Returns:
        model: Trained RandomForestClassifier model.
    """
    X = data.drop("risk_score", axis=1)
    y = data["risk_score"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    accuracy = model.score(X_test, y_test)
    print(f"Model Accuracy: {accuracy * 100:.2f}%")
    return model
