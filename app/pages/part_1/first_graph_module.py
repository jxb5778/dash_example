import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


class FirstGraphModule(object):
    def __init__(self):
        colors = {
            'background': '#111111',
            'text': '#7FDBFF'
        }

        self.layout = html.Div(id='first-graph',
            children=[
                html.H1(
                    children='Hello Dash',
                    style={
                        'textAlign': 'center',
                        'color': colors['text']
                    }
                ),
                html.Div(
                    children='Dash: A web application framework for Python.',
                    style={
                        'textAlign': 'center',
                        'color': colors['text']
                    }
                ),
                dcc.Graph(
                    id='example-graph',
                    figure={
                        'data': [
                            {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                            {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montreal'}
                        ],
                        'layout': {
                            'plot_bgcolor': colors['background'],
                            'paper_bgcolor': colors['background'],
                            'font': {
                                'color': colors['text']
                            }
                        }
                    }
                ),
            ], style={'display': 'none'}
        )

    def set_callbacks(self, app):

        @app.callback(Output('first-graph', 'style'), [Input('tabs', 'value'), Input('tab-subcategories', 'value')])
        def display_module(tab, tab_subcategory):
            if (tab == 1) & (tab_subcategory == 'First Graph'):
                return {'display': 'block'}
            return {'display': 'none'}

        return
