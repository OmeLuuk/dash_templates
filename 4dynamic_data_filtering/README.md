# Dynamic Data Filtering and Display Template

## Overview

This template, part of the `dash_templates` collection, is designed to demonstrate dynamic data filtering and display using Dash. It features interactive components like dropdowns and checklists to filter stock data, with the results dynamically reflected in both a data table and graphs. This template is ideal for understanding real-time data manipulation and visualization in web applications.

## Prerequisites

Before running this template, ensure you have followed the initial setup steps in the main `dash_templates` README. This includes installing Python, setting up a virtual environment, and installing necessary packages like Dash, Pandas, and Plotly (for this template `pip install dash dash-bootstrap-components pandas plotly`).

## Key Concepts

- **Dynamic Filtering**: Users can interact with dropdowns and checklists to filter data based on criteria like stock symbols and categories. The data table and graphs update in response to these selections.
- **Callbacks**: In Dash, callbacks link user interactions with input components to output components. They listen to input changes and update outputs accordingly.
- **Data Handling**: This template uses Pandas for data manipulation, showcasing how to process and visualize data from sources like Excel files.

## Running the App

To run this app:
1. Activate your virtual environment (`(.venv)` should be visible in your command line prompt).
2. Run the script by executing: `(.venv) PS D:\dev\dash_templates> python .\4dynamic_data_filtering\dynamic_data_filtering.py`.

## Interacting with the App

Upon running the app, you can:

1. **Filter Data**: Use the dropdown menus and checklist to filter stock data based on symbols and categories.
2. **View Results**: Observe how the data table and graphs update in real-time to reflect your selections.
3. **Explore Interactivity**: Experiment with different combinations of filters to see how dynamic and responsive Dash apps can be.

This template is a powerful example of creating interactive data dashboards with Dash, perfect for business analytics, financial data analysis, and more.