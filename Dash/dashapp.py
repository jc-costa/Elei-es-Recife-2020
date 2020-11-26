import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import numpy as np
import plotly.graph_objs as go
import pandas as pd
import dash_table
import plotly.express as px
import matplotlib.pyplot as plt
import base64
import os
from random import randrange

df = pd.read_csv('./data/df_resultado_final_tweets_sem_stopwords')
df.drop(columns={'Unnamed: 0'}, inplace=True)

dfOriginal = pd.read_csv('./data/df_resultado_final_tweets_original')
dfOriginal.drop(columns={'Unnamed: 0'}, inplace=True)

dfMarilia = df.loc[df['palavra_chave'] == 'Marília Arraes', :]
dfMariliaOriginal = dfOriginal.loc[df['palavra_chave'] == 'Marília Arraes', :]

dfJoao = df.loc[df['palavra_chave'] == 'João Campos', :]
dfJoaoOriginal = dfOriginal.loc[df['palavra_chave'] == 'João Campos', :]

dfMendonca = df.loc[df['palavra_chave'] == 'Mendonça Filho', :]
dfMendoncaOriginal = dfOriginal.loc[df['palavra_chave'] == 'Mendonça Filho', :]

dfDelegada = df.loc[df['palavra_chave'] == 'Delegada Patricia', :]
dfDelegadaOriginal = dfOriginal.loc[df['palavra_chave'] == 'Delegada Patricia', :]

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

TEXT_TWEET_POSITIVO = {
     'textAlign': 'center',
    'color': '#1a5678',
    'font': 'Arial',
    'font-size': '25px'
}

TEXT_TWEET_NEGATIVO = {
    'textAlign': 'center',
    'color': '#a13045',
    'font': 'Arial',
    'font-size': '25px'
}

TEXT_TWEET = {
   
}


CARD_TEXT_STYLE = {
    'textAlign': 'center',
    'color': '#0074D9'
}

TEXT_TITLE = {
    'textAlign': 'center',
    'color': 'black',
    'font-size': '35px'
}

# Dropdown
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

# Sidebar
sidebar = html.Div(
    [
        html.H2('Candidatos a prefeitura do Recife', style=TEXT_STYLE),
        html.Hr(),
        controls
    ],
    style=SIDEBAR_STYLE,
)

# Content

content_first_row = html.Div(id = 'my-first-row')

content_second_row = html.Div(id='my-second-row')

content_third_row = html.Div(id='my-third-row')

content_fourth_row = html.Div(id='my-fourth-row')

content = html.Div(
    [
        html.H2('Análise de sentimento de tweets sobre os(as) candidatos(as) à Prefeitura de Recife', style=TEXT_STYLE),
        html.H3('Primeiro turno', style={'textAlign': 'center'}),
        html.Hr(),
        content_first_row,
        content_second_row,
        content_third_row,
        content_fourth_row
    ],
    style=CONTENT_STYLE
)

# app
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = html.Div([sidebar, content])

### Controller first row
### Aqui irá ficar o plot com a quantidade de tweets para cada classe

@app.callback(
    dash.dependencies.Output(component_id = 'my-first-row', component_property='children'),
    [dash.dependencies.Input(component_id='candidato-dropdown', component_property= 'value')]
)
def update_output(value):
    if (value == '1'): #Marilia
        fig = px.bar(dfMarilia['classificacao'].value_counts(),
                     labels=dict(index='Classificação', value='Quantidade dos tweets')
                    )
        return (dcc.Graph(figure=fig))
    elif (value == '2'): #João
        fig = px.bar(dfJoao['classificacao'].value_counts(),
                     labels=dict(index='Classificação', value='Quantidade dos tweets')
                    )
        return (dcc.Graph(figure=fig))
    elif (value == '3'): #Mendonça Filho
        fig = px.bar(dfMendonca['classificacao'].value_counts(),
                     labels=dict(index='Classificação', value='Quantidade dos tweets')
                    )
        return (dcc.Graph(figure=fig))
    elif (value == '4'): ### Delegada
        fig = px.bar(dfDelegada['classificacao'].value_counts(),
                     labels=dict(index='Classificação', value='Quantidade dos tweets')
                    )
        return (dcc.Graph(figure=fig))
    else:
        fig = px.bar(
        df['classificacao'].value_counts(),
        labels=dict(index='Classificação', value='Quantidade dos tweets'),
        title = 'Quantidade dos tweets em geral'
        )
        fig.show() 
        return (
           dcc.Graph(figure=fig)
        )

