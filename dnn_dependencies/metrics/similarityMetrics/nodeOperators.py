from pprint import pprint as print
from typing import List

import matplotlib.pyplot as plt
import networkx as nx

G: nx.DiGraph = nx.read_gexf(
    "/Users/karolinaryzka/Documents/dnn-dependencies/dnn_dependencies/onnxArchitecture/gpt2.gexf"
)

import xml.etree.ElementTree as ET


def get_node_labels_from_gexf(file_path):
    node_labels = {}
    tree = ET.parse(file_path)
    root = tree.getroot()

    # Namespace used in the GEXF file
    ns = {"gexf": "http://www.gexf.net/1.2draft"}

    # Find all nodes in the GEXF file
    nodes = root.findall(".//gexf:node", ns)

    # Extract the labels for each node
    for node in nodes:
        node_id = node.get("id")
        label_element = node.find('.//gexf:attvalue[@for="label"]', ns)
        if label_element is not None:
            label = label_element.get("value")
            node_labels[node_id] = label

    return node_labels


# Provide the path to your GEXF file
gexf_file_path = "/Users/karolinaryzka/Documents/dnn-dependencies/dnn_dependencies/onnxArchitecture/gpt2.gexf"

# Call the function to extract node labels
labels = get_node_labels_from_gexf(gexf_file_path)

# Print the node labels
for node_id, label in labels.items():
    print(f"Node ID: {node_id}, Label: {label}")


# def getNodeOperators(G: nx.DiGraph) -> List:
