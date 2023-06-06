from pprint import pprint as print

import networkx as nx
from networkx.algorithms import isomorphism

# G = nx.barabasi_albert_graph(4, 2)
# H = nx.barabasi_albert_graph(4,2)

G = nx.read_gexf("architecture.gexf")

communities = nx.algorithms.community.louvain_communities(G, seed=None)
communityNode = communities[3]

H = nx.subgraph(G, communityNode)

graphMatcher = isomorphism.DiGraphMatcher(G, H)
result = graphMatcher.subgraph_is_isomorphic()

if result:
    G_nodes = list(G.nodes())
    H_nodes = list(H.nodes())
    mapping = graphMatcher.mapping
    print("The graphs are isomorphic with the following mappings:")
    for node in G_nodes:
        print(f"G node {'node'} is mapped to H node {mapping['node']}")
else:
    print("The graphs are not isomorphic.")

# if result:
#     mappings = graphMatcher.mapping
#     print("They are isimorphic with these mappings: ")
#     for mapping in mappings:
#         print(mapping)
# else:
#     print("not isomorphic")

# mappings= graphMatcher.mapping
# print("they are isomorphic with these mappings: ")
# for mapping in mappings:
#     print(mapping)
