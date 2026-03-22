# model.py - Predictive modeling for US Supply Chain Risk Mapper
# Provides risk predictions based on supply chain data

import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import numpy as np

# ---------- Placeholder Model ----------
class SupplyChainRiskModel:
    def __init__(self):
        # Initialize a simple Random Forest model
        # For placeholder purposes, it is not trained on real data yet
        self.model = RandomForestRegressor(n_estimators=10, random_state=42)
        self.trained = False

    def train(self, df: pd.DataFrame):
        """
        Train the model on existing supply chain data.
        Expects a DataFrame with numeric features and a 'Risk Score' column.
        """
        if 'Risk Score' not in df.columns:
            raise ValueError("DataFrame must include 'Risk Score' column for training.")

        # Example: numeric features only
        features = df.select_dtypes(include=np.number).drop(columns=['Risk Score'], errors='ignore')
        if features.empty:
            print("No numeric features to train on. Skipping training.")
            return

        target = df['Risk Score']
        self.model.fit(features, target)
        self.trained = True
        print("Model trained on placeholder data.")

    def predict(self, df: pd.DataFrame) -> pd.Series:
        """
        Predict risk scores for given supply chain data.
        Returns a pandas Series of predicted scores.
        """
        features = df.select_dtypes(include=np.number)
        if features.empty or not self.trained:
            # If model is not trained or no numeric features, return placeholder predictions
            print("Returning placeholder risk scores.")
            return pd.Series([0.5] * len(df), index=df.index)
        return pd.Series(self.model.predict(features), index=df.index)# model.py - US Predictive Supply Chain Risk Mapper

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
