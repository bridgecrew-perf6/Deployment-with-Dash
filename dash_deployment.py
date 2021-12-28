from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
import plotly.express as px
import dash
import pandas as pd
import plotly.graph_objs as go


def drawFigure():
    return  html.Div([
        dbc.Card(
            dbc.CardBody([
                dcc.Graph(
                    figure=px.bar(
                        df, x="sepal_width", y="sepal_length", color="species"
                    ).update_layout(
                        template='plotly_dark',
                        plot_bgcolor= 'rgba(0, 0, 0, 0)',
                        paper_bgcolor= 'rgba(0, 0, 0, 0)',
                    ),
                    config={
                        'displayModeBar': False
                    }
                )
            ])
        ),
    ])

# Text field
def drawText(text):
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                html.Div([
                    html.P(text),
                ], style={'text-align': 'center'})
            ])
        ),
    ])

def drawTextHead(text):
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                html.Div([
                    html.H6(text),
                ], style={'textAlign': 'center'})
            ])
        ),
    ])
def generate_table(dataframe, max_rows=15):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])

# Data
game = pd.read_csv('new_data')
L = len(game)
game_count = game['Name'].value_counts()

#most seen 15 genres
genres = game['Genres'].value_counts().head(15)
genres.keys()


display_cols = ['Name', 'Developers', 'Year', 'Genres','Revenue']
top_15 = game.sort_values(by='Revenue', ascending=False).head(15)

top = top_15[display_cols]


# Build App
app = dash.Dash(external_stylesheets=[dbc.themes.CYBORG])

