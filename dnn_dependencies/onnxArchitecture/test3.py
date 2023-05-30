import networkx as nx 
from pprint import pprint as print
import matplotlib.pyplot as plt



graph = nx.DiGraph()

# nodes with multiple inputs and output at meta deta for each node
node_data = [
    {'id': 'A', 'input': ['1', '2'], 'output': ['3']},
    {'id': 'B', 'input': ['3'], 'output': ['4']},
    {'id': 'C', 'input': ['4', '5'], 'output': ['6']},
    {'id': 'D', 'input': ['4', '6'], 'output': ['5']}
]

#iterates through and adds each node to graph
for node in node_data:
    node_id = node['id']
    inputs = node['input']
    outputs = node['output']
    
    graph.add_node(node_id, input=inputs, output=outputs)

# adds edges to the graph based on corresponding input and outputs
for u in graph.nodes:
    u_data = graph.nodes[u]
    
    for v in graph.nodes:
        v_data = graph.nodes[v]
        
        for output_attr in u_data['output']:
            for input_attr in v_data['input']:
                if output_attr == input_attr:
                    graph.add_edge(u, v)

# Print the graph
print("Nodes:")
print(graph.nodes)
print("\nEdges:")
print(graph.edges)

# Draw the graph
nx.draw(graph, with_labels=True, font_weight='bold')
plt.show()

