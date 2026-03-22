# data.py - US Predictive Supply Chain Risk Mapper
# Modular data pipeline: SQL, Neo4j, API
# Returns DataFrame ready for predict_risk()

import pandas as pd
import numpy as np

def get_supply_data():
    """
    Returns mock supply chain data for vendors, regions, and delivery metrics.
    Replace with real SQL / Neo4j / API calls as needed.
    """
    # Mock vendor list
    vendors = ['Vendor A', 'Vendor B', 'Vendor C', 'Vendor D']
    regions = ['East', 'West', 'South', 'North']
    
    # Simulate data
    data = {
        'vendor': np.random.choice(vendors, 20),
        'region': np.random.choice(regions, 20),
        'delivery_days': np.random.randint(1, 20, 20),
        'issues_reported': np.random.randint(0, 10, 20)
    }
    
    df = pd.DataFrame(data)
    return df
