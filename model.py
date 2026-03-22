# model.py - US Predictive Supply Chain Risk Mapper

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# ---------- Example function: train a predictive model ----------
def train_risk_model(data: pd.DataFrame, target_column: str):
    """
    Train a RandomForest model to predict supply chain risk.
    Returns trained model and feature scaler.
    """
    X = data.drop(columns=[target_column])
    y = data[target_column]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
    
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    score = model.score(X_test, y_test)
    print(f"Model trained. Accuracy on test set: {score:.2f}")
    
    return model, scaler

# ---------- Example function: predict risk ----------
def predict_risk(model, scaler, new_data: pd.DataFrame):
    """
    Predict supply chain risk on new data using the trained model.
    """
    X_scaled = scaler.transform(new_data)
    predictions = model.predict(X_scaled)
    return predictions

# ---------- Placeholder usage ----------
if __name__ == "__main__":
    print("This is the model module for US Predictive Supply Chain Risk Mapper.")
    print("Use train_risk_model() to train models and predict_risk() for predictions.")
