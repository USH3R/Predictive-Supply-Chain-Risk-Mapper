# app.py - US Predictive Supply Chain Risk Mapper

import dash
from dash import dcc, html, Input, Output, dash_table
import pandas as pd
import plotly.express as px

# Import data and model modules
# from data import load_data
# from model import train_model, predict_risk

# ---------- Initialize Dash app ----------
app = dash.Dash(__name__)
app.title = "US Predictive Supply Chain Risk Mapper"

# ---------- Placeholder data ----------
df = pd.DataFrame({
    "Supplier": ["Supplier A", "Supplier B", "Supplier C"],
    "Region": ["North", "South", "East"],
    "Risk Score": [0.2, 0.5, 0.7],
    "Lead Time": [5, 10, 7]
})

# ---------- Layout ----------
app.layout = html.Div([
    html.H1("US Predictive Supply Chain Risk Mapper"),
    
    html.Div([
        html.Label("Select Region:"),
        dcc.Dropdown(
            id="region-dropdown",
            options=[{"label": r, "value": r} for r in df["Region"].unique()],
            value=df["Region"].unique()[0],
            multi=False
        ),
    ], style={"width": "30%", "display": "inline-block"}),

    html.Div([
        html.Label("Select Supplier:"),
        dcc.Dropdown(
            id="supplier-dropdown",
            options=[{"label": s, "value": s} for s in df["Supplier"].unique()],
            value=df["Supplier"].unique()[0],
            multi=False
        ),
    ], style={"width": "30%", "display": "inline-block", "marginLeft": "2%"}),

    html.Br(),

    dcc.Graph(id="risk-score-graph"),
    
    html.H2("Supplier Details"),
    dash_table.DataTable(
        id="supplier-table",
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict("records"),
        style_table={"overflowX": "auto"},
        style_cell={"textAlign": "left"},
    ),
])

# ---------- Callbacks ----------
@app.callback(
    Output("risk-score-graph", "figure"),
    Output("supplier-table", "data"),
    Input("region-dropdown", "value"),
    Input("supplier-dropdown", "value")
)
def update_dashboard(selected_region, selected_supplier):
    # Filter data
    filtered = df[(df["Region"] == selected_region) & (df["Supplier"] == selected_supplier)]
    
    # ---------- Placeholder figure ----------
    fig = px.bar(
        filtered,
        x="Supplier",
        y="Risk Score",
        color="Risk Score",
        range_y=[0, 1],
        title=f"Predicted Risk Score for {selected_supplier} in {selected_region}"
    )
    
    # Update table data
    table_data = filtered.to_dict("records")
    
    return fig, table_data

# ---------- Run app ----------
if __name__ == "__main__":
    app.run(debug=True)
