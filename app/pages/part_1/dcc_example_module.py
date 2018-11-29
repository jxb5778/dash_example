import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


class DccModule(object):
    def __init__(self):
        self.layout = html.Div(id='dcc-example',
            children=[
                html.Label('Dropdown'),
                dcc.Dropdown(
                    options=[
                        {'label': 'New York City', 'value': 'NYC'},
                        {'label': 'Montreal', 'value': 'MTL'},
                        {'label': 'San Fransisco', 'value': 'SF'}
                    ],
                    value='MTL'
                ),

                html.Label('Multi-Select Dropdown'),
                dcc.Dropdown(
                    options=[
                        {'label': 'New York City', 'value': 'NYC'},
                        {'label': 'Montreal', 'value': 'MTL'},
                        {'label': 'San Fransisco', 'value': 'SF'}
                    ],
                    value=['MTL', 'SF'],
                    multi=True
                ),

                html.Label('Radio Items'),
                dcc.RadioItems(
                    options=[
                        {'label': 'New York City', 'value': 'NYC'},
                        {'label': 'Montreal', 'value': 'MTL'},
                        {'label': 'San Fransisco', 'value': 'SF'}
                    ],
                    value='MTL'
                ),

                html.Label('Checkboxes'),
                dcc.Checklist(
                    options=[
                        {'label': 'New York City', 'value': 'NYC'},
                        {'label': 'Montreal', 'value': 'MTL'},
                        {'label': 'San Fransisco', 'value': 'SF'}
                    ],
                    values=['MTL', 'SF']
                ),

                html.Label('Text Input'),
                dcc.Input(value='MTL', type='text'),

                html.Label('Slider'),
                dcc.Slider(
                    min=0,
                    max=9,
                    marks={i: 'Label {}'.format(i) if i == 1 else str(i) for i in range(1, 6)},
                    value=5
                )
            ], style={'columnCount': 2, 'display': 'none'})
        return

    def set_callbacks(self, app):

        @app.callback(Output('dcc-example', 'style'), [Input('tabs', 'value'), Input('tab-subcategories', 'value')])
        def display_module(tab, tab_subcategory):
            if (tab == 1) & (tab_subcategory == 'DCC Examples'):
                return {'columnCount': 2, 'display': 'block'}
            return {'columnCount': 2, 'display': 'none'}

        return