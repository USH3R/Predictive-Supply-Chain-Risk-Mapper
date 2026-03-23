import dash
from dash import dcc, html, dash_table
import pandas as pd
import plotly.express as px

# Mock Data simulating the SQL/Predictive Model output
# --- REPLACEMENT START ---
try:
    # This looks for the file created by the data_engine
    df = pd.read_csv('live_data.csv')
except:
    # EMERGENCY FALLBACK: If live_data.csv is missing, use this so the app doesn't crash
    df = pd.DataFrame({
        "Vendor": ["Fallback-System"],
        "Current_CVEs": [0],
        "GitHub_Leaks": ["None"],
        "Predictive_Risk_Score": [0.0]
    })
# --- REPLACEMENT END ---

app = dash.Dash(__name__)

# The Layout (What appears in the browser)
app.layout = html.Div(style={'backgroundColor': '#0a0a0a', 'color': '#e0e0e0', 'padding': '40px', 'fontFamily': 'sans-serif'}, children=[
    html.H1("🇺🇸 US Predictive Supply Chain Risk Mapper", style={'textAlign': 'center', 'color': '#0074D9'}),
    html.P("Federal Agency Oversight - Real-Time Vendor Threat Intelligence", style={'textAlign': 'center'}),
    html.Hr(style={'borderColor': '#333'}),
    
    html.Div([
        html.H3("Active Vendor Risk Assessment"),
        dash_table.DataTable(
            data=df.to_dict('records'),
            columns=[{"name": i, "id": i} for i in df.columns],
            style_header={'backgroundColor': '#1a1a1a', 'fontWeight': 'bold', 'border': '1px solid #333'},
            style_cell={'backgroundColor': '#111', 'color': '#fff', 'textAlign': 'left', 'padding': '10px'},
            style_data_conditional=[{
                'if': {'filter_query': '{Predictive_Risk_Score} > 0.7', 'column_id': 'Predictive_Risk_Score'},
                'backgroundColor': '#850000', 'color': 'white'
            }]
        )
    ], style={'padding': '20px'}),

    html.Div([
        dcc.Graph(
            figure=px.bar(df, x="Vendor", y="Predictive_Risk_Score", color="Predictive_Risk_Score",
                          title="90-Day Probability of Compromise",
                          template="plotly_dark",
                          color_continuous_scale='Reds')
        )
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)# app.py - US Predictive Supply Chain Risk Mapper
# Full Dash app connecting data.py + model.py

import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

from data import get_supply_data
from model import predict_risk

# Initialize Dash app
app = dash.Dash(__name__)
app.title = "US Predictive Supply Chain Risk Mapper"

# Fetch supply data and compute risk scores
df = get_supply_data()
df = predict_risk(df)

# Layout
app.layout = html.Div([
    html.H1("US Predictive Supply Chain Risk Mapper", style={'textAlign': 'center'}),
    
    # Vendor dropdown for multi-vendor selection
    dcc.Dropdown(
        id='vendor-dropdown',
        options=[{'label': v, 'value': v} for v in df['vendor'].unique()],
        value=df['vendor'].unique().tolist(),
        multi=True,
        placeholder="Select vendors"
    ),
    
    # Risk trend graph
    dcc.Graph(id='risk-trend-graph'),

    # Vendor comparison table
    html.Div(id='vendor-table')
])

# Callbacks for updating graph and table based on dropdown
@app.callback(
    Output('risk-trend-graph', 'figure'),
    Output('vendor-table', 'children'),
    Input('vendor-dropdown', 'value')
)
def update_dashboard(selected_vendors):
    filtered_df = df[df['vendor'].isin(selected_vendors)]
    
    # Risk trend bar graph
    fig = px.bar(
        filtered_df,
        x='vendor',
        y='risk_score',
        color='region',
        barmode='group',
        title='Vendor Risk Score Comparison'
    )
    
    # Table display
    table = html.Table([
        html.Thead(html.Tr([html.Th(col) for col in filtered_df.columns])),
        html.Tbody([
            html.Tr([html.Td(filtered_df.iloc[i][col]) for col in filtered_df.columns])
            for i in range(len(filtered_df))
        ])
    ])
    
    return fig, table

# Run server (accessible in Codespaces via forwarded port)
if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=8080)
