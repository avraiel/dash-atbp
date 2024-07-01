import flask
import requests
import dash
from dash import html, dcc
from pages.create import get_all_roles

dash.register_page(__name__, 
                   path_template = '/update/<employee_id>',
                   name = 'Update')

def layout(employee_id=None, **kwargs):
    layout = html.Div()

    if employee_id is not None:
        base_url = "http://127.0.0.1:8000/employees/"
        request_url = base_url + employee_id + '.json'
        response = requests.get(request_url).json()
        print(response['started_on'])
        layout = html.Div([
            html.H1('Update Employee'),
            # NOTE: Alternative form for PUT requests 
            html.Form(
                action="/updateemployee",
                method="post",
                # action=f"{request_url}",
                children = [
                    dcc.Input(
                        id="employee_pk",
                        type="hidden",
                        name="employee_pk",
                        value=employee_id,
                    ),
                    dcc.Input(
                        id="employee_first_name".format("text"),
                        type="text",
                        name="employee_first_name",
                        value=f"{response['employee_first_name']}",
                        placeholder="First Name".format("text"),
                    ),
                    dcc.Input(
                        id="employee_middle_name".format("text"),
                        type="text",
                        name="employee_middle_name",
                        value=f"{response['employee_middle_name']}",
                        placeholder="Middle Name".format("text"),
                    ),
                    dcc.Input(
                        id="employee_last_name".format("text"),
                        type="text",
                        name="employee_last_name",
                        value=f"{response['employee_last_name']}",
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
                        value=response['started_on'],
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
    return layout

