import json
from textwrap import dedent as d
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


class InteractiveVisualizationsModule(object):
    def __init__(self):
        self.id = 'interactive-visualizations'
        self.callback_check = 'Interactive Visualizations'

        styles = {
            'pre': {
                'border': 'thin lightgrey solid',
                'overflowX': 'scroll'
            }
        }

        self.layout = html.Div(id=self.id,
            children=[
                dcc.Graph(
                    id='basic-interactions',
                    figure={
                        'data': [
                            {
                                'x': [1, 2, 3, 4],
                                'y': [4, 1, 3, 5],
                                'text': ['a', 'b', 'c', 'd'],
                                'customdata': ['c.a', 'c.b', 'c.c', 'c.d'],
                                'name': 'Trace 1',
                                'mode': 'markers',
                                'marker': {'size': 12}
                            },
                            {
                                'x': [1, 2, 3, 4],
                                'y': [9, 4, 1, 4],
                                'text': ['w', 'x', 'y', 'z'],
                                'customdata': ['c.w', 'c.x', 'c.y', 'c.z'],
                                'name': 'Trace 2',
                                'mode': 'markers',
                                'marker': {'size': 12}
                            },
                        ]
                    }
                ),
                html.Div(className='row', children=[
                    html.Div([
                        dcc.Markdown(d("""
                            **Hover Data**
    
                            Mouse over values in the graph.
                        """)),
                        html.Pre(id='hover-data', style=styles['pre'])
                    ], className='three columns'),

                    html.Div([
                        dcc.Markdown(d("""
                            **Click Data**
    
                            Click points in the graph.
                        """)),
                        html.Pre(id='click-data', style=styles['pre'])
                    ], className='three columns'),

                    html.Div([
                        dcc.Markdown(d("""
                            **Selection Data**
    
                            Choose the lasso or rectangle tool in the graph's menu
                            bar and then select points in the graph.
                        """)),
                        html.Pre(id='selected-data', style=styles['pre'])
                    ], className='three columns'),

                    html.Div([
                        dcc.Markdown(d("""
                            **Zoom and Relayout Data**
    
                            Click and drag on the graph to zoom or click on the zoom
                            buttons in the graph's menu bar.
                            Clicking on legend items will also fire
                            this event.
                        """)),
                        html.Pre(id='relayout-data', style=styles['pre'])
                    ], className='three columns'),
                ])
            ], style={'display': 'none'}
        )

        return

    def set_callbacks(self, app):

        @app.callback(Output(self.id, 'style'), [Input('tabs', 'value'), Input('tab-subcategories', 'value')])
        def display_module(tab, tab_subcategory):
            if (tab == 4) & (tab_subcategory == self.callback_check):
                return {'display': 'block'}
            return {'display': 'none'}

        @app.callback(
            Output('hover-data', 'children'),
            [Input('basic-interactions', 'hoverData')]
        )
        def display_hover_data(hoverData):
            return json.dumps(hoverData, indent=2)

        @app.callback(
            Output('click-data', 'children'),
            [Input('basic-interactions', 'clickData')]
        )
        def display_click_data(clickData):
            return json.dumps(clickData, indent=2)

        @app.callback(
            Output('selected-data', 'children'),
            [Input('basic-interactions', 'selectedData')]
        )
        def display_click_data(selectedData):
            return json.dumps(selectedData, indent=2)

        @app.callback(
            Output('relayout-data', 'children'),
            [Input('basic-interactions', 'relayoutData')]
        )
        def display_click_data(relayoutData):
            return json.dumps(relayoutData, indent=2)

        return
