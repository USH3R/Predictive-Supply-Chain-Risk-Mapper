# app.py
# US Predictive Supply Chain Risk Mapper - interactive dashboard

import dash
from dash import html, dcc, Input, Output
import plotly.express as px
import pandas as pd

from data import load_sample_data
from model import predict_risk

# Load and predict
data = load_sample_data()
data = predict_risk(data)

# Initialize app
app = dash.Dash(__name__)
app.title = "US Predictive Supply Chain Risk Mapper"

# Layout
app.layout = html.Div([
    html.H1("US Predictive Supply Chain Risk Mapper", style={'textAlign': 'center'}),
    
    html.P("Interactive dashboard to explore predictive supply chain risks."),
    
    # Vendor selection dropdown
    html.Label("Select Vendor(s):"),
    dcc.Dropdown(
        id='vendor-dropdown',
        options=[{'label': v, 'value': v} for v in data['vendor']],
        value=[data['vendor'][0]],
        multi=True
    ),
    
    # Risk bar chart
    dcc.Graph(id='risk-graph'),
    
    # Risk trend line chart
    dcc.Graph(id='trend-graph'),
    
    # Vendor details table
    html.Div(id='vendor-details')
])

# Callbacks
@app.callback(
    Output('risk-graph', 'figure'),
    Output('trend-graph', 'figure'),
    Output('vendor-details', 'children'),
    Input('vendor-dropdown', 'value')
)
def update_dashboard(selected_vendors):
    filtered = data[data['vendor'].isin(selected_vendors)]
    
    # Bar chart for predicted risk
    risk_fig = px.bar(
        filtered,
        x='vendor',
        y='predicted_risk',
        title='Predicted Risk by Vendor'
    )
    
    # Trend line over weeks
    trend_fig = px.line(
        filtered,
        x='week',
        y='predicted_risk',
        color='vendor',
        title='Predicted Risk Trends Over Time'
    )
    
    # Table
    table = html.Table([
        html.Tr([html.Th("Vendor"), html.Th("Risk Score"), html.Th("Criticality")])
    ] + [
        html.Tr([html.Td(row['vendor']), html.Td(row['risk_score']), html.Td(row['criticality'])])
        for _, row in filtered.iterrows()
    ])
    
    return risk_fig, trend_fig, table

# Run app
if __name__ == '__main__':
    app.run(debug=True)
    return fig, details

# Run
if __name__ == '__main__':
    app.run(debug=True)
