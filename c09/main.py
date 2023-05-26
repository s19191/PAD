import pandas as pd
from dash import Dash, dcc, html, dash_table
from dash.dependencies import Input, Output
import plotly.express as px

df = pd.read_csv('winequelity.csv')

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Wine Quality Analysis"),

    html.H3("Select a model type:"),
    dcc.RadioItems(
        id='model-type',
        options=[
            {'label': 'Regression', 'value': 'regression'},
            {'label': 'Classification', 'value': 'classification'}
        ],
        value='regression',
        labelStyle={'display': 'inline-block'}
    ),

    html.H3("Select a variable:"),
    dcc.Dropdown(
        id='variable-dropdown',
        options=[{'label': col, 'value': col} for col in df.columns],
        value=df.columns[1]
    ),

    html.Div(id='graph-container'),

    dash_table.DataTable(df.to_dict('records'), [{"name": i, "id": i} for i in df.columns])
])


@app.callback(
    Output('graph-container', 'children'),
    [Input('model-type', 'value'),
     Input('variable-dropdown', 'value')]
)
def display_graph(model_type, variable):
    if model_type == 'regression':
        fig = px.scatter(df, x=variable, y='pH', color='quality')
        fig.update_layout(title=f"Regression: pH with {variable}")
    else:
        fig = px.histogram(df, x=variable, color='target')
        fig.update_layout(title=f"Classification: Target with {variable}")

    return dcc.Graph(figure=fig)


app.run_server(debug=True)
