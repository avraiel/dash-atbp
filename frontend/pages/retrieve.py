import json
import requests
import flask
import dash
from dash import html, dcc

dash.register_page(__name__,
                    path_template='/employee/<employee_id>',
                    name = "Retrieve")

def layout(employee_id=None, **kwargs):
    if employee_id is not None:
        base_url = "http://127.0.0.1:8000/employees/"
        request_url = base_url + employee_id + '.json'
        print(request_url)
        response = requests.get(request_url).json()
        return html.Div([
            html.P(f"The user requested data for employee of employee ID: {employee_id}."),
            html.Br(),
            html.P(f"The data is as follows {response}")]
        )
    else:
        return html.Div(
            f"The user did not request for any employee"
        )
