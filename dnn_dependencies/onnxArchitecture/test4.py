import networkx 
import matplotlib.pyplot as plt

# Read the GEXF file into a NetworkX graph
graph = networkx.read_gexf('architecture.gexf')

# Create an empty NetworkX graph to store the transformed graph
newGraph = networkx.Graph()

for node_id, node_data in graph.nodes(data=True):
    input_attr = node_data.get('input')
    output_attr = node_data.get('output')
    newGraph.add_node(node_id, input=input_attr, output=output_attr)


for source_node_id, source_node_data in graph.nodes(data=True):
    source_output = source_node_data.get('output')
    for target_node_id, target_node_data in graph.nodes(data=True):
        target_input = target_node_data.get('input')
        if source_output == target_input:
            newGraph.add_edge(source_node_id, target_node_id)


networkx.draw(newGraph, with_labels=True, font_weight='bold')


plt.show()

