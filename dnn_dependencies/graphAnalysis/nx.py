import networkx
from networkx import Graph

graph: Graph = networkx.read_gexf("architecture.gexf")

print(graph.nodes["0"])
