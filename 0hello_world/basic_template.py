import dash
import dash_html_components as html

# Create a Dash application
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    html.H1("Hello World", style={'text-align': 'center'}),
    html.P("Hello World", style={'font-weight': 'bold'}),
    html.P("Hello World", style={'font-style': 'italic'}),
    html.P("Hello World", style={'text-decoration': 'underline'}),
    html.P("Hello World", style={'color': 'blue'}),
    html.P("Hello World", style={'font-weight': 'bold', 'font-style': 'italic', 'text-decoration': 'underline', 'color': 'green'}),
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
