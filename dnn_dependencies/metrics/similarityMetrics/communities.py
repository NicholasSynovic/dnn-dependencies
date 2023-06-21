from pprint import pprint as print
from typing import List

import matplotlib.pyplot as plt
import networkx as nx

G: nx.DiGraph = nx.read_gexf(
    "/Users/karolinaryzka/Documents/dnn-dependencies/dnn_dependencies/onnxArchitecture/gpt2.gexf"
)


# Get number of communities in graph
def numberOfCommunities(G: nx.DiGraph) -> str:
    communities: List = []
    communities = nx.community.louvain_communities(G)
    totalCommunities = len(communities)
    print("Number of communities in graph: " + str(totalCommunities))


numberOfCommunities(G)
