from pprint import pprint as print
from typing import List

import networkx as nx

G: nx.DiGraph = nx.read_gexf(
    "/Users/karolinaryzka/Documents/dnn-dependencies/dnn_dependencies/onnxArchitecture/gpt2.gexf"
)


# Get total number nodes in graph
def totalNodes(G: nx.DiGraph) -> str:
    return "Number of nodes in graph: " + str(G.number_of_nodes())


print(totalNodes(G))
