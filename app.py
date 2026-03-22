# app.py - US Predictive Supply Chain Risk Mapper Dashboard
import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

from data import get_supply_data
from model import predict_risk

# Initialize Dash app
app = dash.Dash(__name__)
app.title = "US Predictive Supply Chain Risk Mapper"

# Get supply chain data (mock or real)
df = get_supply_data()
df = predict_risk(df)  # Add predicted risk scores

# Multi-vendor comparison plot
fig_vendor = px.bar(df, x="vendor", y="predicted_risk", color="region",
                    barmode="group", title="Predicted Risk by Vendor & Region")

# Risk trend plot (mock: metric_1 over vendor/region)
fig_trend = px.line(df, x="vendor", y="metric_1", color="region",
                    title="Supply Metric Trend by Vendor & Region")

# Layout with two main plots
app.layout = html.Div([
    html.H1("US Predictive Supply Chain Risk Mapper"),
    
    html.Div([
        html.H2("Multi-Vendor Risk Comparison"),
        dcc.Graph(figure=fig_vendor)
    ]),
    
    html.Div([
        html.H2("Supply Metric Trend"),
        dcc.Graph(figure=fig_trend)
    ])
])

if __name__ == "__main__":
    app.run(debug=True)# app.py - US Predictive Supply Chain Risk Mapper
# Full modular app using data.py + model.py with multi-vendor & trend plots

from dash import Dash, dcc, html, Input, Output
from data import get_supply_data
from model import predict_risk, risk_summary
import pandas as pd

# -------------------------
# Initialize Dash App
# -------------------------
app = Dash(__name__)
app.title = "US Predictive Supply Chain Risk Mapper"

# -------------------------
# Load and process data
# -------------------------
df = get_supply_data("mock")  # Pull mock data
df = predict_risk(df)         # Add 'risk' column

# Simulate risk trend over time for vendors
# Create mock time series (for demonstration)
df_trend = df.copy()
df_trend = df_trend.loc[df_trend.index.repeat(5)]
df_trend['day'] = list(range(1, 6)) * (len(df_trend) // 5)
df_trend['risk_trend'] = df_trend['risk'] * (1 + 0.1 * df_trend['day'])

# -------------------------
# App Layout
# -------------------------
app.layout = html.Div([
    html.H1("US Predictive Supply Chain Risk Mapper", style={'textAlign': 'center'}),
    html.H2(f"Average Risk: {risk_summary(df)['average_risk']:.2f}", style={'textAlign': 'center'}),

    # Dropdown to filter by region
    html.Label("Select Region:"),
    dcc.Dropdown(
        id='region-dropdown',
        options=[{'label': r, 'value': r} for r in sorted(df['region'].unique())],
        value=None,
        placeholder="All regions",
        multi=False
    ),

    # Multi-vendor comparison dropdown
    html.Label("Select Vendors for Comparison:"),
    dcc.Dropdown(
        id='vendor-dropdown',
        options=[{'label': v, 'value': v} for v in sorted(df['vendor'].unique())],
        value=[],
        multi=True,
        placeholder="Select one or more vendors"
    ),

    # Bar chart of risk scores
    dcc.Graph(id="risk-bar"),

    # Trend plot
    dcc.Graph(id="risk-trend"),

    # Table of vendor metrics and risk
    html.H3("Vendor Risk Details"),
    dcc.Graph(id="risk-table")
])

# -------------------------
# Callbacks
# -------------------------
@app.callback(
    Output('risk-bar', 'figure'),
    Output('risk-table', 'figure'),
    Output('risk-trend', 'figure'),
    Input('region-dropdown', 'value'),
    Input('vendor-dropdown', 'value')
)
def update_dashboard(selected_region, selected_vendors):
    # Filter by region
    filtered_df = df if not selected_region else df[df['region'] == selected_region]

    # Bar chart for risk scores (filtered by region)
    bar_fig = {
        "data": [
            {"x": filtered_df["vendor"], "y": filtered_df["risk"], "type": "bar", "name": "Risk Score"}
        ],
        "layout": {"title": f"Predicted Risk per Vendor ({selected_region if selected_region else 'All Regions'})"}
    }

    # Table of metrics + risk
    table_fig = {
        "data": [
            {
                "type": "table",
                "header": {"values": list(filtered_df.columns), "fill_color": "paleturquoise"},
                "cells": {"values": [filtered_df[col] for col in filtered_df.columns], "fill_color": "lavender"}
            }
        ]
    }

    # Risk trend plot (time series) for selected vendors
    trend_df = df_trend if not selected_vendors else df_trend[df_trend['vendor'].isin(selected_vendors)]
    trend_fig = {
        "data": [
            {"x": trend_df[trend_df['vendor'] == v]['day'],
             "y": trend_df[trend_df['vendor'] == v]['risk_trend'],
             "type": "line",
             "name": v} for v in trend_df['vendor'].unique()
        ],
        "layout": {"title": "Vendor Risk Trends Over Time", "xaxis": {"title": "Day"}, "yaxis": {"title": "Risk"}}
    }

    return bar_fig, table_fig, trend_fig

# -------------------------
# Run the app
# -------------------------
if __name__ == "__main__":
    app.run(debug=True)
