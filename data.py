# data.py - US Predictive Supply Chain Risk Mapper
# Modular interface for supply chain data

import pandas as pd
try:
    from mock_data import get_mock_data
except ImportError:
    get_mock_data = None

def get_supply_data(use_mock=True) -> pd.DataFrame:
    """
    Returns supply chain data from multiple sources.
    - use_mock: if True, return simulated data from mock_data.py
    """
    if use_mock and get_mock_data is not None:
        return get_mock_data()
    
    # Placeholder for SQL data
    sql_df = get_sql_data()
    # Placeholder for Neo4j data
    neo4j_df = get_neo4j_data()
    # Placeholder for API data
    api_df = get_api_data()

    # Combine all sources
    combined_df = pd.concat([sql_df, neo4j_df, api_df], ignore_index=True)
    return combined_df

def get_sql_data() -> pd.DataFrame:
    # Placeholder: return empty DataFrame
    return pd.DataFrame(columns=['vendor', 'region', 'supply_quantity', 'delivery_delay_days'])

def get_neo4j_data() -> pd.DataFrame:
    # Placeholder: return empty DataFrame
    return pd.DataFrame(columns=['vendor', 'region', 'supply_quantity', 'delivery_delay_days'])

def get_api_data() -> pd.DataFrame:
    # Placeholder: return empty DataFrame
    return pd.DataFrame(columns=['vendor', 'region', 'supply_quantity', 'delivery_delay_days'])# data.py - Modular data interface for US Predictive Supply Chain Risk Mapper
import pandas as pd

try:
    from mock_data import get_mock_data
    USE_MOCK = True
except ImportError:
    USE_MOCK = False

def get_supply_data(source="real"):
    """
    Returns supply chain data as DataFrame.
    If mock_data.py exists, it will be used for testing.
    """
    if USE_MOCK or source == "mock":
        return get_mock_data()
    
    # Placeholder for real SQL / Neo4j / API integration
    # Example:
    # df_sql = pd.read_sql("SELECT * FROM supply_table", connection)
    # df_neo4j = run_cypher_query(...).to_dataframe()
    # df_api = pd.json_normalize(requests.get(api_url).json())
    
    return pd.DataFrame()  # Empty placeholder for real data# data.py - Handles supply chain data (SQL, Neo4j, API, or mock)

import pandas as pd
import numpy as np

def get_supply_data(source: str = "mock") -> pd.DataFrame:
    """
    Returns a DataFrame ready for predict_risk().

    Parameters:
        source (str): "mock", "sql", "neo4j", "api" (default="mock")

    Returns:
        pd.DataFrame: supply chain data with columns ['vendor', 'region', 'metric1', 'metric2', ...]
    """
    if source == "mock":
        # Generate mock data for testing
        np.random.seed(42)
        df = pd.DataFrame({
            "vendor": [f"Vendor {i}" for i in range(1, 11)],
            "region": np.random.choice(["North", "South", "East", "West"], size=10),
            "metric1": np.random.uniform(0, 100, size=10),
            "metric2": np.random.uniform(0, 50, size=10)
        })
    elif source == "sql":
        # TODO: Connect to SQL and fetch data
        df = pd.DataFrame()  # placeholder
    elif source == "neo4j":
        # TODO: Connect to Neo4j and fetch data
        df = pd.DataFrame()  # placeholder
    elif source == "api":
        # TODO: Call APIs and fetch data
        df = pd.DataFrame()  # placeholder
    else:
        raise ValueError("Invalid data source. Choose 'mock', 'sql', 'neo4j', or 'api'.")

    return df# data.py - US Predictive Supply Chain Risk Mapper
# Added modular interface for fetching supply chain data from SQL, Neo4j, and APIs

import pandas as pd
from sqlalchemy import create_engine
from neo4j import GraphDatabase
import requests

# ------------------------------
# SQL Configuration
# ------------------------------
SQL_URI = "postgresql://username:password@host:port/database"
SQL_TABLE = "supply_chain_data"

# ------------------------------
# Neo4j Configuration
# ------------------------------
NEO4J_URI = "neo4j://localhost:7687"
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "password"

# ------------------------------
# API Configuration
# ------------------------------
API_URL = "https://api.supplychain.example.com/data"
API_KEY = "your_api_key_here"

# ------------------------------
# Main function for app.py
# ------------------------------
def get_supply_data(vendor=None, region=None, source="sql"):
    """
    Fetch supply chain data from the selected source and return as a Pandas DataFrame.

    Parameters:
        vendor (str, optional): Filter by vendor name.
        region (str, optional): Filter by region name.
        source (str): "sql", "neo4j", or "api".

    Returns:
        pd.DataFrame: DataFrame containing the requested supply chain data.
    """
    if source.lower() == "sql":
        return _get_sql_data(vendor, region)
    elif source.lower() == "neo4j":
        return _get_neo4j_data(vendor, region)
    elif source.lower() == "api":
        return _get_api_data(vendor, region)
    else:
        raise ValueError("Invalid data source. Choose 'sql', 'neo4j', or 'api'.")

