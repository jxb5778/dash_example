import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input, State


class StateWithButtonModule(object):
    def __init__(self):
        self.id = 'state-with-button'
        self.callback_check = 'State with Button'

        self.layout = html.Div(id=self.id,
            children=[
                    dcc.Input(id='input-1-state', type='text', value='Montreal'),
                    dcc.Input(id='input-2-state', type='text', value='Canada'),
                    html.Button(id='submit-button', n_clicks=0, children='Submit'),
                    html.Div(id='output-state')
                ], style={'display': 'none'}
        )

        return

    def set_callbacks(self, app):

        @app.callback(Output(self.id, 'style'), [Input('tabs', 'value'), Input('tab-subcategories', 'value')])
        def display_module(tab, tab_subcategory):
            if (tab == 3) & (tab_subcategory == self.callback_check):
                return {'display': 'block'}
            return {'display': 'none'}

        @app.callback(
            Output('output-state', 'children'),
            [Input('submit-button', 'n_clicks')],
            [
                State('input-1-state', 'value'),
                State('input-2-state', 'value')
            ]
        )
        def update_output(n_clicks, input1, input2):
            return """
                The Button has been pressed {} times,
                Input 1 is "{}",
                and Input 2 is "{}"
            """.format(n_clicks, input1, input2)

        return
