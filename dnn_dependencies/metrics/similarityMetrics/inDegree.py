from pprint import pprint as print
from typing import List

import matplotlib.pyplot as plt
import networkx as nx

G: nx.DiGraph = nx.read_gexf(
    "/Users/karolinaryzka/Documents/dnn-dependencies/dnn_dependencies/onnxArchitecture/gpt2.gexf"
)


def inDegreeDistribution(G: nx.DiGraph) -> plt:
    degreeList: List[int] = []
    for node in G.nodes():
        inDegree = G.in_degree(node)
        degreeList.append(inDegree)
    degreeList.sort(reverse=True)
    plt.hist(degreeList)
    plt.xlabel("Degree")
    plt.ylabel("# of Nodes")
    plt.title("Distribution of in-degrees of nodes in graph")
    plt.show()


inDegreeDistribution(G)
