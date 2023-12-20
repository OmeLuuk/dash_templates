import dash
from dash import html, dcc, callback, Input, Output, State
import json

# Initialize the Dash app
app = dash.Dash(__name__)

# App layout
app.layout = html.Div([
    # 1. Button
    html.Div([
        html.Button('Submit', id='submit-button', n_clicks=0),
        html.Div(id='button-output')
    ], style={'margin-bottom': '20px'}),  # Adding margin for spacing

    # 2. Text Box
    html.Div([
        dcc.Input(id='input-text', type='text', placeholder='Enter text here'),
        html.Div(id='text-output')
    ], style={'margin-bottom': '20px'}),  # Adding margin for spacing

    # 3. Dropdown Menu
    html.Div([
        dcc.Dropdown(
            id='dropdown-menu',
            options=[
                {'label': 'Option 1', 'value': 'OPT1'},
                {'label': 'Option 2', 'value': 'OPT2'},
                {'label': 'Option 3', 'value': 'OPT3'}
            ],
            placeholder="Select an option"
        ),
        html.Div(id='dropdown-output')
    ], style={'margin-bottom': '20px'}),  # Adding margin for spacing

    # 4. Checklist
    html.Div([
        dcc.Checklist(
            id='checklist',
            options=[
                {'label': 'Item 1', 'value': 'ITEM1'},
                {'label': 'Item 2', 'value': 'ITEM2'},
                {'label': 'Item 3', 'value': 'ITEM3'}
            ],
            value=[]
        ),
        html.Div(id='checklist-output')
    ], style={'margin-bottom': '20px'}),  # Adding margin for spacing

    # 5. Combination of Inputs
    html.Div([
        html.Div("Enter text and press Submit:"),
        dcc.Input(id='combo-input-text', type='text', placeholder='Enter text'),
        html.Button('Submit Text', id='combo-submit-button', n_clicks=0),
        html.Div(id='combo-output')
    ], style={'margin-bottom': '20px'})  # Adding margin for spacing
])

# Callback for the Button
@app.callback(
    Output('button-output', 'children'),
    Input('submit-button', 'n_clicks')
)
def update_output(n_clicks):
    return f'Button has been pressed {n_clicks} times.'

# Callback for the Text Box
@app.callback(
    Output('text-output', 'children'),
    Input('input-text', 'value')
)
def update_output(value):
    return f'You have entered: {value}'

# Callback for the Dropdown Menu
@app.callback(
    Output('dropdown-output', 'children'),
    Input('dropdown-menu', 'value')
)
def update_output(value):
    return f'You have selected: {value}'

# Callback for the Checklist
@app.callback(
    Output('checklist-output', 'children'),
    Input('checklist', 'value')
)
def update_output(value):
    return f'You have selected: {json.dumps(value)}'

# Callback for the Combination
@app.callback(
    Output('combo-output', 'children'),
    Input('combo-submit-button', 'n_clicks'),
    State('combo-input-text', 'value')
)
def update_output(n_clicks, text):
    if n_clicks > 0:
        return f'You submitted "{text}"'
    return 'No submission yet.'

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
