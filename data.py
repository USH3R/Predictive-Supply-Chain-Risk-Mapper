# data.py - US Predictive Supply Chain Risk Mapper
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
