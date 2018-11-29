import pandas as pd
from dash.dependencies import Input, Output
from app.app_helper_lib import *


class AgrModule(object):
    def __init__(self):
        df = pd.read_csv(
            'https://gist.githubusercontent.com/chriddyp/'
            'c78bf172206ce24f77d6363a2d754b59/raw/'
            'c353e8ef842413cae56ae3920b8fd78468aa4cb2/'
            'usa-agricultural-exports-2011.csv'
        )
        self.layout = html.Div(id='arg-module',
            children=[
                html.H4(children='US Agriculture Exports (2011)'),
                generate_table(df)
            ], style={'display': 'none'}
        )
        return

    def set_callbacks(self, app):

        @app.callback(Output('arg-module', 'style'), [Input('tabs', 'value'), Input('tab-subcategories', 'value')])
        def display_module(tab, tab_subcategory):
            if (tab == 1) & (tab_subcategory == 'Agriculture Exports'):
                return {'display': 'block'}
            return {'display': 'none'}

        return