### Controller second row
@app.callback(
    dash.dependencies.Output(component_id = 'my-second-row', component_property='children'),
    [dash.dependencies.Input(component_id='candidato-dropdown', component_property= 'value')]
)
def update_output(value):
    if (value == '1'): #Marilia
        path_folder = '/wordclouds/Marilia/'
        path_img = path_folder + 'juntos.png'
        layout = {'title': {'text':'DISPLAY ME!'}}
        renderIMG = html.Div([
            html.Img(src= app.get_asset_url(path_img), style={'height':'50%', 'width':'900px'}),
        ])
        return renderIMG
    elif (value == '2'): #João Campos
        path_folder = '/wordclouds/joao/'
        path_img = path_folder + 'juntos.png'
        renderIMG = html.Div([
            html.Img(src= app.get_asset_url(path_img), style={'height':'50%', 'width':'1000px'}),
        ])
        return renderIMG
    elif (value == '3'):
        path_folder = '/wordclouds/mendonca/'
        path_img = path_folder + 'juntos.png'
        renderIMG = html.Div([
            html.Img(src= app.get_asset_url(path_img), style={'height':'50%', 'width':'1100px'}),
        ])
        return renderIMG
        
    elif (value == '4'):
        path_folder = '/wordclouds/Delegada/'
        path_img = path_folder + 'juntas.png'
        renderIMG = html.Div([
            html.Img(src= app.get_asset_url(path_img), style={'height':'50%', 'width':'700px'}),
        ])
        return renderIMG
        
    else:
        dictRanking = []
        dictRanking.append({'Candidato': 'Marília Arraes', 'Positivo': dfMarilia['classificacao'].value_counts()['Positivo'], 'Neutro': dfMarilia['classificacao'].value_counts()['Neutro'], 'Negativo':dfMarilia['classificacao'].value_counts()['Negativo'] })
        dictRanking.append({'Candidato': 'João Campos', 'Positivo': dfJoao['classificacao'].value_counts()['Positivo'], 'Neutro': dfJoao['classificacao'].value_counts()['Neutro'], 'Negativo':dfJoao['classificacao'].value_counts()['Negativo']})
        dictRanking.append({'Candidato': 'Delegada Patricia', 'Positivo': dfDelegada['classificacao'].value_counts()['Positivo'], 'Neutro': dfDelegada['classificacao'].value_counts()['Neutro'], 'Negativo':dfDelegada['classificacao'].value_counts()['Negativo'] })
        dictRanking.append({'Candidato': 'Mendonça Filho', 'Positivo': dfMendonca['classificacao'].value_counts()['Positivo'], 'Neutro': dfMendonca['classificacao'].value_counts()['Neutro'], 'Negativo':dfMendonca['classificacao'].value_counts()['Negativo'] })
        dfRanking = pd.DataFrame(dictRanking)
        fig = px.bar(dfRanking, x = 'Candidato', y = ['Positivo','Neutro', 'Negativo'], title='Ranking das análises', labels=dict(index='Candidato', value='Quantidade dos tweets'))
        return dcc.Graph(figure=fig)

# Controlelr third row
### Aqui irá ficar os tweets positivos
@app.callback(
    dash.dependencies.Output(component_id = 'my-third-row', component_property='children'),
    [dash.dependencies.Input(component_id='candidato-dropdown', component_property= 'value')]
)

