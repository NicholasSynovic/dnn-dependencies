import networkx as nx
from pprint import pprint as print
from networkx.algorithms import isomorphism
from typing import List

G: nx.DiGraph = nx.read_gexf('architecture.gexf')

nodes: List = [1, 5, 7]

H: nx.DiGraph = G.subgraph(nodes)

# #prints communities in graph G
# for i, community in enumerate(communitiesH):
#     print(f"Community {i+1}: {community}")



def isSubgraphisomorphic(G: nx.DiGraph, H: nx.DiGraph) -> bool:
    #initializes matcher to compare graphs G and H
    matcher = isomorphism.DiGraphMatcher(G, H)
    #prints boolean value for isomophism between G and H
    return matcher.subgraph_is_isomorphic()
