import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from secret import SOURCE_IMAGE
from scatters import Scatters

import requests
import pandas as pd

response = requests.get('http://localhost:8000/api/v1/list/')
data = pd.json_normalize(response.json())


""" LAYOUT COMPONENTS """


def tabs_component():
    """ Component is responsible for tabs at the top of the screen """
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
    return tabs


def navbar_component():
    """ Component is responsible for navbar at the top of the screen """
    navbar = dbc.Row(
        dbc.Navbar([
            dbc.Col(html.Img(
                src=SOURCE_IMAGE,
                height='50px')),
            dbc.Col(dbc.NavbarBrand('Дашборд', className='ml-2')),
        ], fixed='top')
    )
    return navbar


def alert_is_logged_component():
    """ Component is responsible for message about succeed login """
    alert = dbc.Row(
        dbc.Col(
            dbc.Alert("Вы успешно авторизовались", color="success", dismissable=True, is_open=True)
        ))
    return alert


def first_tab_component():
    """ Component is responsible for First tab that contains stage_user_bar scatter """
    first_tab = dbc.Row(
        dbc.Col([
            html.H3('Исполнители', style={'text-align': 'center'}),
            dcc.Graph(figure=Scatters.stage_user_bar(data))]),
    )
    return first_tab


def second_tab_component():
    """ Component is responsible for Second tab that contains stage_name_pie and foiv_pie scatters """
    second_tab = dbc.Row([
        dbc.Col([
            html.H3('Этапы документа', style={'text-align': 'center'}),
            dcc.Graph(
                figure=Scatters.stage_name_pie(data),
                style={'margin-top': '0px'})],
                style={'width': '50%', 'background-color': '#aebcc2'}),
        dbc.Col([
            html.H3('ФОИВ', style={'text-align': 'center'}),
            dcc.Graph(
                figure=Scatters.foiv_pie(data))],
                style={'width': '50%', 'background-color': '#aebcc2'}),
    ], style={'display': 'flex', 'height': '700px'})
    return second_tab


def third_tab_component():
    """ Component is responsible for Third tab that contains is_aborted, is_done, marked_on_delete pie scatters """
    third_tab = dbc.Row([
        dbc.Col([
            html.H3('Отменена', style={'text-align': 'center'}),
            dcc.Graph(
                figure=Scatters.is_aborted_pie(data))],
                style={'width': '40%', 'background-color': '#aebcc2'}),
        dbc.Col([
            html.H3('Выполнена', style={'text-align': 'center'}),
            dcc.Graph(
                figure=Scatters.is_done_pie(data))],
                style={'width': '30%', 'background-color': '#aebcc2'}),
        dbc.Col([
            html.H3('Отмечена на удаление', style={'text-align': 'center'}),
            dcc.Graph(
                figure=Scatters.marked_on_delete_pie(data))],
                style={'width': '30%', 'background-color': '#aebcc2'}),
    ])
    return third_tab
