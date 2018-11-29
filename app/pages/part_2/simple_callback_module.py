import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


class SimpleCallbackModule(object):
    def __init__(self):
        self.id = 'simple-callback'

        self.callback_check = 'Simple Callback'

        self.layout = html.Div(id=self.id,
            children=[
                dcc.Input(id='my-id', value='initial value', type='text'),
                html.Div(id='my-div')
            ], style={'display': 'none'}
        )

    def set_callbacks(self, app):

        @app.callback(Output(self.id, 'style'), [Input('tabs', 'value'), Input('tab-subcategories', 'value')])
        def display_module(tab, tab_subcategory):
            if (tab == 2) & (tab_subcategory == self.callback_check):
                return {'display': 'block'}
            return {'display': 'none'}

        @app.callback(
            Output(component_id='my-div', component_property='children'),
            [Input(component_id='my-id', component_property='value')]
        )
        def update_output_div(input_value):
            return 'You\'ve entered "{}"'.format(input_value)

        return
