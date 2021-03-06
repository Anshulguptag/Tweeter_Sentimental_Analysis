import dash
from dash.dependencies import Output, Event
import dash_core_components as dcc
import dash_html_components as html
import plotly
import random
import numpy as np
import plotly.graph_objs as go
from collections import deque

X = deque(maxlen=20)
X.append(1)
Y = deque(maxlen=20)
Y.append(1)


app = dash.Dash(__name__)
app.layout = html.Div(
    [
        dcc.Graph(id='live-graph', animate=True),
        dcc.Interval(
            id='graph-update',
            interval=1*10000
        ),
    ]
)

@app.callback(Output('live-graph', 'figure'),
              events=[Event('graph-update', 'interval')])
def update_graph_scatter():
    pulldata = open("C:\\Users\\anshul\\jupyter\\sample.txt", "r").read()
    lines = pulldata.split('\n')
    xar = []
    yar = []
    '''
    par = []
    nar = []
    near = []
    p = 0
    n = 0
    ne = 0
    '''
    x1 = 0
    y = 0
    for l in lines:
        x1 += 1
        if 'Positive' in l:
            y += 1
        elif 'Negative' in l:
            y -= 1
            # else:
            #  ne += 0

    X.append(x1)
    Y.append(y/x1)

    data = plotly.graph_objs.Scatter(
            x=list(X),
            y=list(Y),
            name='Scatter',
            mode= 'lines+markers'
            )

    return {'data': [data],'layout' : go.Layout(xaxis=dict(range=[min(X),max(X)]),
                                                yaxis=dict(range=[min(Y),max(Y)]),)}



if __name__ == '__main__':
    app.run_server(debug=True)