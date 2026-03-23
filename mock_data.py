# data.py - US Predictive Supply Chain Risk Mapper
# Provides mock or real supply chain data for the app

import pandas as pd

def get_supply_data():
    """
    Returns a DataFrame with mock supply chain data
    suitable for predict_risk() and Dash visualization.
    Columns included:
        - vendor: vendor name
        - region: geographical region
        - delivery_time: delivery time in days
        - cost: total cost in USD
        - other_metric: example additional metric
    """
    data = {
        'vendor': ['A', 'B', 'C', 'D', 'E'],
        'region': ['North', 'South', 'West', 'East', 'Central'],
        'delivery_time': [5, 8, 3, 6, 7],
        'cost': [100, 200, 150, 180, 220],
        'other_metric': [0.1, 0.2, 0.3, 0.25, 0.15]
    }
    
    df = pd.DataFrame(data)
    return df
