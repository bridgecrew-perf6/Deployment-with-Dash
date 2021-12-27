import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go

app = dash.Dash(__name__)

# additional color dictionary
colors = {
    'background': '#111111',
    'text': '#7FDBFF'}

#Read csv file
game = pd.read_csv('new_data')

gamenew = game[['name', 'required_age','developers', 'publishers', 'total_positive',
                'total_negative', 'total_reviews', 'currency', 'final_formatted',
                'genre', 'year']]

gamenew.rename(columns={'name': 'Game Name',
                        'required_age': 'Required Age',
                        'developers': 'Game Developers',
                        'publishers': 'Game Publishers',
                        'total_positive': 'Positive Reviews',
                        'total_negative': 'Negative Reviews',
                        'currency': 'Currency',
                        'final_formatted': 'Price',
                        'genre': 'Genres',
                        'year': 'Released Year'})

############## OS SYSTEM ##################
fig = make_subplots(rows=1, cols=3, subplot_titles=('linux', 'mac', 'windows'))
length = len(game)

cnames = ['linux', 'mac', 'windows']
for k, name in enumerate(cnames):
    columns = game[name].sum()
    fig.add_trace(go.Bar(x=['True', 'False'], y=[columns, length-columns], name=name), 1,k+1)

fig.update_layout(title_text='Most Used OS Systems', title_x=0.5,barmode='relative',  bargap=0.05, width=700, height=400)

############# MOST SEEN GENRES #########
genres = game.genre.value_counts()
most_seen_genres = genres[genres.values > 90]

# draw a pie chart for genres
figGenres = px.pie(game, values=most_seen_genres, names= most_seen_genres.keys(), title='Most Seen Genres')
fig.show()
fig.show()

######## MOST SEEN DEVELOPERS ###########
most_seen_developers = game.developers.value_counts().head(10)
figDev = px.pie(game, values=most_seen_developers, names= most_seen_developers.keys(), title='Most Seen Developers')
fig.show()

def generate_table(dataframe, max_rows=10):
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


app.layout = html.Div(children=[
    html.H1(children='Steam Game Deployment'),

    html.Div(children='''
        Game data
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    ),
    dcc.Graph(
        id='Genres',
        figure=figGenres
    ), dcc.Graph(
        id='Developers',
        figure=figDev
    ),
    html.H4(children='Steam Games Data'),
    generate_table(gamenew)
])

if __name__ == '__main__':
    app.run_server(debug=True)