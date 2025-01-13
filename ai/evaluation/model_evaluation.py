from sklearn.metrics import (
    mean_squared_error, mean_absolute_error, r2_score,
    accuracy_score, precision_score, recall_score, f1_score
)
import numpy as np

def regression_metrics(y_true, y_pred):
    """Evaluate regression models with multiple metrics."""
    mse = mean_squared_error(y_true, y_pred)
    mae = mean_absolute_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)
    return {
        "Mean Squared Error": mse,
        "Mean Absolute Error": mae,
        "R2 Score": r2
    }

def classification_metrics(y_true, y_pred):
    """Evaluate classification models with precision, recall, F1."""
    accuracy = accuracy_score(y_true, y_pred)
    precision = precision_score(y_true, y_pred, average='weighted')
    recall = recall_score(y_true, y_pred, average='weighted')
    f1 = f1_score(y_true, y_pred, average='weighted')
    return {
        "Accuracy": accuracy,
        "Precision": precision,
        "Recall": recall,
        "F1 Score": f1
    }

def evaluate_model(model, X_test, y_test, task="regression"):
    """General model evaluation function for regression or classification."""
    predictions = model.predict(X_test)
    if task == "regression":
        return regression_metrics(y_test, predictions)
    elif task == "classification":
        return classification_metrics(y_test, predictions)
    else:
        raise ValueError("Task must be 'regression' or 'classification'")
