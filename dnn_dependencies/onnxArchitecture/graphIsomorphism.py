from pprint import pprint as print

import networkx as nx

graph1 = nx.DiGraph()
graph2 = nx.DiGraph()
graph3 = nx.DiGraph()

# nodes with multiple inputs and output at meta deta for each node
node_data1 = [
    {"id": "A", "input": ["1", "2"], "output": ["3"]},
    {"id": "B", "input": ["3"], "output": ["4"]},
    {"id": "C", "input": ["4", "5"], "output": ["6"]},
    {"id": "D", "input": ["4", "6"], "output": ["5"]},
]

# iterates through and adds each node to graph
for node in node_data1:
    node_id = node["id"]
    inputs = node["input"]
    outputs = node["output"]

    graph1.add_node(node_id, input=inputs, output=outputs)

# adds edges to the graph based on corresponding input and outputs
for u in graph1.nodes:
    u_data = graph1.nodes[u]

    for v in graph1.nodes:
        v_data = graph1.nodes[v]

        for output_attr in u_data["output"]:
            for input_attr in v_data["input"]:
                if output_attr == input_attr:
                    graph1.add_edge(u, v)


node_data2 = [
    {"id": "A", "input": ["1", "4"], "output": ["6"]},
    {"id": "B", "input": ["3"], "output": ["4"]},
    {"id": "C", "input": ["4", "6"], "output": ["6"]},
    {"id": "D", "input": ["4", "2"], "output": ["3"]},
]


for node in node_data2:
    node_id = node["id"]
    inputs = node["input"]
    outputs = node["output"]

    graph2.add_node(node_id, input=inputs, output=outputs)


for u in graph2.nodes:
    u_data = graph2.nodes[u]

    for v in graph2.nodes:
        v_data = graph2.nodes[v]

        for output_attr in u_data["output"]:
            for input_attr in v_data["input"]:
                if output_attr == input_attr:
                    graph2.add_edge(u, v)

print(nx.vf2pp_is_isomorphic(graph1, graph2, node_label=None))

node_data3 = [
    {"id": "A", "input": ["1", "4"], "output": ["6"]},
    {"id": "B", "input": ["3"], "output": ["4"]},
    {"id": "C", "input": ["4", "6"], "output": ["6"]},
    {"id": "D", "input": ["4", "2"], "output": ["3"]},
]


for node in node_data3:
    node_id = node["id"]
    inputs = node["input"]
    outputs = node["output"]

    graph3.add_node(node_id, input=inputs, output=outputs)


for u in graph3.nodes:
    u_data = graph3.nodes[u]

    for v in graph3.nodes:
        v_data = graph3.nodes[v]

        for output_attr in u_data["output"]:
            for input_attr in v_data["input"]:
                if output_attr == input_attr:
                    graph3.add_edge(u, v)

print(nx.vf2pp_is_isomorphic(graph2, graph3, node_label=None))


def isIsomorphic(graph1: nx.DiGraph, graph2: nx.DiGraph) -> bool:
    return nx.vf2pp_is_isomorphic(graph1, graph2, node_label=None)
