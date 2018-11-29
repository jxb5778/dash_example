from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html


class MultipleLayerOutputsModule(object):
    def __init__(self):

        self.id = 'multi-layer-outputs'

        self.all_options = {
            'America': ['New York City', 'San Fransisco', 'Cincinnati'],
            'Canada': ['Montreal', 'Toronto', 'Ottawa']
        }

        self.layout = html.Div(id=self.id,
            children = [
                dcc.Dropdown(
                    id='countries-dropdown',
                    options=[{'label': k, 'value': k} for k in self.all_options.keys()],
                    value='America'
                ),
                html.Hr(),

                dcc.RadioItems(id='cities-dropdown'),

                html.Hr(),

                html.Div(id='display-selected-values')
            ], style={'display': 'none'}
        )

    def set_callbacks(self, app):

        @app.callback(Output(self.id, 'style'), [Input('tabs', 'value'), Input('tab-subcategories', 'value')])
        def display_module(tab, tab_subcategory):
            if (tab == 2) & (tab_subcategory == 'Multiple Layer Outputs'):
                return {'display': 'block'}
            return {'display': 'none'}

        @app.callback(Output('cities-dropdown', 'options'), [Input('countries-dropdown', 'value')])
        def set_cities_options(selected_country):
            return [{'label': i, 'value': i} for i in self.all_options[selected_country]]

        @app.callback(Output('cities-dropdown', 'value'), [Input('cities-dropdown', 'options')])
        def set_cities_value(available_options):
            return available_options[0]['value']

        @app.callback(
            Output('display-selected-values', 'children'),
            [Input('countries-dropdown', 'value'), Input('cities-dropdown', 'value')]
        )
        def set_display_children(selected_country, selected_city):
            return '{} is a city in {}'.format(selected_city, selected_country)

        return
