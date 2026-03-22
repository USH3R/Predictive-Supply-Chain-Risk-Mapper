# data.py - US Predictive Supply Chain Risk Mapper
# Handles connections and data retrieval from SQL, Neo4j, and APIs

import sqlalchemy
from neo4j import GraphDatabase
import requests
import pandas as pd

# ---------- SQL DATABASE ----------
def get_sql_data(connection_string, query):
    """
    Connect to SQL database and return query result as a DataFrame.
    """
    engine = sqlalchemy.create_engine(connection_string)
    with engine.connect() as conn:
        df = pd.read_sql(query, conn)
    return df

# ---------- NEO4J DATABASE ----------
def get_neo4j_data(uri, user, password, cypher_query):
    """
    Connect to Neo4j and return query result as a list of dicts.
    """
    driver = GraphDatabase.driver(uri, auth=(user, password))
    with driver.session() as session:
        result = session.run(cypher_query)
        data = [record.data() for record in result]
    driver.close()
    return data

# ---------- API REQUEST ----------
def fetch_api_data(url, params=None, headers=None):
    """
    Fetch JSON data from a REST API.
    """
    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()
    return response.json()

# ---------- EXAMPLE USAGE PLACEHOLDERS ----------
if __name__ == "__main__":
    print("This is the data module for US Predictive Supply Chain Risk Mapper.")
    print("Use get_sql_data(), get_neo4j_data(), fetch_api_data() to pull data.")# data.py
# Modular data loading for US Predictive Supply Chain Risk Mapper

import pandas as pd
from sqlalchemy import create_engine
from neo4j import GraphDatabase
import requests

# ----------------------------
# SQL Data
# ----------------------------
def load_sql_data(connection_string, query):
    """
    Load data from SQL database.
    """
    engine = create_engine(connection_string)
    df = pd.read_sql(query, engine)
    return df

# ----------------------------
# Neo4j Graph Data
# ----------------------------
def load_neo4j_data(uri, user, password, cypher_query):
    """
    Load data from Neo4j graph database.
    """
    driver = GraphDatabase.driver(uri, auth=(user, password))
    with driver.session() as session:
        result = session.run(cypher_query)
        data = [record.data() for record in result]
    driver.close()
    return pd.DataFrame(data)

# ----------------------------
# API Data
# ----------------------------
def load_api_data(url, params=None):
    """
    Load JSON data from an API.
    """
    response = requests.get(url, params=params)
    response.raise_for_status()
    return pd.DataFrame(response.json())

# ----------------------------
# Sample placeholder data
# ----------------------------
def load_sample_data():
    """
    Return a small sample dataset for dashboard testing.
    """
    data = pd.DataFrame({
        'vendor': ['Vendor A', 'Vendor B', 'Vendor C'],
        'risk_score': [0.2, 0.5, 0.8],
        'criticality': [3, 2, 5],
        'week': [1, 1, 1]
    })
    return data