# ------------------------------
# Internal helper functions
# ------------------------------
def _get_sql_data(vendor=None, region=None):
    """Fetch data from SQL database."""
    engine = create_engine(SQL_URI)
    query = f"SELECT * FROM {SQL_TABLE}"
    filters = []
    if vendor:
        filters.append(f"vendor = '{vendor}'")
    if region:
        filters.append(f"region = '{region}'")
    if filters:
        query += " WHERE " + " AND ".join(filters)
    df = pd.read_sql(query, engine)
    return df

def _get_neo4j_data(vendor=None, region=None):
    """Fetch data from Neo4j graph database."""
    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
    with driver.session() as session:
        cypher = "MATCH (s:SupplyChain) RETURN s.vendor AS vendor, s.region AS region, s.risk AS risk"
        if vendor or region:
            conditions = []
            if vendor:
                conditions.append(f"s.vendor = '{vendor}'")
            if region:
                conditions.append(f"s.region = '{region}'")
            cypher += " WHERE " + " AND ".join(conditions)
        result = session.run(cypher)
        records = [record.data() for record in result]
    driver.close()
    return pd.DataFrame(records)

def _get_api_data(vendor=None, region=None):
    """Fetch data from an external API."""
    params = {"vendor": vendor, "region": region, "api_key": API_KEY}
    response = requests.get(API_URL, params=params)
    response.raise_for_status()
    data = response.json()
    return pd.DataFrame(data)# data.py - US Predictive Supply Chain Risk Mapper
# Added modular interface for fetching supply chain data from SQL, Neo4j, and APIs

import pandas as pd
from sqlalchemy import create_engine
from neo4j import GraphDatabase
import requests

# ------------------------------
# SQL Configuration
# ------------------------------
SQL_URI = "postgresql://username:password@host:port/database"
SQL_TABLE = "supply_chain_data"

# ------------------------------
# Neo4j Configuration
# ------------------------------
NEO4J_URI = "neo4j://localhost:7687"
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "password"

# ------------------------------
# API Configuration
# ------------------------------
API_URL = "https://api.supplychain.example.com/data"
API_KEY = "your_api_key_here"

# ------------------------------
# Main function for app.py
# ------------------------------
def get_supply_data(vendor=None, region=None, source="sql"):
    """
    Fetch supply chain data from the selected source and return as a Pandas DataFrame.

    Parameters:
        vendor (str, optional): Filter by vendor name.
        region (str, optional): Filter by region name.
        source (str): "sql", "neo4j", or "api".

    Returns:
        pd.DataFrame: DataFrame containing the requested supply chain data.
    """
    if source.lower() == "sql":
        return _get_sql_data(vendor, region)
    elif source.lower() == "neo4j":
        return _get_neo4j_data(vendor, region)
    elif source.lower() == "api":
        return _get_api_data(vendor, region)
    else:
        raise ValueError("Invalid data source. Choose 'sql', 'neo4j', or 'api'.")

# ------------------------------
# Internal helper functions
# ------------------------------
def _get_sql_data(vendor=None, region=None):
    """Fetch data from SQL database."""
    engine = create_engine(SQL_URI)
    query = f"SELECT * FROM {SQL_TABLE}"
    filters = []
    if vendor:
        filters.append(f"vendor = '{vendor}'")
    if region:
        filters.append(f"region = '{region}'")
    if filters:
        query += " WHERE " + " AND ".join(filters)
    df = pd.read_sql(query, engine)
    return df

def _get_neo4j_data(vendor=None, region=None):
    """Fetch data from Neo4j graph database."""
    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
    with driver.session() as session:
        cypher = "MATCH (s:SupplyChain) RETURN s.vendor AS vendor, s.region AS region, s.risk AS risk"
        if vendor or region:
            conditions = []
            if vendor:
                conditions.append(f"s.vendor = '{vendor}'")
            if region:
                conditions.append(f"s.region = '{region}'")
            cypher += " WHERE " + " AND ".join(conditions)
        result = session.run(cypher)
        records = [record.data() for record in result]
    driver.close()
    return pd.DataFrame(records)

def _get_api_data(vendor=None, region=None):
    """Fetch data from an external API."""
    params = {"vendor": vendor, "region": region, "api_key": API_KEY}
    response = requests.get(API_URL, params=params)
    response.raise_for_status()
    data = response.json()
    return pd.DataFrame(data)
