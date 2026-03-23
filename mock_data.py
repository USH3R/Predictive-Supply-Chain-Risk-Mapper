# mock_data.py - Simulated multi-source supply chain data
# Supports SQL, API, and Neo4j mock inputs

import pandas as pd

def get_sql_data():
    """Simulate SQL data fetch"""
    data = {
        'vendor': ['A', 'B', 'C'],
        'region': ['North', 'South', 'West'],
        'delivery_time': [5, 8, 3],
        'cost': [100, 200, 150],
        'other_metric': [0.1, 0.2, 0.3]
    }
    df = pd.DataFrame(data)
    return df

def get_api_data():
    """Simulate API data fetch"""
    data = {
        'vendor': ['D', 'E'],
        'region': ['East', 'Central'],
        'delivery_time': [7, 6],
        'cost': [180, 220],
        'other_metric': [0.15, 0.25]
    }
    df = pd.DataFrame(data)
    return df

def get_neo4j_data():
    """Simulate Neo4j graph-based data fetch"""
    data = {
        'vendor': ['F'],
        'region': ['NorthEast'],
        'delivery_time': [4],
        'cost': [130],
        'other_metric': [0.12]
    }
    df = pd.DataFrame(data)
    return df

def get_mock_data():
    """Combine all mock sources into one DataFrame"""
    sql_df = get_sql_data()
    api_df = get_api_data()
    neo_df = get_neo4j_data()
    
    combined_df = pd.concat([sql_df, api_df, neo_df], ignore_index=True)
    return combined_df
