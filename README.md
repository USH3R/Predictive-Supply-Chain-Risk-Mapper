# US Predictive Supply Chain Risk Mapper

[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://www.python.org/)
[![SQL](https://img.shields.io/badge/SQL-PostgreSQL-lightblue)](https://www.postgresql.org/)
[![Dash](https://img.shields.io/badge/Dash-Python-orange)](https://dash.plotly.com/)
[![Hackathon Ready](https://img.shields.io/badge/Hackathon-Ready-brightgreen)](#)
[![Federal Impact](https://img.shields.io/badge/Federal-Government--Cybersecurity-red)](#)

---

The **US Predictive Supply Chain Risk Mapper** is a hackathon-ready cybersecurity tool designed to help federal agencies predict supply chain risk for vendors, visualize dependencies, and provide actionable mitigation strategies. Built entirely in **Python + SQL + Dash**, this tool combines predictive modeling with interactive dashboards for real-time risk assessment.
---  
**How to Run the Application**
  
1. Run in GitHub Codespaces (Recommended)  
Open this repository on GitHub.  
Click Code → Codespaces → Create Codespace on main.  
Wait for the environment to load.  
Open the terminal inside Codespaces.  
Run:         &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bash run.sh  
When the server starts, open the browser,
or open the Port tab and then open forwarded port (usually 8050), to view the dashboard.  
  
3. Run Manually Inside the Repository (Local Machine)  
If you downloaded or cloned the repository:  
Open a terminal.  
Navigate to the project folder.  
Example:  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cd US-Predictive-Supply-Chain-Risk-Mapper  
Run the launcher:  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bash run.sh  
Open your browser and go to:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;http://localhost:8050

3. If You Are Using a Random Public Terminal  
Public terminals do not automatically have this project. You must first download or clone the repository.  

A. Option A — Clone with Git  
Type:  
git clone https://github.com/YOUR_USERNAME/REPO_NAME.git  
cd REPO_NAME  
bash run.sh  

B. Option B — Download ZIP  
Click Code → Download ZIP on GitHub.  
Extract the folder from the ZIP file. Then,  
Open a terminal in that folder.
Run / Type: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bash run.sh

4. Quick Start Command  
If you are already in the correct folder, just use:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bash run.sh  
           
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

**Future Enhancements**

Add real-time dark web / threat feed monitoring.
Integrate advanced ML predictive models.
Expand dashboard with Neo4j graph visualizations.
Automate mitigation suggestions and alerting.
Potential Federal Impact

This tool provides federal agencies with:

Real-time vendor risk assessment.
Early detection of supply chain threats.
Actionable recommendations for mitigation.
Visualizations for cascading risks across government dependencies.

By combining predictive modeling and interactive dashboards, this tool could strengthen U.S. federal cybersecurity posture and reduce the risk of attacks similar to the SolarWinds supply chain breach.

✅ **Proposed updated repo structure after modular expansion**
U.S.-Predictive-Supply-Chain-Risk-Mapper/
│         
├─ run.sh         
├─ requirements.txt         
├─ README.md         
├─ app.py                                         # Main dashboard              
├─ data.py                                         # Data loading: SQL / Neo4j / APIs               
├─ model.py                                        # Predictive model               
├─ utils.py (optional)                             # Helper functions               
└─ assets/                                         # Charts, logos, static files               

