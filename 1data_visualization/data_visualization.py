import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd

# Sample dataset to use as a placeholder, provided by Plotly for demonstration purposes
df = px.data.iris()

# Scatter plot
scatter_plot = px.scatter(df, x="sepal_width", y="sepal_length", color="species")

# Line plot
line_plot = px.line(df, x="sepal_length", y="petal_length", color="species")

# Bar chart
bar_chart = px.bar(df, x="species", y="petal_width")

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Data Visualization with Dash"),
    html.Div([
        dcc.Graph(figure=scatter_plot),
        dcc.Graph(figure=line_plot),
        dcc.Graph(figure=bar_chart)
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)
