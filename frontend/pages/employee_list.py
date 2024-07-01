import json
import requests
import flask
import dash
from dash import html, dcc

dash.register_page(__name__,
                    path='/employees',
                    name = "Employee List")

def get_role_name(role_id):
    request_url = "http://127.0.0.1:8000/roles/" + str(role_id) + ".json"
    response = requests.get(request_url).json()
    role_name = response['role_name']
    return role_name

def layout(**kwargs):
    request_url = "http://127.0.0.1:8000/employees.json"
    response = requests.get(request_url).json()
    
    layout = html.Div([
        html.Table([
            html.Tr([
                html.Td(f'{employee['employee_first_name']} {employee['employee_last_name']}'),
                html.Td([f'{get_role_name(employee['role'])}'],
                        style = {"padding" : "10px"}),
                html.Td([
                    # Go to Edit Page
                    html.A(
                        href=f"/update/{employee['employee_id']}",
                        children = [
                            html.Button('Edit', type='submit', id='details-emp', n_clicks=0),
                        ],
                        style = {"display": "inline-block", "padding" : "10px"}
                    ),
                    # Get Details
                    html.A(
                        href=f"/employee/{employee['employee_id']}",
                        children = [
                            html.Button('Details', type='submit', id='details-emp', n_clicks=0),
                        ],
                        style = {"display": "inline-block", "padding" : "10px"}
                    ),
                    # NOTE: DELETE Form
                    html.Form(
                        # action="/post",
                        method="post",
                        action="/deleteemployee",
                        children = [
                            dcc.Input(
                                id="delete_pk",
                                type="hidden",
                                name="delete_pk",
                                value=f'{employee['employee_id']}'
                            ),
                            html.Button('Delete', type='submit', id='delete-emp', n_clicks=0),
                        ],
                        style = {"display": "inline-block", "padding" : "10px"}
                    )
                ]
                )
            ], # Table styles
            style = {"border-bottom": "1px solid black"}
            ) for employee in response
        ]
        ) 
    ])
    return layout