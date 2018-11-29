from dash.dependencies import Output, Input
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go


class UpdateGraphOnHoverModule(object):
    def __init__(self):

        self.df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/'
            'cb5392c35661370d95f300086accea51/raw/'
            '8e0768211f6b747c0db42a9ce9a0937dafcbd8b2/'
            'indicators.csv')

        self.available_indicators = self.df['Indicator Name'].unique()

        self.id = 'update-graph-on-hover'
        self.callback_check = 'Update Graph on Hover'

        self.layout = html.Div(id=self.id,
            children= [
                html.Div([
                    html.Div([
                        dcc.Dropdown(
                            id='crossfilter-xaxis-column',
                            options=[{'label': i, 'value': i} for i in self.available_indicators],
                            value='Fertility rate, total (births per woman)'
                        ),
                        dcc.RadioItems(
                            id='crossfilter-xaxis-type',
                            options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
                            value='Linear',
                            labelStyle={'display': 'inline-block'}
                        )
                        ],
                        style={'width': '49%', 'display': 'inline-block'}),


                    html.Div([
                        dcc.Dropdown(
                            id='crossfilter-yaxis-column',
                            options=[{'label': i, 'value': i} for i in self.available_indicators],
                            value='Life expectancy at birth, total (years)'
                        ),
                        dcc.RadioItems(
                            id='crossfilter-yaxis-type',
                            options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
                            value='Linear',
                            labelStyle={'display': 'inline-block'}
                        )
                    ], style={'width': '49%', 'float': 'right', 'display': 'inline-block'})
                ], style={
                    'borderBottom': 'thin lightgrey solid',
                    'backgroundColor': 'rgb(250, 250, 250)',
                    'padding': '10px 5px'
                }),

                html.Div([
                    dcc.Graph(
                        id='crossfilter-indicator-scatter',
                        hoverData={'points': [{'customdata': 'Japan'}]}
                    )
                ], style={'width': '49%', 'display': 'inline-block', 'padding': '0 20'}),

                html.Div([
                    dcc.Graph(id='x-time-series'),
                    dcc.Graph(id='y-time-series'),
                ], style={'display': 'inline-block', 'width': '49%'}),

                html.Div(dcc.Slider(
                    id='crossfilter-year--slider',
                    min=self.df['Year'].min(),
                    max=self.df['Year'].max(),
                    value=self.df['Year'].max(),
                    marks={str(year): str(year) for year in self.df['Year'].unique()}
                ), style={'width': '49%', 'padding': '0px 20px 20px 20px'})
            ],style={'display': 'none'}
        )

    def set_callbacks(self, app):
        @app.callback(Output(self.id, 'style'), [Input('tabs', 'value'), Input('tab-subcategories', 'value')])
        def display_module(tab, tab_subcategory):
            if (tab == 4) & (tab_subcategory == self.callback_check):
                return {'display': 'block'}
            return {'display': 'none'}

        @app.callback(
            Output('crossfilter-indicator-scatter', 'figure'),
            [
                Input('crossfilter-xaxis-column', 'value'),
                Input('crossfilter-yaxis-column', 'value'),
                Input('crossfilter-xaxis-type', 'value'),
                Input('crossfilter-yaxis-type', 'value'),
                Input('crossfilter-year--slider', 'value')
            ]
        )
        def update_graph(xaxis_column_name, yaxis_column_name, xaxis_type, yaxis_type, year_value):
            dff = self.df[self.df['Year'] == year_value]

            return {
                'data': [go.Scatter(
                    x=dff[dff['Indicator Name'] == xaxis_column_name]['Value'],
                    y=dff[dff['Indicator Name'] == yaxis_column_name]['Value'],
                    text=dff[dff['Indicator Name'] == yaxis_column_name]['Country Name'],
                    customdata=dff[dff['Indicator Name'] == yaxis_column_name]['Country Name'],
                    mode='markers',
                    marker={
                        'size': 15,
                        'opacity': 0.5,
                        'line': {'width': 0.5, 'color': 'white'}
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
                    margin={'l': 40, 'b': 30, 't': 10, 'r': 0},
                    height=450,
                    hovermode='closest'
                )
            }

        @app.callback(
            Output('x-time-series', 'figure'),
            [
                Input('crossfilter-indicator-scatter', 'hoverData'),
                Input('crossfilter-xaxis-column', 'value'),
                Input('crossfilter-xaxis-type', 'value')
            ]
        )
        def update_y_timeseries(hoverData, xaxis_column_name, axis_type):
            country_name = hoverData['points'][0]['customdata']
            dff = self.df[self.df['Country Name'] == country_name]
            dff = dff[dff['Indicator Name'] == xaxis_column_name]
            title = '<b>{}</b><br>{}'.format(country_name, xaxis_column_name)

            return create_time_series(dff, axis_type, title)

        @app.callback(
            Output('y-time-series', 'figure'),
            [
                Input('crossfilter-indicator-scatter', 'hoverData'),
                Input('crossfilter-yaxis-column', 'value'),
                Input('crossfilter-yaxis-type', 'value')
            ]
        )
        def update_x_timeseries(hoverData, yaxis_column_name, axis_type):
            country_name = hoverData['points'][0]['customdata']
            dff = self.df[self.df['Country Name'] == country_name]
            dff = dff[dff['Indicator Name'] == yaxis_column_name]
            title = '<b>{}</b><br>{}'.format(country_name, yaxis_column_name)

            return create_time_series(dff, axis_type, title)

        return


def create_time_series(dff, axis_type, title):
    return {
        'data': [go.Scatter(
            x=dff['Year'],
            y=dff['Value'],
            mode='lines+markers'
        )],
        'layout': {
            'height': 225,
            'margin': {'l': 20, 'b': 30, 'r': 10, 't': 10},
            'annotations': [{
                'x': 0, 'y': 0.85, 'xanchor': 'left', 'yanchor': 'bottom',
                'xref': 'paper', 'yref': 'paper', 'showarrow': False,
                'align': 'left', 'bgcolor': 'rgba(255, 255, 255, 0.5)',
                'text': title
            }],
            'yaxis': {'type': 'linear' if axis_type == 'Linear' else 'log'},
            'xaxis': {'showgrid': False}
        }
    }

