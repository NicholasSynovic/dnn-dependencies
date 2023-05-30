import networkx
from networkx import Graph

graph1: Graph = networkx.read_gexf("architecture.gexf")
graph2: Graph = networkx.read_gexf("reuse.gexf")

print(graph1.number_of_nodes(), graph1.number_of_edges())


# print(networkx.algorithms.is_isomorphic(G1=graph1, G2=graph2))
