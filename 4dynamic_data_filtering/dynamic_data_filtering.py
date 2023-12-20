import dash
import dash_bootstrap_components as dbc
from dash import html, dcc, dash_table
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Load the data from template 2
excel_file = '2reading_files/example_excel_sheet.xlsx'
df = pd.read_excel(excel_file)

# Initialize the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# App layout
app.layout = html.Div([
    dbc.Row([
        dbc.Col([
            # Dropdown for Stock Symbol filtering
            dcc.Dropdown(
                id='stock-symbol-dropdown',
                options=[{'label': symbol, 'value': symbol} for symbol in df['Stock Symbol'].unique()],
                multi=True,
                placeholder="Filter by Stock Symbol..."
            ),
            # Add more filters here if needed
        ]),
        dbc.Col([
            # Dropdown for Category filtering
            dcc.Dropdown(
                id='category-dropdown',
                options=[{'label': cat, 'value': cat} for cat in df['Category'].unique()],
                multi=True,
                placeholder="Filter by Category..."
            )
        ]),
        # Additional filters can be added in more columns
    ]),
    dbc.Row([
        dbc.Col([
            # Data Table
            dash_table.DataTable(id='table-container', data=df.to_dict('records'), columns=[{'name': i, 'id': i} for i in df.columns])
        ])
    ]),
    dbc.Row([
        dbc.Col([
            # Graph
            dcc.Graph(id='graph-container')
        ])
    ]),

    # New Row for Symbol Checklist
    dbc.Row([
        dbc.Col([
            dcc.Checklist(
                id='symbol-checklist',
                options=[{'label': symbol, 'value': symbol} for symbol in df['Stock Symbol'].unique()],
                value=df['Stock Symbol'].unique(),  # Initially, all symbols are selected
                inline=True
            )
        ])
    ]),
    dbc.Row([
        dbc.Col([
            # New Data Table for Selected Symbols
            dash_table.DataTable(id='symbol-table')
        ])
    ])
])

# Callback for updating the table and graph based on filters
@app.callback(
    [Output('table-container', 'data'), Output('graph-container', 'figure')],
    [Input('stock-symbol-dropdown', 'value'), Input('category-dropdown', 'value')]
)
def update_output(stock_symbols, categories):
    # Filter data based on selections
    filtered_df = df
    if stock_symbols:
        filtered_df = filtered_df[filtered_df['Stock Symbol'].isin(stock_symbols)]
    if categories:
        filtered_df = filtered_df[filtered_df['Category'].isin(categories)]

    # Update table
    table_data = filtered_df.to_dict('records')

    # Update graph (example: bar chart of closing prices)
    fig = px.bar(filtered_df, x='Stock Symbol', y='Closing Price', color='Category')

    return table_data, fig

# Callback for the Symbol Checklist
@app.callback(
    Output('symbol-table', 'data'),
    Input('symbol-checklist', 'value')
)
def update_symbol_table(selected_symbols):
    # Filter the DataFrame based on selected symbols
    filtered_df = df[df['Stock Symbol'].isin(selected_symbols)]
    return filtered_df.to_dict('records')

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
