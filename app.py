# app.py - US Predictive Supply Chain Risk Mapper

import dash
from dash import dcc, html, Input, Output, callback
import plotly.express as px
import pandas as pd

# ---------- Initialize app ----------
app = dash.Dash(__name__)
app.title = "US Predictive Supply Chain Risk Mapper"

# ---------- Placeholder data ----------
# Example dataframe (replace with SQL, Neo4j, or API data later)
example_data = pd.DataFrame({
    "Vendor": ["Vendor A", "Vendor B", "Vendor C"],
    "Risk Score": [0.2, 0.7, 0.5],
    "Category": ["Logistics", "Supplier", "Distribution"]
})

# ---------- Layout ----------
app.layout = html.Div([
    html.H1("US Predictive Supply Chain Risk Mapper", style={"textAlign": "center"}),
    
    html.H3("Select Vendor:"),
    dcc.Dropdown(
        id="vendor-dropdown",
        options=[{"label": v, "value": v} for v in example_data["Vendor"]],
        value="Vendor A",
        clearable=False
    ),

    html.Br(),
    html.Div(id="risk-output"),

    html.Br(),
    dcc.Graph(id="risk-graph"),

    html.Br(),
    html.H3("Detailed Data Table"),
    html.Div(id="data-table")
])

# ---------- Callbacks ----------
@app.callback(
    Output("risk-output", "children"),
    Output("risk-graph", "figure"),
    Output("data-table", "children"),
    Input("vendor-dropdown", "value")
)
def update_dashboard(selected_vendor):
    # Filter data (placeholder)
    filtered = example_data[example_data["Vendor"] == selected_vendor]
    
    # Graph
    fig = px.bar(filtered, x="Category", y="Risk Score", color="Risk Score",
                 range_y=[0, 1], title=f"Risk Breakdown for {selected_vendor}")
    
    # Table
    table = html.Table([
        html.Thead(html.Tr([html.Th(col) for col in filtered.columns])),
        html.Tbody([
            html.Tr([html.Td(filtered.iloc[0][col]) for col in filtered.columns])
        ])
    ])
    
    details_text = f"Selected Vendor: {selected_vendor} | Risk Score: {filtered['Risk Score'].values[0]:.2f}"
    
    return details_text, fig, table

# ---------- Main ----------
if __name__ == "__main__":
    # Placeholder for real-time running
    app.run(debug=True)# app.py
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# -----------------------------
# Placeholder data
# -----------------------------
data = pd.DataFrame({
    'vendor': ['Vendor A', 'Vendor B', 'Vendor C', 'Vendor A', 'Vendor B', 'Vendor C'],
    'week': [1, 1, 1, 2, 2, 2],
    'predicted_risk': [0.2, 0.5, 0.3, 0.25, 0.45, 0.35],
    'risk_score': [2, 5, 3, 2.5, 4.5, 3.5],
    'criticality': ['High', 'Medium', 'Low', 'High', 'Medium', 'Low']
})

# -----------------------------
# Initialize Dash app
# -----------------------------
app = dash.Dash(__name__)
app.title = "US Predictive Supply Chain Risk Mapper"

# -----------------------------
# Layout
# -----------------------------
app.layout = html.Div([
    html.H1("US Predictive Supply Chain Risk Mapper", style={'textAlign': 'center'}),
    
    html.Div([
        html.Label("Select Vendors:"),
        dcc.Dropdown(
            id='vendor-dropdown',
            options=[{'label': v, 'value': v} for v in data['vendor'].unique()],
            value=['Vendor A', 'Vendor B'],
            multi=True
        )
    ], style={'width': '50%', 'margin': 'auto'}),
    
    html.Br(),
    
    html.Div([
        dcc.Graph(id='risk-graph'),
        dcc.Graph(id='trend-graph')
    ]),
    
    html.Div(id='vendor-details', style={'marginTop': '20px'})
])

# -----------------------------
# Callbacks
# -----------------------------
@app.callback(
    Output('risk-graph', 'figure'),
    Output('trend-graph', 'figure'),
    Output('vendor-details', 'children'),
    Input('vendor-dropdown', 'value')
)
def update_dashboard(selected_vendors):
    filtered = data[data['vendor'].isin(selected_vendors)]

    # Risk bar chart
    risk_fig = px.bar(
        filtered,
        x='vendor',
        y='predicted_risk',
        title='Predicted Risk by Vendor'
    )

    # Trend line
    trend_fig = px.line(
        filtered,
        x='week',
        y='predicted_risk',
        color='vendor',
        title='Predicted Risk Trends Over Time'
    )

    # Vendor table
    table = html.Table([
        html.Tr([html.Th("Vendor"), html.Th("Risk Score"), html.Th("Criticality")])
    ] + [
        html.Tr([html.Td(row['vendor']), html.Td(row['risk_score']), html.Td(row['criticality'])])
        for _, row in filtered.iterrows()
    ])

    return risk_fig, trend_fig, table

# -----------------------------
# Main
# -----------------------------
if __name__ == '__main__':
    app.run(debug=True)  # use debug=True for development
