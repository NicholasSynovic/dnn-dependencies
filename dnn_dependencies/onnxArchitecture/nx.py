import networkx
from matplotlib import pyplot
from networkx import Graph, draw_networkx

graph: Graph = networkx.read_gexf("architecture.gexf")
draw_networkx(G=graph)
pyplot.savefig("test.svg")
