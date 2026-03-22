# app.py - US Predictive Supply Chain Risk Mapper

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
