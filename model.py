# model.py - US Predictive Supply Chain Risk Mapper

import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

# ---------- Build a sample predictive model ----------
def build_risk_model():
    """
    Build a placeholder Random Forest model pipeline.
    Replace with real features and model tuning later.
    """
    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('model', RandomForestRegressor(n_estimators=100, random_state=42))
    ])
    return pipeline

# ---------- Fit the model ----------
def train_model(data: pd.DataFrame, feature_cols: list, target_col: str):
    """
    Train the risk prediction model.
    """
    model = build_risk_model()
    X = data[feature_cols]
    y = data[target_col]
    
    model.fit(X, y)
    print("Model training complete.")
    return model

# ---------- Predict risk ----------
def predict_risk(model, new_data: pd.DataFrame, feature_cols: list):
    """
    Predict risk scores using the trained model.
    """
    predictions = model.predict(new_data[feature_cols])
    new_data['Predicted Risk'] = predictions
    return new_data

# ---------- Test with dummy data ----------
if __name__ == "__main__":
    # Example dummy dataset
    df = pd.DataFrame({
        'Feature1': [1, 2, 3],
        'Feature2': [0.1, 0.2, 0.3],
        'Risk Score': [0.2, 0.5, 0.7]
    })
    features = ['Feature1', 'Feature2']
    target = 'Risk Score'
    
    model = train_model(df, features, target)
    predictions = predict_risk(model, df, features)
    print(predictions)
