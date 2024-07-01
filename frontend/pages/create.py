import flask
import requests
import dash
from dash import html, dcc

def get_all_roles():
    request_url = "http://127.0.0.1:8000/roles.json"
    response = requests.get(request_url).json()
    roles = {}
    for role in response:
        roles[role['role_id']] = role['role_name']
    return roles

print(get_all_roles())
dash.register_page(__name__, 
                   path = '/create',
                   name = 'Create Employee')

layout = html.Div([
    html.H1('Create Employee'),
    html.Form(
        # action="/post",
        method="post",
        # action="http://localhost:8000/employees/",
        action="/createemployee",
        children = [
            dcc.Input(
                id="employee_first_name".format("text"),
                type="text",
                name="employee_first_name",
                placeholder="First Name".format("text"),
            ),
            dcc.Input(
                id="employee_middle_name".format("text"),
                type="text",
                name="employee_middle_name",
                placeholder="Middle Name".format("text"),
            ),
            dcc.Input(
                id="employee_last_name".format("text"),
                type="text",
                name="employee_last_name",
                placeholder="Last Name".format("text"),
            ),
            html.Select(id="role",
                       name="role",
                       children = [
                           html.Option(
                               f"{value}",
                               value = key,
                           ) for key, value in get_all_roles().items()
            ]
            ),
            dcc.Input(
                id="started_on",
                type="datetime-local",
                name="started_on",
                placeholder="Started On".format("text"),
            ),
            # dcc.DatePickerSingle(
            #     id="started_on",
            #     placeholder="Started On".format("text"),
            #     display_format='MMMM DD, YYYY'
            # ),
            html.Button('Submit', type='submit', id='submit-val', n_clicks=0),
        ]
    )
])

