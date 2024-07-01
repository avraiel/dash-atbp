import flask
from flask import flash
import dash
import requests
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

CONTENT_STYLE = {
    "margin-top": "1em",
    "margin-left": "1em",
    "margin-right": "1em",
    "padding": "1em 1em",
}

app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.secret_key = 'wow so secret'

app.layout = html.Div([
    html.H1('Navigation Links'),
    html.Div([
        html.Div(
            dcc.Link(f"{page['name']}", href=page["relative_path"])
        ) for page in dash.page_registry.values()
    ]),
    html.Hr(),      
    dash.page_container
], style = CONTENT_STYLE)




# NOTE: Delete Employee, sends reqeust to APi
@app.server.route('/deleteemployee', methods=['POST'])
def delete_employee():
    delete_pk = flask.request.form['delete_pk']
    if delete_pk:
        requests.delete("http://127.0.0.1:8000/employees/" + delete_pk)
        # TODO: Add notification
        # flash('Invalid password provided', 'error')
        return flask.redirect('/employees')
    return flask.redirect('/employees')

# NOTE: Create Employee, sends request to API
@app.server.route('/createemployee', methods=['POST'])
def create_employee():
    create_url = "http://127.0.0.1:8000/employees/"
    requests.post(create_url, json = flask.request.form)
    return flask.redirect('/employees')


# NOTE: Get Employee
@app.server.route('/employee_get/request/', methods=['POST'])
def get_employee():
    employee_pk = flask.request.form['employee_pk']
    request_url = "http://127.0.0.1:8000/employees/" + str(employee_pk) + ".json"
    response = requests.get(request_url)
    return flask.redirect('/employees')

# NOTE: Update Employee Handler
@app.server.route('/updateemployee', methods=['POST'])
def update_employee():
    print(flask.request.form)
    employee_pk = flask.request.form['employee_pk']
    request_url = "http://127.0.0.1:8000/employees/" + str(employee_pk) + "/"
    requests.put(request_url, json = flask.request.form)
    return flask.redirect('/employees')


if __name__ == '__main__':
    app.run(debug=True, dev_tools_props_check=False)