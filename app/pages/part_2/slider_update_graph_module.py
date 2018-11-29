from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go


class SliderUpdateGraphModule(object):
    def __init__(self):
        self.id = 'slider-update-graph'
        self.callback_check = 'Slider Update Graph'

        self.df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')

        self.layout = html.Div(id=self.id,
            children=[
                dcc.Graph(id='graph-with-slider'),
                dcc.Slider(
                    id='year-slider',
                    min=self.df['year'].min(),
                    max=self.df['year'].max(),
                    value=self.df['year'].min(),
                    marks={str(year): str(year) for year in self.df['year'].unique()}
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
            Output('graph-with-slider', 'figure'),
            [Input('year-slider', 'value')])
        def update_figure(selected_year):
            filtered_df = self.df[self.df.year == selected_year]
            traces = []
            for i in filtered_df.continent.unique():
                df_by_continent = filtered_df[filtered_df['continent'] == i]
                traces.append(go.Scatter(
                    x=df_by_continent['gdpPercap'],
                    y=df_by_continent['lifeExp'],
                    text=df_by_continent['country'],
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=i
                ))

            return {
                'data': traces,
                'layout': go.Layout(
                    xaxis={'type': 'log', 'title': 'GDP Per Capita'},
                    yaxis={'title': 'Life Expectancy', 'range': [20, 90]},
                    margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                    legend={'x': 0, 'y': 1},
                    hovermode='closest'
                )
            }

        return