def update_output(value):
    if (value == '1'): #Marilia
        dfMariliaOriginalPositivo = dfMariliaOriginal.loc[dfMariliaOriginal['classificacao'] == 'Positivo', :]
        tamanhoDF = len(dfMariliaOriginalPositivo['tweet'])
        return (
            html.Div([
                html.H1('Tweets positivos', style=TEXT_TITLE),
                html.Br(),
                html.Br(),
                html.Br(),
                html.H3(dfMariliaOriginalPositivo['tweet'].values[randrange(tamanhoDF)], style=TEXT_TWEET_POSITIVO),
                html.Br(),
                html.H3(dfMariliaOriginalPositivo['tweet'].values[randrange(tamanhoDF)], style=TEXT_TWEET_POSITIVO),
                html.Br(),
                html.H3(dfMariliaOriginalPositivo['tweet'].values[randrange(tamanhoDF)], style=TEXT_TWEET_POSITIVO),
                html.Br(),
                html.H3(dfMariliaOriginalPositivo['tweet'].values[randrange(tamanhoDF)], style=TEXT_TWEET_POSITIVO),
                html.Br(),
            ])
        )
    elif (value == '2'): #João
        dfJoaoOriginalPositivo = dfJoaoOriginal.loc[dfJoaoOriginal['classificacao'] == 'Positivo', :]
        tamanhoDF = len(dfJoaoOriginalPositivo['tweet'])
        return (
            html.Div([
                html.H1('Tweets positivos', style=TEXT_TITLE),
                html.Br(),
                html.Br(),
                html.Br(),
                html.H3(dfJoaoOriginalPositivo['tweet'].values[randrange(tamanhoDF)], style=TEXT_TWEET_POSITIVO),
                html.Br(),
                html.H3(dfJoaoOriginalPositivo['tweet'].values[randrange(tamanhoDF)], style=TEXT_TWEET_POSITIVO),
                html.Br(),
                html.H3(dfJoaoOriginalPositivo['tweet'].values[randrange(tamanhoDF)], style=TEXT_TWEET_POSITIVO),
                html.Br(),
                html.H3(dfJoaoOriginalPositivo['tweet'].values[randrange(tamanhoDF)], style=TEXT_TWEET_POSITIVO),
                html.Br(),
            ])
        )
    elif (value == '3'): #Mendonça Filho
        dfMendoncaOriginalPositivo = dfMendoncaOriginal.loc[dfMendoncaOriginal['classificacao'] == 'Positivo', :]
        tamanhoDF = len(dfMendoncaOriginalPositivo['tweet'])
        return (
            html.Div([
                html.H1('Tweets positivos', style=TEXT_TITLE),
                html.Br(),
                html.Br(),
                html.Br(),
                html.H3(dfMendoncaOriginalPositivo['tweet'].values[randrange(tamanhoDF)], style=TEXT_TWEET_POSITIVO),
                html.Br(),
                html.H3(dfMendoncaOriginalPositivo['tweet'].values[randrange(tamanhoDF)], style=TEXT_TWEET_POSITIVO),
                html.Br(),
                html.H3(dfMendoncaOriginalPositivo['tweet'].values[randrange(tamanhoDF)], style=TEXT_TWEET_POSITIVO),
                html.Br(),
                html.H3(dfMendoncaOriginalPositivo['tweet'].values[randrange(tamanhoDF)], style=TEXT_TWEET_POSITIVO),
                html.Br(),
            ])
        )
    elif (value == '4'): ### Delegada
        dfDelegadaPositivo = dfDelegadaOriginal.loc[dfDelegadaOriginal['classificacao'] == 'Positivo', :]
        tamanhoDF = len(dfDelegadaPositivo['tweet'])
        return (
            html.Div([
                html.H1('Tweets positivos', style=TEXT_TITLE),
                html.Br(),
                html.Br(),
                html.Br(),
                html.H3(dfDelegadaPositivo['tweet'].values[randrange(tamanhoDF)], style=TEXT_TWEET_POSITIVO),
                html.Br(),
                html.H3(dfDelegadaPositivo['tweet'].values[randrange(tamanhoDF)], style=TEXT_TWEET_POSITIVO),
                html.Br(),
                html.H3(dfDelegadaPositivo['tweet'].values[randrange(tamanhoDF)], style=TEXT_TWEET_POSITIVO),
                html.Br(),
                html.H3(dfDelegadaPositivo['tweet'].values[randrange(tamanhoDF)], style=TEXT_TWEET_POSITIVO),
                html.Br(),
            ])
        )
    else:
        return ''

