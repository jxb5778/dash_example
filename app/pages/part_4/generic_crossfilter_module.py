import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import pandas as pd
from dash.dependencies import Input, Output


class GenericCrossfilterModule(object):
    def __init__(self):

        self.id ='generic-crossfilter-module'
        self.callback_check = 'Generic Crossfilter Recipe'

        self.layout = html.Div(id=self.id,
            children=[
                html.Div(
                    dcc.Graph(
                        id='g1',
                        config={'displayModeBar': False}
                    ), className='four columns'
                ),
                html.Div(
                    dcc.Graph(
                    id='g2',
                    config={'displayModeBar': False}
                    ), className='four columns'
                ),
                html.Div(
                    dcc.Graph(
                        id='g3',
                        config={'displayModeBar': False}
                    ), className='four columns'
                )
            ], className='row', style={'display': 'none'}
        )

    def set_callbacks(self, app):

        @app.callback(Output(self.id, 'style'), [Input('tabs', 'value'), Input('tab-subcategories', 'value')])
        def display_module(tab, tab_subcategory):
            if (tab == 4) & (tab_subcategory == self.callback_check):
                return {'display': 'block'}
            return {'display': 'none'}

        # app.callback is a decorator which means that it takes a function
        # as its argument.
        # highlight is a function "generator": it's a function that returns a function

        app.callback(
            Output('g1', 'figure'),
            [
                Input('g1', 'selectedData'),
                Input('g2', 'selectedData'),
                Input('g3', 'selectedData')
            ]
        )(highlight('Column 0', 'Column 1'))

        app.callback(
            Output('g2', 'figure'),
            [
                Input('g2', 'selectedData'),
                Input('g1', 'selectedData'),
                Input('g3', 'selectedData')
            ]
        )(highlight('Column 2', 'Column 3'))

        app.callback(
            Output('g3', 'figure'),
            [
                Input('g3', 'selectedData'),
                Input('g1', 'selectedData'),
                Input('g2', 'selectedData')
            ]
        )(highlight('Column 4', 'Column 5'))

        return


def highlight(x, y):
    np.random.seed(0)

    df = pd.DataFrame({
        'Column {}'.format(i): np.random.rand(30) + i * 10 for i in range(6)
    })

    def callback(*selectedDatas):
        selectedpoints = df.index
        for i, seleced_data in enumerate(selectedDatas):
            if seleced_data is not None:
                selected_index = [
                    p['customdata'] for p in seleced_data['points']
                ]
                if len(selected_index) > 0:
                    selectedpoints = np.intersect1d(
                        selectedpoints, selected_index
                    )
        figure = {
            'data':[
                {
                    'x': df[x],
                    'y': df[y],
                    'text': df.index,
                    'textposition': 'top',
                    'selectedpoints': selectedpoints,
                    'customdata': df.index,
                    'type': 'scatter',
                    'mode': 'markers+text',
                    'marker': {
                        'color': 'rgba(0, 116, 217, 0.7)',
                        'size': 12,
                        'line': {
                            'color': 'rgb(0, 116, 217)',
                            'width': 0.5
                        }
                    },
                    'textfont': {
                        'color': 'rgba(30, 30, 30, 1)'
                    },
                    'unselected': {
                        'marker': {
                            'opacity': 0.3
                        },
                        'textfont': {
                            # make color transparent when not selected
                            'color': 'rgba(0, 0, 0'
                        }
                    }
                }
            ],
            'layout': {
                'margin': {'l': 15, 'r': 0, 'b': 15, 't': 15},
                'dragmode': 'selected',
                'hovermode': 'closest',
                'showlegend': False
            }
        }

        shape = {
            'type': 'rect',
            'line': {
                'width': 1,
                'dash': 'dot',
                'color': 'darkgrey'
            }
        }

        if selectedDatas[0] and selectedDatas[0]['range']:
            figure['layout']['shapes'] = [dict({
                'x0': selectedDatas[0]['range']['x'][0],
                'x1': selectedDatas[0]['range']['x'][1],
                'y0': selectedDatas[0]['range']['y'][0],
                'y1': selectedDatas[0]['range']['y'][1]
            }, **shape)]
        else:
            figure['layout']['shapes'] = [dict({
                'type': 'rect',
                'x0': np.min(df[x]),
                'x1': np.max(df[x]),
                'y0': np.min(df[y]),
                'y1': np.max(df[y])
            }, **shape)]

        return figure

    return callback
