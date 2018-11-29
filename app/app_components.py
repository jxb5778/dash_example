from app.pages.part_1 import agr_module, dcc_example_module, first_graph_module, gdp_per_capita_module, markdown_module
from app.pages.part_2 import multiple_layer_outputs_module, multiple_outputs_simple_module, multiple_inputs_module, \
    simple_callback_module, slider_update_graph_module
from app.pages.part_3 import state_with_button_module
from app.pages.part_4 import generic_crossfilter_module, interactive_visualizations_module, update_graph_on_hover_module

# Part 1 componenets
agr = agr_module.AgrModule()
dcc_example = dcc_example_module.DccModule()
first_graph = first_graph_module.FirstGraphModule()
gdp_per_capita = gdp_per_capita_module.GdpPerCapitaModule()
markdown = markdown_module.MarkdownModule()

# Part 2 components
multiple_layer_outputs = multiple_layer_outputs_module.MultipleLayerOutputsModule()
multiple_outputs_simple = multiple_outputs_simple_module.MultipleOutputsSimple()
multiple_inputs = multiple_inputs_module.MultipleInputsModule()
simple_callback = simple_callback_module.SimpleCallbackModule()
slider_update_graph = slider_update_graph_module.SliderUpdateGraphModule()

# Part 3 components
state_with_button = state_with_button_module.StateWithButtonModule()

#Part 4 components
generic_crossfilter = generic_crossfilter_module.GenericCrossfilterModule()
interactive_visualizations = interactive_visualizations_module.InteractiveVisualizationsModule()
update_graph_on_hover = update_graph_on_hover_module.UpdateGraphOnHoverModule()

components = [
    agr, dcc_example, first_graph, gdp_per_capita, markdown, multiple_layer_outputs, multiple_outputs_simple,
    multiple_inputs, simple_callback, slider_update_graph, state_with_button, generic_crossfilter,
    interactive_visualizations, update_graph_on_hover
]