import joblib
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier

def train_model(X, y, task="regression", save_path="model.pkl"):
    """Train a regression or classification model with hyperparameter tuning."""
    if task == "regression":
        model = RandomForestRegressor(random_state=42)
        param_grid = {"n_estimators": [50, 100, 200], "max_depth": [None, 10, 20]}
    elif task == "classification":
        model = RandomForestClassifier(random_state=42)
        param_grid = {"n_estimators": [50, 100, 200], "max_depth": [None, 10, 20]}
    else:
        raise ValueError("Task must be 'regression' or 'classification'")

    grid_search = GridSearchCV(model, param_grid, cv=5, scoring="accuracy" if task == "classification" else "neg_mean_squared_error")
    grid_search.fit(X, y)
    best_model = grid_search.best_estimator_

    # Save the model
    joblib.dump(best_model, save_path)
    print(f"Model saved to {save_path}")
    return best_model
