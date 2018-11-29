from app import app
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input
from app.app_components import components


header = html.Div([
    dcc.Tabs(
        id='tabs',
        value=1,
        children=[dcc.Tab(label= 'Part {}'.format(i), value=i) for i in range(1,5)],
    ),
    html.Div(id='subcategories',
        children=[
            dcc.Dropdown(id='tab-subcategories'),
            html.Hr()
        ]
    )
])

app.layout = html.Div([
    header,
    html.Div([component.layout for component in components])
    ], style={
        'width': '80%',
        'fontFamily': 'Sans-Serif',
        'margin-left': 'auto',
        'margin-right': 'auto'
    })

tab_subcategories = {
    '1': ['Agriculture Exports', 'DCC Examples', 'First Graph', 'GDP Per Capita', 'Markdown'],
    '2': [
            'Multiple Layer Outputs', 'Multiple Outputs Simple', 'Multiple Inputs', 'Simple Callback',
            'Slider Update Graph'
        ],
    '3': ['State with Button'],
    '4': ['Generic Crossfilter Recipe', 'Interactive Visualizations', 'Update Graph on Hover']
}


@app.callback(Output('tab-subcategories', 'options'), [Input('tabs', 'value')])
def set_tab_subcategories(tab):
    return [{'label': i, 'value': i} for i in tab_subcategories[str(tab)]]


@app.callback(Output('tab-subcategories', 'value'), [Input('tab-subcategories', 'options')])
def set_tab_subcategory_value(available_options):
    return available_options[0]['value']


for component in components:
    component.set_callbacks(app)
