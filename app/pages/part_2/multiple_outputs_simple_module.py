import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


class MultipleOutputsSimple(object):
    def __init__(self):

        self.id = 'multiple-outputs-simple'

        self.layout = html.Div(id=self.id,
            children = [
                dcc.RadioItems(
                    id='dropdown-a',
                    options=[{'label': i, 'value': i} for i in ['Canada', 'USA', 'Mexico']],
                    value='Canada'
                ),
                html.Div(id='output-a'),

                dcc.RadioItems(
                    id='dropdown-b',
                    options=[{'label': i, 'value': i} for i in ['MTL', 'NYC', 'SF']],
                    value='Canada'
                ),

                html.Div(id='output-b')
            ], style={'display': 'none'}
        )

    def set_callbacks(self, app):

        @app.callback(Output(self.id, 'style'), [Input('tabs', 'value'), Input('tab-subcategories', 'value')])
        def display_module(tab, tab_subcategory):
            if (tab == 2) & (tab_subcategory == 'Multiple Outputs Simple'):
                return {'display': 'block'}
            return {'display': 'none'}

        @app.callback(Output('output-a', 'children'), [Input('dropdown-a', 'value')])
        def callback_a(dropdown_value):
            return 'You\'ve selected "{}"'.format(dropdown_value)

        @app.callback(Output('output-b', 'children'), [Input('dropdown-b', 'value')])
        def callback_b(dropdown_value):
            return 'You\'ve selected "{}"'.format(dropdown_value)

        return
