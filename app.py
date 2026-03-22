# app.py - US Predictive Supply Chain Risk Mapper
# Modular Dash app connecting data.py + model.py

import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

from data import get_supply_data
from model import predict_risk

# Initialize app
app = dash.Dash(__name__)
app.title = "US Predictive Supply Chain Risk Mapper"

# Fetch data and predict risks
df = get_supply_data()
df = predict_risk(df)

# Layout
app.layout = html.Div([
    html.H1("US Predictive Supply Chain Risk Mapper"),
    
    # Vendor dropdown
    dcc.Dropdown(
        id='vendor-dropdown',
        options=[{'label': v, 'value': v} for v in df['vendor'].unique()],
        value=df['vendor'].unique().tolist(),
        multi=True
    ),
    
    # Risk trend graph
    dcc.Graph(id='risk-trend-graph'),

    # Vendor comparison table
    html.Div(id='vendor-table')
])

# Callbacks
@app.callback(
    Output('risk-trend-graph', 'figure'),
    Output('vendor-table', 'children'),
    Input('vendor-dropdown', 'value')
)
def update_dashboard(selected_vendors):
    filtered_df = df[df['vendor'].isin(selected_vendors)]
    
    # Risk trend over vendors
    fig = px.bar(filtered_df, x='vendor', y='risk_score', color='region', barmode='group',
                 title='Vendor Risk Score Comparison')
    
    # Table
    table = html.Table([
        html.Thead(html.Tr([html.Th(col) for col in filtered_df.columns])),
        html.Tbody([
            html.Tr([html.Td(filtered_df.iloc[i][col]) for col in filtered_df.columns])
            for i in range(len(filtered_df))
        ])
    ])
    
    return fig, table

# Run server
if __name__ == '__main__':
    app.run(debug=True)# app.py - US Predictive Supply Chain Risk Mapper
# Modular Dash app connecting data.py + model.py

import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

from data import get_supply_data
from model import predict_risk

# Initialize app
app = dash.Dash(__name__)
app.title = "US Predictive Supply Chain Risk Mapper"

# Fetch and predict
df = get_supply_data()
df = predict_risk(df)

# Layout
app.layout = html.Div([
    html.H1("US Predictive Supply Chain Risk Mapper"),
    
    # Vendor dropdown
    dcc.Dropdown(
        id='vendor-dropdown',
        options=[{'label': v, 'value': v} for v in df['vendor'].unique()],
        value=df['vendor'].unique().tolist(),
        multi=True
    ),
    
    # Risk trend graph
    dcc.Graph(id='risk-trend-graph'),

    # Vendor comparison table
    html.Div(id='vendor-table')
])

# Callbacks
@app.callback(
    Output('risk-trend-graph', 'figure'),
    Output('vendor-table', 'children'),
    Input('vendor-dropdown', 'value')
)
def update_dashboard(selected_vendors):
    filtered_df = df[df['vendor'].isin(selected_vendors)]
    
    # Risk trend over delivery delay
    fig = px.bar(filtered_df, x='vendor', y='risk_score', color='region', barmode='group',
                 title='Vendor Risk Score Comparison')
    
    # Table
    table = html.Table([
        html.Thead(html.Tr([html.Th(col) for col in filtered_df.columns])),
        html.Tbody([
            html.Tr([html.Td(filtered_df.iloc[i][col]) for col in filtered_df.columns])
            for i in range(len(filtered_df))
        ])
    ])
    
    return fig, table

# Run server
if __name__ == '__main__':
    app.run(debug=True)
