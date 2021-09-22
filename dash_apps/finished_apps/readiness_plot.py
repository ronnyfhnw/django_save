from dash import dcc
import dash
from dash import html
from dash.dependencies import Input, Output
from django_plotly_dash import DjangoDash
import plotly.graph_objects as go
from dashboard.models import sleep, activity, readiness
import datetime as dt
import pandas as pd
from django.db import connection

app = DjangoDash('readiness_plot')

df = pd.read_sql_query("SELECT * FROM dashboard_readiness", connection)
#df = df.sort_values(by='timestamp', ascending=False)
df = df.reset_index(drop=True)

slider = dcc.RangeSlider(
        id='my-range-slider',
        min=0,
        max=df.shape[0] - 1,
        step=1,
        value=[0, df.shape[0] - 1])

app.layout = html.Div([dcc.Graph(id="plot"), slider])

@app.callback(
    Output('plot', 'figure'),
    [Input('my-range-slider', 'value')])
def update_output(value):
      fig = go.Figure()
      fig.add_scattergl(x=df.timestamp.iloc[value[0]:(value[1]-1)], y=df.readiness_score.iloc[value[0]:(value[1]-1)], line={'color': 'green'})
      fig.update_layout({
            'plot_bgcolor': 'rgba(0, 0, 0, 0)',
            'paper_bgcolor': 'rgba(0,0,21, 0.8)',
      })

      # deactivating grid
      fig.update_xaxes(showgrid=False, color='white')
      fig.update_yaxes(showgrid=True, gridcolor='rgba(255,255,255,0.6)', color='white')

      # setting y range
      fig.update_yaxes(range=[0,100])
      fig.update_layout(showlegend=False, width=960, height=400, margin=dict(l=40, r=40, t=40, b=10))
      return fig