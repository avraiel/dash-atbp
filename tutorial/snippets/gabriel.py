# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import requests
from urllib.error import URLError

from django_plotly_dash import DjangoDash
app = DjangoDash("gabriel")

## IMPORTANT: To run this application, you need to run two django servers. One acts as a place to ping for the data, the second one is to act as the frontend. It's a scuffed version of backend and frontend honestly.

retrieved = True
# Cannot read data from self on the same port, results into IMPORTANT text above
try:
    df = pd.read_json("http://127.0.0.1:8000/employees.json")
except URLError:
    retrieved = False 

if retrieved:
    print("I retrieved data!")
    fig = px.histogram(df, x="employee_status", color="employee_status")

    app.layout = html.Div(children=[
        html.H1(children='Hello Dash World!'),

        html.Div(children='''
            Dash: A web application framework for your data.
        '''),

        dcc.Graph(
            id='example-graph',
            figure=fig
        )
    ])
else:
    app.layout = html.Div(children=[
        html.H1(children='Hello Dash World! No Graph'),

        html.Div(children='''
            Dash: A web application framework for your data.
        '''),
    ])

# if __name__ == '__main__':
#     app.run(debug=True)
