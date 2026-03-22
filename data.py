# data.py - US Predictive Supply Chain Risk Mapper
# Provides modular access to supply chain data from SQL, Neo4j, API, or mock data

import pandas as pd
import random

# Optional: import SQL and Neo4j clients if needed
# import sqlalchemy
# from neo4j import GraphDatabase
# import requests

def get_supply_data(source='mock'):
    """
    Fetch supply chain data from the specified source.
    Returns a pandas DataFrame with columns suitable for predict_risk().
    
    source: 'mock', 'sql', 'neo4j', 'api'
    """
    if source == 'mock':
        return _get_mock_data()
    elif source == 'sql':
        return _get_sql_data()
    elif source == 'neo4j':
        return _get_neo4j_data()
    elif source == 'api':
        return _get_api_data()
    else:
        raise ValueError(f"Unknown data source: {source}")

# -------------------------
# Internal helper functions
# -------------------------

def _get_mock_data():
    """Return a simple mock DataFrame for immediate testing"""
    vendors = ['Vendor A', 'Vendor B', 'Vendor C']
    regions = ['North', 'South', 'East', 'West']
    
    data = []
    for vendor in vendors:
        for region in regions:
            data.append({
                'vendor': vendor,
                'region': region,
                'delivery_days': random.randint(1, 20),
                'cost': random.randint(1000, 5000)
            })
    df = pd.DataFrame(data)
    return df

def _get_sql_data():
    """Placeholder: simulate SQL data fetch"""
    # Example:
    # engine = sqlalchemy.create_engine('postgresql://user:pass@host/db')
    # df = pd.read_sql("SELECT vendor, region, delivery_days, cost FROM supply_table", engine)
    df = _get_mock_data()  # Temporary fallback
    return df

def _get_neo4j_data():
    """Placeholder: simulate Neo4j graph database fetch"""
    # Example:
    # driver = GraphDatabase.driver("bolt://localhost:7687", auth=("user", "pass"))
    # query = "MATCH (v:Vendor)-[r:SUPPLIES]->(p:Product) RETURN v.name, p.region, r.delivery_days, r.cost"
    # df = run_query(driver, query)
    df = _get_mock_data()  # Temporary fallback
    return df

def _get_api_data():
    """Placeholder: simulate fetching from an API"""
    # Example:
    # response = requests.get("https://api.supplychain.com/data")
    # df = pd.DataFrame(response.json())
    df = _get_mock_data()  # Temporary fallback
    return df# data.py - US Predictive Supply Chain Risk Mapper
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
