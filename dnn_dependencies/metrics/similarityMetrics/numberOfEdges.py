from pprint import pprint as print
from typing import List

import networkx as nx

G: nx.DiGraph = nx.read_gexf(
    "/Users/karolinaryzka/Documents/dnn-dependencies/dnn_dependencies/onnxArchitecture/gpt2.gexf"
)


# Get total number of edges in graph
def totalEdges(G: nx.DiGraph) -> str:
    return "Number of edges in graph: " + str(G.size())


print(totalEdges(G))
