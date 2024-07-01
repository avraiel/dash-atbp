import flask

import dash
from dash import html, dcc

dash.register_page(__name__, 
                   path = '/create',
                   name = 'Create and Update')

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
            dcc.Input(
                id="role",
                type="number",
                name="role",
                placeholder="Role".format("text"),
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

