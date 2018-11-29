from dash. dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go


class MultipleInputsModule(object):
    def __init__(self):
        self.id = 'multiple-inputs'

        self.callback_check = 'Multiple Inputs'

        self.df = pd.read_csv(
            'https://gist.githubusercontent.com/chriddyp/'
            'cb5392c35661370d95f300086accea51/raw/'
            '8e0768211f6b747c0db42a9ce9a0937dafcbd8b2/'
            'indicators.csv')

        self.availabile_indicators = self.df['Indicator Name'].unique()

        self.layout = html.Div(id = self.id,
            children=[
                html.Div([
                    html.Div([
                        dcc.Dropdown(
                            id='xaxis-column',
                            options=[{'label': i, 'value': i} for i in self.availabile_indicators],
                            value='Fertility rate, total (births per woman)'
                        ),
                        dcc.RadioItems(
                            id='xaxis-type',
                            options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
                            value='Linear',
                            labelStyle={'display': 'inline-block'}
                        )
                    ],
                    style={'width': '48%', 'display': 'inline-block'}),

                    html.Div([
                        dcc.Dropdown(
                            id='yaxis-column',
                            options=[{'label': i, 'value': i} for i in self.availabile_indicators],
                            value='Fertility rate, total (births per woman)'
                        ),
                        dcc.RadioItems(
                            id='yaxis-type',
                            options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
                            value='Linear',
                            labelStyle={'display': 'inline-block'}
                        )
                    ], style={'width': '48%', 'display': 'inline-block'})
                ]),

                dcc.Graph(id='indicator-graphic'),

                dcc.Slider(
                    id='year--slider',
                    min=self.df['Year'].min(),
                    max=self.df['Year'].max(),
                    value=self.df['Year'].max(),
                    marks={str(year): str(year) for year in self.df['Year'].unique()}
                )
            ], style={'display': 'none'}
        )

    def set_callbacks(self, app):

        @app.callback(Output(self.id, 'style'), [Input('tabs', 'value'), Input('tab-subcategories', 'value')])
        def display_module(tab, tab_subcategory):
            if (tab == 2) & (tab_subcategory == self.callback_check):
                return {'display': 'block'}
            return {'display': 'none'}

        @app.callback(
            Output('indicator-graphic', 'figure'),
            [
                Input('xaxis-column', 'value'),
                Input('yaxis-column', 'value'),
                Input('xaxis-type', 'value'),
                Input('yaxis-type', 'value'),
                Input('year--slider', 'value')
            ]
        )
        def update_graph(xaxis_column_name, yaxis_column_name, xaxis_type, yaxis_type, year_value):
            dff = self.df[self.df['Year'] == year_value]

            return {
                'data': [go.Scatter(
                    x=dff[dff['Indicator Name'] == xaxis_column_name]['Value'],
                    y=dff[dff['Indicator Name'] == yaxis_column_name]['Value'],
                    text=dff[dff['Indicator Name'] == yaxis_column_name]['Country Name'],
                    mode='markers',
                    marker={
                        'size': 15,
                        'opacity': 0.5,
                        'line': {'width': 0.5, 'color': 'white'},
                    }
                )],
                'layout': go.Layout(
                    xaxis={
                        'title': xaxis_column_name,
                        'type': 'linear' if xaxis_type == 'Linear' else 'log'
                    },
                    yaxis={
                        'title': yaxis_column_name,
                        'type': 'linear' if yaxis_type == 'Linear' else 'log'
                    },
                    margin={'l': 40, 'b': 40, 't': 10, 'r': 0},
                    hovermode='closest'
                )
            }

        return
