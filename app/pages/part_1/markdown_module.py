import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from textwrap import dedent


class MarkdownModule(object):
    def __init__(self):
        markdown_text = dedent("""
                ### Dash and Markdown

                Dash apps can be written in Markdown.
                Dash uses the [CommonMark](http://commonmark.org)
                specification of MarkDown.
                Check out their [60 Second Markdown Tutorial](http://commonmark.org/help/)
                if this is your first introduction to MarkDown!

                """)
        self.layout = html.Div(id='markdown',
            children=[
                dcc.Markdown(children=markdown_text)
            ], style={'display': 'none'}
        )
        return

    def set_callbacks(self, app):

        @app.callback(Output('markdown', 'style'), [Input('tabs', 'value'), Input('tab-subcategories', 'value')])
        def display_module(tab, tab_subcategory):
            if (tab == 1) & (tab_subcategory == 'Markdown'):
                return {'display': 'block'}
            return {'display': 'none'}

        pass
