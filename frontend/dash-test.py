# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import requests

app = Dash(__name__)

## TODO: Modify to accept JSON data into dash app

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
# df = pd.DataFrame({
#     "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
#     "Amount": [4, 1, 2, 2, 4, 5],
#     "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
# })
link = requests.get("http://127.0.0.1:8000/employees.json").json()
# print(link, end="\n")
df = pd.read_json("http://127.0.0.1:8000/employees.json")
print(df)
# link = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu").json()


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

if __name__ == '__main__':
    app.run(debug=True)
