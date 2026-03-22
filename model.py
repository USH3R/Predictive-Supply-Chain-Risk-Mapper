# model.py - Predictive ML/AI for Supply Chain Risk

import pandas as pd
import numpy as np

# ------------------------------
# Example placeholder predictive model
# ------------------------------
def predict_risk(df: pd.DataFrame) -> pd.DataFrame:
    """
    Predicts risk scores for supply chain entries in df.

    Parameters:
        df (pd.DataFrame): DataFrame containing supply chain data with at least
                           columns ['vendor', 'region', 'metric1', 'metric2', ...]

    Returns:
        pd.DataFrame: Original DataFrame with an additional 'risk' column.
    """
    df = df.copy()
    
    # Placeholder: generate random risk score if no real model yet
    if 'risk' not in df.columns:
        np.random.seed(42)  # For reproducibility
        df['risk'] = np.random.uniform(0, 10, size=len(df))
    
    # TODO: Replace the above with your real ML/AI predictive model
    # e.g., trained scikit-learn or XGBoost model: model.predict(df_features)

    return df

# ------------------------------
# Example utility function
# ------------------------------
def risk_summary(df: pd.DataFrame) -> dict:
    """
    Returns a summary of predicted risk.
    
    Parameters:
        df (pd.DataFrame): DataFrame containing 'risk' column.
    
    Returns:
        dict: Summary stats like mean, max, high-risk count, etc.
    """
    summary = {
        "average_risk": df['risk'].mean() if 'risk' in df else None,
        "max_risk": df['risk'].max() if 'risk' in df else None,
        "high_risk_count": df[df['risk'] >= 8].shape[0] if 'risk' in df else 0
    }
    return summary
