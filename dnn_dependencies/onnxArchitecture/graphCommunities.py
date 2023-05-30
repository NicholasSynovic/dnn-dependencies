import networkx as nx
from pprint import pprint as print

G = nx.read_gexf('EuroSiS Generale Pays.gexf')

communities = nx.algorithms.community.greedy_modularity_communities(G)

for i, community in enumerate(communities):
    print(f"Community {i+1}: {community}")





