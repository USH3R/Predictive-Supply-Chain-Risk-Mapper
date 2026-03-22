# model.py
# Predictive model placeholder for US Predictive Supply Chain Risk Mapper

from sklearn.ensemble import RandomForestRegressor
import pandas as pd

# ----------------------------
# Train dummy model
# ----------------------------
def train_model(df, features, target):
    """
    Train a dummy model (RandomForest placeholder)
    """
    model = RandomForestRegressor(n_estimators=10, random_state=42)
    model.fit(df[features], df[target])
    return model

# ----------------------------
# Predict risk
# ----------------------------
def predict_risk(df):
    """
    Adds a 'predicted_risk' column.
    Currently a placeholder: copies risk_score.
    """
    df['predicted_risk'] = df['risk_score']  # placeholder
    return df
