from pprint import pprint as print
from typing import List

import matplotlib.pyplot as plt
import networkx as nx

G: nx.DiGraph = nx.read_gexf(
    "/Users/karolinaryzka/Documents/dnn-dependencies/dnn_dependencies/onnxArchitecture/gpt2.gexf"
)


def clusteringCoefficient(G: nx.DiGraph) -> plt:
    coefficientList: List[int] = []
    for node in G.nodes():
        clusteringCoefficient = nx.clustering(G, node)
        coefficientList.append(clusteringCoefficient)
    coefficientList.sort(reverse=True)
    plt.hist(coefficientList)
    plt.xlabel("Clustering Coefficient")
    plt.ylabel("# of Nodes")
    plt.title("Distribution of clustering coefficients of nodes in graph")
    plt.show()


clusteringCoefficient(G)
