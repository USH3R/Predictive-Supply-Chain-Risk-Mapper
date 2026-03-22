# app.py - US Predictive Supply Chain Risk Mapper
# Added Dash dashboard using modular data.py interface

import dash
from dash import dcc, html, Output, Input
import plotly.express as px
from data import get_supply_data

# ------------------------------
# Initialize Dash app
# ------------------------------
app = dash.Dash(__name__)
app.title = "US Predictive Supply Chain Risk Mapper"

# ------------------------------
# Sample options for dropdowns
# (Replace with dynamic lists from your database/API if desired)
# ------------------------------
vendors = ["Vendor A", "Vendor B", "Vendor C"]
regions = ["North", "South", "East", "West"]

# ------------------------------
# Layout
# ------------------------------
app.layout = html.Div([
    html.H1("US Predictive Supply Chain Risk Mapper"),
    html.Div([
        html.Label("Select Vendor:"),
        dcc.Dropdown(id="vendor-dropdown", options=[{"label": v, "value": v} for v in vendors], value=None, multi=True),
        html.Label("Select Region:"),
        dcc.Dropdown(id="region-dropdown", options=[{"label": r, "value": r} for r in regions], value=None, multi=True),
    ], style={"width": "30%", "display": "inline-block", "verticalAlign": "top"}),
    html.Div([
        dcc.Graph(id="risk-graph"),
        html.Div(id="risk-details")
    ], style={"width": "65%", "display": "inline-block", "paddingLeft": "20px"})
])

# ------------------------------
# Callbacks
# ------------------------------
@app.callback(
    Output("risk-graph", "figure"),
    Output("risk-details", "children"),
    Input("vendor-dropdown", "value"),
    Input("region-dropdown", "value")
)
def update_dashboard(selected_vendors, selected_regions):
    # Fetch data from modular data.py
    df = get_supply_data(vendor=selected_vendors, region=selected_regions, source="sql")  # Change source if needed

    if df.empty:
        fig = px.scatter(title="No Data Available")
        details = "No supply chain data available for the selected filters."
        return fig, details

    # Example risk graph
    fig = px.scatter(
        df,
        x="vendor",
        y="risk",
        color="region",
        size="risk",
        hover_data=["vendor", "region", "risk"],
        title="Supply Chain Risk by Vendor and Region"
    )

    # Example textual details
    avg_risk = df["risk"].mean() if "risk" in df.columns else None
    details = f"Average Risk Score: {avg_risk:.2f}" if avg_risk is not None else "Risk data unavailable."

    return fig, details

# ------------------------------
# Run the app
# ------------------------------
if __name__ == "__main__":
    app.run(debug=True)  # Use app.run() for Dash v2+# app.py - US Predictive Supply Chain Risk Mapper

import dash
from dash import dcc, html, Output, Input
import plotly.graph_objects as go
import pandas as pd

# Import the updated model
from model import SupplyChainRiskModel

# Initialize Dash app
app = dash.Dash(__name__)
app.title = "US Predictive Supply Chain Risk Mapper"

# Initialize the predictive model
model = SupplyChainRiskModel()

# Placeholder dataset for now (replace with real SQL/Neo4j/API data later)
data = pd.DataFrame({
    "Vendor": ["Vendor A", "Vendor B", "Vendor C"],
    "Region": ["North", "South", "West"],
    "Supply Volume": [1000, 1500, 800]
})

# Layout
app.layout = html.Div([
    html.H1("US Predictive Supply Chain Risk Mapper"),
    
    html.Div([
        html.Label("Select Vendor:"),
        dcc.Dropdown(
            id="vendor-dropdown",
            options=[{"label": v, "value": v} for v in data["Vendor"]],
            value=data["Vendor"].iloc[0]
        )
    ], style={"width": "300px", "margin-bottom": "20px"}),
    
    html.Div([
        html.Label("Select Region:"),
        dcc.Dropdown(
            id="region-dropdown",
            options=[{"label": r, "value": r} for r in data["Region"]],
            value=data["Region"].iloc[0]
        )
    ], style={"width": "300px", "margin-bottom": "20px"}),

    dcc.Graph(id="risk-graph"),
    html.Div(id="risk-details", style={"margin-top": "20px", "font-weight": "bold"})
])

# Callbacks
@app.callback(
    Output("risk-graph", "figure"),
    Output("risk-details", "children"),
    Input("vendor-dropdown", "value"),
    Input("region-dropdown", "value")
)
def update_dashboard(vendor, region):
    # Filter placeholder dataset
    filtered = data[(data["Vendor"] == vendor) & (data["Region"] == region)]
    
    # Convert to numeric array for prediction
    numeric_data = filtered[["Supply Volume"]].values if not filtered.empty else None
    
    # Predict risk using the model
    risk_score = model.predict(numeric_data) if numeric_data is not None else 0.5
    
    # Create risk graph
    fig = go.Figure(go.Bar(
        x=[vendor],
        y=[risk_score],
        marker_color="red" if risk_score > 0.7 else "orange" if risk_score > 0.4 else "green"
    ))
    fig.update_layout(
        title=f"Predicted Supply Chain Risk Score for {vendor} ({region})",
        yaxis=dict(range=[0, 1], title="Risk Score"),
        xaxis=dict(title="Vendor")
    )
    
    # Risk details text
    details = f"Predicted Risk Score: {risk_score:.2f}"
    
    return fig, details

# Run server
if __name__ == "__main__":
    app.run(debug=True)
