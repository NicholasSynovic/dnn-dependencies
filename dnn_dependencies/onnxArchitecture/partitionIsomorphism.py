from pprint import pprint as print
from typing import List

import networkx as nx
from networkx.algorithms import community, isomorphism

G: nx.DiGraph = nx.read_gexf("architecture.gexf")

# detects partition in graph G
# based on modularity: measures density of connections within communities
# in comparison to what the expected density is of a random network
partitions: List = list(community.greedy_modularity_communities(G))

# A list of frozensets of nodes, one for each community
# prints list of each set and nodes that are in each set, returns largest communities first
# print(partitions)

# # of partitions
print(len(partitions))

partitionNode: List = partitions[3]
print(partitionNode)

H: nx.DiGraph = nx.subgraph(G, partitionNode)


def isPartitionIsomorphic(G: nx.DiGraph, H: nx.DiGraph) -> bool:
    # initializes matcher to compare graphs G and H
    matcher: isomorphism.DiGraphMatcher = isomorphism.DiGraphMatcher(G, H)
    # prints boolean value for isomophism between G and H
    return matcher.subgraph_is_isomorphic()


print(isPartitionIsomorphic(G, H))
