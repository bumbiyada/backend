import requests
import pandas as pd

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_auth
from dash.dependencies import Input, Output

# import plotly.express as px
import plotly.io as pio
import plotly.graph_objs as go

pio.renderers.default = 'browser'

# request and data frame manipulations
response = requests.get('http://localhost:8000/api/v1/list/')

df = pd.json_normalize(response.json())

""" SCATTERS """

# first scatter

# magic
df_yes = pd.DataFrame(columns=['Stage_user','Is_done'])
df_no = pd.DataFrame(columns=['Stage_user','Is_done'])
df_2 = df.loc[:, 'Stage_user':'Is_done':2]
for i in range(len(df_2)):
    done_var = df_2['Is_done'].iloc[i]
    user_var = df_2['Stage_user'].iloc[i]
    if done_var == 0:
        df_no = df_no.append({'Stage_user': user_var, 'Is_done': done_var},ignore_index=True)
    elif done_var == 1:
        df_yes = df_yes.append({'Stage_user': user_var, 'Is_done': done_var},ignore_index=True)
sum_yes = df_yes['Stage_user'].value_counts()
sum_no = df_no['Stage_user'].value_counts()
sum_counts = df['Stage_user'].value_counts()

list_my = sum_counts.index.to_list()
list_my[0] = 'Исполнитель не указан'
sum_counts.index = list_my

fig = go.Figure()
fig.add_trace(go.Bar(name='Выполнена', x=sum_yes.index, y=sum_yes))
fig.add_trace(go.Bar(name='Не выполнена', x=sum_no.index, y=sum_no))
fig.update_layout(
                    legend_title_text="Задача Выполнена?",
                    margin_l=30,
                    margin_r=30,
                    margin_t=20,
                    margin_b=0,
                    width=1400,
                    barmode='stack')
fig.update_yaxes(title_text="Количество выполненных задач")

# second
sum_counts_1 = df['Stage_name'].value_counts().sort_index()
fig_1 = go.Figure()
fig_1.add_trace(go.Pie(values=sum_counts_1, labels=sum_counts_1.index, textinfo='label+percent'))
fig_1.update_layout(legend_title_text="Этапы документа",
                    margin_l=0,
                    margin_r=0,
                    margin_t=20,
                    margin_b=0)

# third
sum_counts_2 = df['Is_aborted'].value_counts().sort_index()
list_my = sum_counts_2.index.to_list()
list_my[0] = 'нет'
list_my[1] = 'да'
sum_counts_2.index = list_my
fig_2 = go.Figure()
fig_2.add_trace(go.Pie(values=sum_counts_2, labels=sum_counts_2.index, textinfo='label+percent'))
fig_2.update_layout(legend_title_text="Задача отменена?",
                    margin_l=0,
                    margin_r=0,
                    margin_t=20,
                    margin_b=0)

# forth
sum_counts_3 = df['Is_done'].value_counts().sort_index()
list_my = sum_counts_3.index.to_list()
list_my[0] = 'нет'
list_my[1] = 'да'
sum_counts_3.index = list_my
fig_3 = go.Figure()
fig_3.add_trace(go.Pie(values=sum_counts_3, labels=sum_counts_3.index, textinfo='label+percent'))
fig_3.update_layout(legend_title_text="задача выполнена?",
                    margin_l=0,
                    margin_r=0,
                    margin_t=20,
                    margin_b=0)

# fifth
sum_counts_4 = df['Marked_on_delete'].value_counts().sort_index()
list_my = sum_counts_4.index.to_list()
list_my[0] = 'нет'
list_my[1] = 'да'
sum_counts_4.index = list_my
fig_4 = go.Figure()
fig_4.add_trace(go.Pie(values=sum_counts_4, labels=sum_counts_4.index, textinfo='label+percent'))
fig_4.update_layout(legend_title_text="пометка на удаление",
                    margin_l=0,
                    margin_r=0,
                    margin_t=20,
                    margin_b=0)

# sixth
sum_counts_5 = df['Foiv'].value_counts().sort_index()
fig_5 = go.Figure()
fig_5.add_trace(go.Pie(values=sum_counts_5, labels=sum_counts_5.index, textinfo='label+percent'))
fig_5.update_layout(legend_title_text="Вид Фоива",
                    margin_l=0,
                    margin_r=0,
                    margin_t=20,
                    margin_b=0)

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

""" LAYOUT """

# tabs

tabs = dbc.Row(
    [
        dbc.Tabs(
            [
                dbc.Tab(label="Сотрудники и задачи", tab_id="tab-1", style={'width': '100%'}),
                dbc.Tab(label="Этапы + Фоив", tab_id="tab-2"),
                dbc.Tab(label="Булевы значения", tab_id="tab-3"),
            ],
            id="tabs",
            active_tab="tab-1",
            style={'width': '100%'}
        ),
        html.Div(id="content", style={'width': '100%'}),
    ]
)


@app.callback(Output("content", "children"), [Input("tabs", "active_tab")])
def switch_tab(at):
    if at == "tab-1":
        return first_row
    elif at == "tab-2":
        return second_row
    elif at == "tab-3":
        return third_row
    return html.P("This shouldn't ever be displayed...")


SOURCE_IMAGE = 'https://sverdlovsk.roskazna.gov.ru/upload/C%20Днем%20образования%20%20Российского%20казначейства!(' \
               '2579511_373_08_12_2015).JPG '
navbar = dbc.Row(
    dbc.Navbar([
        dbc.Col(html.Img(
            src=SOURCE_IMAGE,
            height='50px')),
        dbc.Col(dbc.NavbarBrand('Дашборд', className='ml-2')),
    ], fixed='top')
)

alert = dbc.Row(
    dbc.Col(
        dbc.Alert("Вы успешно авторизовались", color="success", dismissable=True, is_open=True)
    ))

first_row = dbc.Row(
    dbc.Col([
        html.H3('Исполнители', style={'text-align': 'center'}),
        dcc.Graph(figure=fig)]),
)

second_row = dbc.Row([
    dbc.Col([
        html.H3('Этапы документа', style={'text-align': 'center'}),
        dcc.Graph(figure=fig_1, style={'margin-top': '0px'})], style={'width': '50%', 'background-color': '#aebcc2'}),
    dbc.Col([
        html.H3('ФОИВ', style={'text-align': 'center'}),
        dcc.Graph(figure=fig_5)], style={'width': '50%', 'background-color': '#aebcc2'}),
], style={'display': 'flex', 'height': '700px'})

third_row = dbc.Row([
    dbc.Col([
        html.H3('Отменена', style={'text-align': 'center'}),
        dcc.Graph(figure=fig_2)], style={'width': '40%', 'background-color': '#aebcc2'}),
    dbc.Col([
        html.H3('Выполнена', style={'text-align': 'center'}),
        dcc.Graph(figure=fig_3)], style={'width': '30%', 'background-color': '#aebcc2'}),
    dbc.Col([
        html.H3('Отмечена на удаление', style={'text-align': 'center'}),
        dcc.Graph(figure=fig_4)], style={'width': '30%', 'background-color': '#aebcc2'}),
])

app.layout = html.Div([
    navbar,
    alert,
    tabs,
], style={
    'margin-left': '20px',
    'margin-right': '20px'
})

""" AUTHENTIFICATION """

auth = dash_auth.BasicAuth(
    app,
    {'123': '123',
     'admin': 'password'}
)

app.run_server(debug=True)
