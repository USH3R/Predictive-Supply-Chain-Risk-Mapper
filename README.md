# US Predictive Supply Chain Risk Mapper

[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://www.python.org/)
[![SQL](https://img.shields.io/badge/SQL-PostgreSQL-lightblue)](https://www.postgresql.org/)
[![Dash](https://img.shields.io/badge/Dash-Python-orange)](https://dash.plotly.com/)
[![Hackathon Ready](https://img.shields.io/badge/Hackathon-Ready-brightgreen)](#)
[![Federal Impact](https://img.shields.io/badge/Federal-Government--Cybersecurity-red)](#)

---

## Description

The **US Predictive Supply Chain Risk Mapper** is a hackathon-ready cybersecurity tool designed to help federal agencies predict supply chain risk for vendors, visualize dependencies, and provide actionable mitigation strategies. Built entirely in **Python + SQL + Dash**, this tool combines predictive modeling with interactive dashboards for real-time risk assessment.
---

## Features

1. **Vendor Risk Collection**
   - Pull CVE feeds, GitHub leaks, and other public signals.
   - Store vendor information and dependencies in a SQL database.

2. **Predictive Risk Scoring**
   - Simple AI/ML model predicts probability of vendor compromise within 30–90 days.
   - Early-warning system to anticipate supply chain attacks.

3. **Supply Chain Mapping**
   - Visualize vendor dependencies in an interactive network graph.
   - Identify cascading risks that affect multiple agencies.

4. **Interactive Dashboard**
   - Built using **Dash (Python)** for real-time monitoring.
   - Displays risk scores, vendor tables, and dependency maps.
   - Highlights high-risk vendors for fast decision-making.

5. **Actionable Recommendations**
   - Suggest mitigation strategies automatically.
   - Generate briefing-ready reports for agency leadership.
---

## Architecture Diagram
Vendor Data (CVE feeds, APIs, GitHub leaks)
→
Python Scraper / Data Processor 
→
SQL Database (Stores vendors, risk scores, dependencies)
→
Predictive Model (Python ML, e.g., scikit-learn or simple logic)
→
Dash Dashboard (Risk maps, vendor graph, score tables)


**Minimal, hackathon-ready:**

Python – scraping, processing, predictive modeling, backend logic

SQL – storing vendor data, CVEs, risk scores

Dash (Python library) – front-end dashboard and visualizations

- Optional / advanced later:

Neo4j – graph database for supply chain relationships

Docker – containerization for easy deployment
