from pprint import pprint as print
from typing import List

import matplotlib.pyplot as plt
import networkx as nx

G: nx.DiGraph = nx.read_gexf(
    "/Users/karolinaryzka/Documents/dnn-dependencies/dnn_dependencies/onnxArchitecture/gpt2.gexf"
)


def outDegreeDistribution(G: nx.DiGraph) -> plt:
    degreeList: List[int] = []
    for node in G.nodes():
        outDegree = G.out_degree(node)
        degreeList.append(outDegree)
    degreeList.sort(reverse=True)
    plt.hist(degreeList)
    plt.xlabel("Degree")
    plt.ylabel("# of Nodes")
    plt.title("Distribution of out-degrees of nodes in graph")
    plt.show()


outDegreeDistribution(G)
