# model.py - US Predictive Supply Chain Risk Mapper
# Modular predictive model
# Computes risk_score for given DataFrame

import pandas as pd
import numpy as np

def predict_risk(df: pd.DataFrame) -> pd.DataFrame:
    """
    Adds a 'risk_score' column to df based on delivery_days and issues_reported.
    """
    # Simple mock formula: normalized delivery_days + issues
    df['risk_score'] = (df['delivery_days'] / df['delivery_days'].max() +
                        df['issues_reported'] / df['issues_reported'].max()) / 2
    return df