# Controlelr fourth row
### Aqui irá ficar os tweets Negativos
@app.callback(
    dash.dependencies.Output(component_id = 'my-fourth-row', component_property='children'),
    [dash.dependencies.Input(component_id='candidato-dropdown', component_property= 'value')]
)
def update_output(value):
    if (value == '1'): #Marilia
        dfMariliaOriginalNegativo = dfMariliaOriginal.loc[dfMariliaOriginal['classificacao'] == 'Negativo', :]
        tamanhoDF = len(dfMariliaOriginalNegativo['tweet'])
        return (
            html.Div([
                html.H1('Tweets Negativos', style=TEXT_TITLE),
                html.Br(),
                html.Br(),
                html.Br(),
                html.H3(dfMariliaOriginalNegativo['tweet'].values[randrange(tamanhoDF)], style=TEXT_TWEET_NEGATIVO),
                html.Br(),
                html.H3(dfMariliaOriginalNegativo['tweet'].values[randrange(tamanhoDF)], style=TEXT_TWEET_NEGATIVO),
                html.Br(),
                html.H3(dfMariliaOriginalNegativo['tweet'].values[randrange(tamanhoDF)], style=TEXT_TWEET_NEGATIVO),
                html.Br(),
                html.H3(dfMariliaOriginalNegativo['tweet'].values[randrange(tamanhoDF)], style=TEXT_TWEET_NEGATIVO),
                html.Br(),
            ])
        )
    elif (value == '2'): #João
        dfJoaoOriginalNegativo = dfJoaoOriginal.loc[dfJoaoOriginal['classificacao'] == 'Negativo', :]
        tamanhoDF = len(dfJoaoOriginalNegativo['tweet'])
        return (
            html.Div([
                html.H1('Tweets Negativos', style=TEXT_TITLE),
                html.Br(),
                html.Br(),
                html.Br(),
                html.H3(dfJoaoOriginalNegativo['tweet'].values[randrange(tamanhoDF)], style=TEXT_TWEET_NEGATIVO),
                html.Br(),
                html.H3(dfJoaoOriginalNegativo['tweet'].values[randrange(tamanhoDF)], style=TEXT_TWEET_NEGATIVO),
                html.Br(),
                html.H3(dfJoaoOriginalNegativo['tweet'].values[randrange(tamanhoDF)], style=TEXT_TWEET_NEGATIVO),
                html.Br(),
                html.H3(dfJoaoOriginalNegativo['tweet'].values[randrange(tamanhoDF)], style=TEXT_TWEET_NEGATIVO),
                html.Br(),
            ])
        )
    elif (value == '3'): #Mendonça Filho
        dfMendoncaOriginalNegativo = dfMendoncaOriginal.loc[dfMendoncaOriginal['classificacao'] == 'Negativo', :]
        tamanhoDF = len(dfMendoncaOriginalNegativo['tweet'])
        return (
            html.Div([
                html.H1('Tweets Negativos', style=TEXT_TITLE),
                html.Br(),
                html.Br(),
                html.Br(),
                html.H3(dfMendoncaOriginalNegativo['tweet'].values[randrange(tamanhoDF)], style=TEXT_TWEET_NEGATIVO),
                html.Br(),
                html.H3(dfMendoncaOriginalNegativo['tweet'].values[randrange(tamanhoDF)], style=TEXT_TWEET_NEGATIVO),
                html.Br(),
                html.H3(dfMendoncaOriginalNegativo['tweet'].values[randrange(tamanhoDF)], style=TEXT_TWEET_NEGATIVO),
                html.Br(),
                html.H3(dfMendoncaOriginalNegativo['tweet'].values[randrange(tamanhoDF)], style=TEXT_TWEET_NEGATIVO),
                html.Br(),
            ])
        )
    elif (value == '4'): ### Delegada
        dfDelegadaOriginalNegativo = dfDelegada.loc[dfDelegadaOriginal['classificacao'] == 'Negativo', :]
        tamanhoDF = len(dfDelegadaOriginalNegativo['tweet'])
        return (
            html.Div([
                html.H1('Tweets Negativos', style=TEXT_TITLE),
                html.Br(),
                html.Br(),
                html.Br(),
                html.H3(dfDelegadaOriginalNegativo['tweet'].values[randrange(tamanhoDF)], style=TEXT_TWEET_NEGATIVO),
                html.Br(),
                html.H3(dfDelegadaOriginalNegativo['tweet'].values[randrange(tamanhoDF)], style=TEXT_TWEET_NEGATIVO),
                html.Br(),
                html.H3(dfDelegadaOriginalNegativo['tweet'].values[randrange(tamanhoDF)], style=TEXT_TWEET_NEGATIVO),
                html.Br(),
                html.H3(dfDelegadaOriginalNegativo['tweet'].values[randrange(tamanhoDF)], style=TEXT_TWEET_NEGATIVO),
                html.Br(),
            ])
        )
    else:
        return ''

# Main
if __name__ == '__main__':
    app.run_server(port='8085')