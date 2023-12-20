import pandas as pd
import dash
from dash import dash_table
from dash import dcc
from dash import html
import plotly.express as px

# Here we need to put the path to the file we wish to read, in this case an excel file
# Note that the path to this file is relative to where you run the python app from, NOT relative to where this python file is
# Excuting this from the folder where the file is located means you need to load 'example_excel_sheet.xlsx'. Executing from the top level folder dash_templates means using this path:
excel_file = '2reading_files/example_excel_sheet.xlsx'
df = pd.read_excel(excel_file)

# Calculating total value (Volume * Closing Price) and adding it to the dataframe
df['Total Value'] = df['Volume'] * df['Closing Price']

# Calculating the percentage change for each stock
df['Percentage Change'] = ((df['Closing Price'] - df['Opening Price']) / df['Opening Price']) * 100

# Aggregating total value by category for the pie chart
df_agg = df.groupby('Category')['Total Value'].sum().reset_index()

# Pie chart: Total value by category
pie_chart = px.pie(df_agg, names='Category', values='Total Value', title='Total Value by Category')

# Bar chart: Percentage Change of Stocks
bar_chart = px.bar(df, x='Stock Symbol', y='Percentage Change', title='Percentage Change in Stock Prices')

# Dash app layout
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Stock Information"),
    dash_table.DataTable(
        data=df.to_dict('records'),
        columns=[{'name': i, 'id': i} for i in df.columns]
    ),
    dcc.Graph(figure=pie_chart),
    dcc.Graph(figure=bar_chart)
])

if __name__ == '__main__':
    app.run_server(debug=True)