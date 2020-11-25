import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import numpy as np
import plotly.graph_objs as go

import plotly.express as px

# the style arguments for the sidebar.
SIDEBAR_STYLE = {
    'position': 'fixed',
    'top': 0,
    'left': 0,
    'bottom': 0,
    'width': '25%',
    'padding': '20px 10px',
    'background-color': '#f8f9fa'
}

# the style arguments for the main content page.
CONTENT_STYLE = {
    'margin-left': '25%',
    'margin-right': '5%',
    'padding': '20px 10p'
}

TEXT_STYLE = {
    'textAlign': 'center',
    'color': '#191970'
}

CARD_TEXT_STYLE = {
    'textAlign': 'center',
    'color': '#0074D9'
}

controls = dbc.FormGroup(
    [
        html.P('Escolha um candidato', style={
            'textAlign': 'center'
        }),
        dcc.Dropdown(
            id='candidato-dropdown',
            options=[{
                'label': 'Marilia Arraes',
                'value': '1'
            }, 
            {
                'label': 'João Campos',
                'value': '2'
            },
            {
                'label': 'Mendonça Filho',
                'value': '3'
            },
            {
                'label': 'Delegada Patricia',
                'value': '4'
            },
            ],
        ),
        html.Br(),
        html.Br(),
    ]
)

sidebar = html.Div(
    [
        html.H2('Candidatos a prefeitura do Recife', style=TEXT_STYLE),
        html.Hr(),
        controls
    ],
    style=SIDEBAR_STYLE,
)

content_first_row = html.Div(id = 'my-first-row')

content_second_row = html.Div(id='my-second-row')

content_third_row = html.Div(
   html.H1('Tweets Positivos')
)

content_fourth_row = html.Div(
    html.H1('Tweets Negativos')
)

content = html.Div(
    [
        html.H2('Análise de sentimento de tweets dos candidatos a prefeitura de Recife', style=TEXT_STYLE),
        html.H3('Primeiro turno', style={'textAlign': 'center'}),
        html.Hr(),
        content_first_row,
        content_second_row,
        content_third_row,
        content_fourth_row
    ],
    style=CONTENT_STYLE
)

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = html.Div([sidebar, content])


@app.callback(
    dash.dependencies.Output(component_id = 'my-first-row', component_property='children'),
    [dash.dependencies.Input(component_id='candidato-dropdown', component_property= 'value')]
)
def update_output(value):
    if (value == '1'):
        df = px.data.iris()
        fig = px.scatter(df, x="sepal_width", y="sepal_length")
        return (
            dcc.Graph(figure=fig)
        )
    else:
        return ''


@app.callback(
    dash.dependencies.Output(component_id = 'my-second-row', component_property='children'),
    [dash.dependencies.Input(component_id='candidato-dropdown', component_property= 'value')]
)
def update_output(value):
    if (value == '1'):
        df = pd.read_csv('./df_resultado_palavra_chave')
        fig = px.scatter(df, x="sepal_width", y="sepal_length")
        return (
            dcc.Graph(figure=fig)
        )
    else:
        return ''



if __name__ == '__main__':
    app.run_server(port='8085')

