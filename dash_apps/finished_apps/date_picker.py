from datetime import date
from django_plotly_dash import DjangoDash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
import re
import datetime as dt
from dashboard import funs

today = dt.datetime.now().date()

app = DjangoDash('date_picker')  

app.layout = html.Div([
    dcc.DatePickerSingle(
        id='my-date-picker-single',
        display_format='DD.MM.YYYY',
        min_date_allowed=date(2021, 1, 8),
        max_date_allowed=today,
        initial_visible_month=today,
        date=today, 
        style={
            'margin-left':'8px',
            'margin-bottom':'8px',
            'margin-right':'8px',
        }
    ), 
    html.Div(id='output_div')], style={'height':'400px'})


@app.callback(
    Output('output_div', 'children'),
    Input('my-date-picker-single', 'date'))
def update_output(date_value):
    if date_value is not None:
            date_string = date_value
            print(date_string)
            data = funs.sleep_data_detailed(dt.datetime.strptime(date_string, '%Y-%m-%d').strftime('%Y-%m-%d %H:%M:%S'))
            fig = []
            for pair in data:
                fig.append(html.Div(
                    [html.Div(pair['name'], style={
      'height': '80px',
      'width': '188.8px',
      'float': 'left',
      'box-sizing': 'border-box',
      'font-family': ['Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans'],
      'color': 'white',
      'margin': 'auto',
      'font-size': '30px',
      'text-align': 'center',
      'vertical-align': 'middle',
      'line-height': '80px',    
      'background-color': 'rgba(82,82,82,0.4)',
}), 
html.Div(pair['value'], style={
      'height': '80px',
      'width': '188.8px',
      'float': 'left',
      'box-sizing': 'border-box',
      'font-family': ['Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans'],
      'color': 'white',
      'margin': 'auto',
      'font-size': '30px',
      'text-align': 'center',
      'vertical-align': 'middle',
      'line-height': '80px',    
      'background-color': 'rgba(0,0,21, 0.6)',
})], id="measurements", style={
      'height': '160px',
      'width': '188.8px',
      'float': 'left',
      'box-sizing': 'border-box',
      'font-family': ['Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans'],
      'color': 'white',
      'margin': 'auto',
      'font-size': '30px',    
      'background-color': 'transparent'

}))


            fig = html.Div(fig, style={'margin': '0', 'height':'400px'})
            return fig