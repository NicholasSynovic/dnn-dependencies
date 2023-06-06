from pprint import pprint as print
from typing import List

import networkx as nx
from networkx.algorithms import isomorphism

G: nx.DiGraph = nx.read_gexf("architecture.gexf")


# detects communities in graph H
communities: List[dict] = nx.algorithms.community.louvain_communities(G, seed=None)


communityNode: dict = communities[3]

H: nx.DiGraph = nx.subgraph(G, communityNode)


# #prints communities in graph G
# for i, community in enumerate(communitiesH):
#     print(f"Community {i+1}: {community}")


# prints boolean value for isomophism between G and H
# print(matcher.subgraph_is_isomorphic())
def isCommunitiesIsomorphic(G: nx.DiGraph, H: nx.DiGraph) -> bool:
    # initializes matcher to compare graphs G and H
    matcher: isomorphism.DiGraphMatcher = isomorphism.DiGraphMatcher(G, H)
    return matcher.subgraph_is_isomorphic()
