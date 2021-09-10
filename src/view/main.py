import dash
import dash_auth

from layout_components import navbar_component, alert_is_logged_component, tabs_component
from layout_components import first_tab_component, second_tab_component, third_tab_component, first_tab_table
from layout_components import first_tab_button
import plotly.io as pio

import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output

from secret import PASSWORDS

pio.renderers.default = 'browser'

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])

""" LAYOUT """

app.layout = html.Div([
    navbar_component(),
    alert_is_logged_component(),
    tabs_component(),
], style={
    'margin-left': '20px',
    'margin-right': '20px'
})


@app.callback(Output("content", "children"), [Input("tabs", "active_tab")])  # callback of tabs_component
def switch_tab(at):
    if at == "tab-1":
        return first_tab_component()
    elif at == "tab-2":
        return second_tab_component()
    elif at == "tab-3":
        return third_tab_component()
    return html.P("This shouldn't ever be displayed...")


@app.callback(
    Output("table_id", "children"), [Input("loading_table", "n_clicks")]
)
def load_output(n_clicks):
    if n_clicks:
        return first_tab_table()
    return first_tab_button()


""" AUTHENTIFICATION """

auth = dash_auth.BasicAuth(
    app,
    PASSWORDS
)

""" RUN APP """

app.run_server(debug=True)
