import pandas as pd
from dash import Dash, dcc, html, dash_table
from dash.dependencies import Input, Output

df = pd.read_csv('winequelity.csv', delimiter=",")

app = Dash(__name__)

app.layout = dash_table.DataTable(df.to_dict('records'), [{"name": i, "id": i} for i in df.columns])

app.layout = html.Div(children=[
    html.Div([
        html.Label([
            'Select model'
        ]),
        dcc.RadioItems(['Regression', 'Classification'], id='model'),
        html.Div(id='output'),

    ], style={'color': 'black'}
    ),

    dash_table.DataTable(df.to_dict('records'), [{"name": i, "id": i} for i in df.columns])
])

app.run_server(debug=True)


# @app.callback(Output(component_id='output', component_property='children'),
#               Input(component_id='model', component_property='value'))
# def update_output_div(input_value):
#     return f'Output: {input_value}'