app.layout = html.Div([
    html.Div(children=[
    html.H1('FULL - STEAM',style={'text-align': 'center'}),
    html.H2('More Games',style={'text-align': 'center'}),
        dbc.Card(
            dbc.CardBody([
                dbc.Row([
                    dbc.Col([
                        drawText('STEAM BY MORE NUMBERS AND GRAPHS')
                    ], width=12)])])),

    html.P('''Steam is a video game digital distribution service by Valve.
              It was launched as a standalone software client in September 2003.
              Valve to provide automatic updates for client games.'''),


        dbc.Card(
            dbc.CardBody([
                dbc.Row([
                    dbc.Col([
                        drawText('STEAM HAD APPROXIMATELY 120 MILLION MONTHLY ACTIVE PLAYERS IN 2020')
                    ], width=4),
                    dbc.Col([
                        drawText('MORE ACTION, ADVENTURE GAMES IN 2020')
                    ], width=4),
                    dbc.Col([
                        drawText('STEAM HAD APPROXIMATELY 120 MILLION MONTHLY ACTIVE PLAYERS IN 2020.')
                    ], width=4)
                ])])),

    dbc.Card(
        dbc.CardBody([
            dbc.Row([
                dbc.Col([
                    drawTextHead('AGE - FEE RELATION')
                ], width=3),
                dbc.Col([
                    drawTextHead('ANNUAL RELEASED GAME')
                ], width=3),
                dbc.Col([
                    drawTextHead('MOST SEEN GENRES')
                ], width=6),
            ], align='center'),
            html.Br(),
            dbc.Row([
                dbc.Col([
                    html.Div([
                        dbc.Card(
                            dbc.CardBody([
                                dcc.Graph(
                                    figure=px.bar(
                                        game, x="Is Free", y="Required Age", color="Required Age"

                                    ).update_layout(
                                        template='plotly_dark',
                                        plot_bgcolor='rgba(0, 0, 0, 0)',
                                        paper_bgcolor='rgba(0, 0, 0, 0)',
                                    ),
                                    config={
                                        'displayModeBar': False
                                    }
                                )
                            ])
                        ),
                    ])
                ], width=3),
                dbc.Col([
                    html.Div([
                        dbc.Card(
                            dbc.CardBody([

                                dcc.Graph(
                                    figure=px.bar(
                                        game, x="Year", y=game_count
                                    ).update_layout(
                                        template='plotly_dark',
                                        plot_bgcolor='rgba(0, 0, 0, 0)',
                                        paper_bgcolor='rgba(0, 0, 0, 0)',
                                    ),
                                    config={
                                        'displayModeBar': False
                                    }
                                )
                            ])
                        ),
                    ])
                ], width=3),
                dbc.Col([
                    html.Div([
                        dbc.Card(
                            dbc.CardBody([
                                dcc.Graph(
                                    figure=px.pie(
                                        game, values=genres, names=genres.keys()
                                    ).update_layout(
                                        template='plotly_dark',
                                        plot_bgcolor='rgba(0, 0, 0, 0)',
                                        paper_bgcolor='rgba(0, 0, 0, 0)',
                                    ),
                                    config={
                                        'displayModeBar': False
                                    }
                                )
                            ])
                        ),
                    ])
                ], width=6),
            ], align='center'),

            html.Br(),
        dbc.Row([
            dbc.Col([
                drawTextHead('YEAR - DEVELOPERS TOP 15 DISTRIBUTION')
                ], width=6),
            dbc.Col([
                drawTextHead('YEAR - MONTH REVENUE DISTRIBUTION')
                ], width=6),
        ], align='center'),
            html.Br(),
            dbc.Row([
                dbc.Col([
                    html.Div([
                        dbc.Card(
                            dbc.CardBody([
                                dcc.Graph(
                                    figure=go.Figure(
                                        data=[go.Heatmap(
                                            x=top['Developers'],
                                            y=top['Year'],
                                            z=top['Revenue'], colorscale='geyser')]
                                    ).update_layout(
                                        xaxis_title="Developers",
                                        yaxis_title="Year",
                                        legend_title="Revenue",
                                        template='plotly_dark',
                                        plot_bgcolor='rgba(0, 0, 0, 0)',
                                        paper_bgcolor='rgba(0, 0, 0, 0)',
                                    ),
                                )
                            ])
                        ),
                    ])
                ], width=6),
                dbc.Col([
                    html.Div([
                        dbc.Card(
                            dbc.CardBody([
                                dcc.Graph(
                                    figure = go.Figure(
                                        data = [go.Heatmap(
                                            x= game['Year'],
                                            y= game['Month'],
                                            z =game['Revenue'],colorscale='geyser')]
                                    ).update_layout(
                                        xaxis_title="Year",
                                        yaxis_title="Month",
                                        legend_title="Revenue",
                                        template='plotly_dark',
                                        plot_bgcolor='rgba(0, 0, 0, 0)',
                                        paper_bgcolor='rgba(0, 0, 0, 0)',
                                    ),
                                )
                            ])
                        ),
                    ])
                ], width=6),
            ], align='center'),
            html.Br(),
            dbc.Row([
                dbc.Col([
                  drawTextHead('YEAR - GENRES TOP 15 DISTRIBUTION')
                ], width=12),
            ], align='center'),
            html.Br(),
            dbc.Row([
                dbc.Col([
                    html.Div([
                        dbc.Card(
                            dbc.CardBody([
                                dcc.Graph(
                                    figure=px.scatter(
                                        top,
                                        x="Year",
                                        y="Genres",
                                        size="Revenue",
                                        color="Revenue",
                                        log_x=True,
                                        size_max=60

                                    ).update_layout(
                                        template='plotly_dark',
                                        plot_bgcolor='rgba(0, 0, 0, 0)',
                                        paper_bgcolor='rgba(0, 0, 0, 0)',
                                    ),
                                    config={
                                        'displayModeBar': False
                                    }
                                )
                            ])
                        ),
                    ])
                ], width=12),
            ], align='center'),
            html.Br(),
            dbc.Row([
                dbc.Col([
                    drawTextHead('TOP 15')
                ], width=12),
            ], align='center'),
            html.Br(),
            dbc.Row([
                dbc.Col([
                    html.Div([
                        dbc.Card(
                            dbc.CardBody([
                                generate_table(top, 15)
                            ])
                        ),
                    ])
                ], width=12),
            ], align='center'),
        ]), color = 'dark'
    )
])
])

# Run app and display result inline in the notebook
if __name__ == '__main__':
    app.run_server(debug=True)