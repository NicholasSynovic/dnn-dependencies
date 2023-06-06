import networkx as nx
from pprint import pprint as print
from networkx.algorithms import approximation
import numpy as np
import matplotlib.pyplot as plt
from typing import List




# Comparison of degree distributions
G: nx.DiGraph = nx.read_gexf('architecture.gexf')

fig: plt.figure = plt.figure("Degree of graph", figsize=(5, 4))
axgrid = fig.add_gridspec(5, 4)

#graph of in degrees
degree_sequence = sorted((d for n, d in G.in_degree()), reverse=True)
dmax = max(degree_sequence)

ax2 = fig.add_subplot(axgrid[3:, :2])
ax2.bar(*np.unique(degree_sequence, return_counts=True))
ax2.set_title("In Degree histogram")
ax2.set_xlabel("Degree")
ax2.set_ylabel("# of Nodes")

#graph of out degree
degree_sequence2 = sorted((d for n, d in G.out_degree()), reverse=True)
dmax2 = max(degree_sequence2)

ax2 = fig.add_subplot(axgrid[3:, 2:])
ax2.bar(*np.unique(degree_sequence2, return_counts=True))
ax2.set_title("Out Degree histogram")
ax2.set_xlabel("Degree")
ax2.set_ylabel("# of Nodes")

#show graphs
fig.tight_layout()
plt.show()




#in/out degree for specified nodes
def inDegree(G: nx.DiGraph, nodeID: str) -> str:
    return('in degree for node ' + nodeID + ' :' + str(G.in_degree(nodeID)))
print(inDegree(G, '97'))

def outDegree(G: nx.DiGraph, nodeID: str) -> str:
    return('out degree for node ' + nodeID + ' :' + str(G.out_degree(nodeID)))
print(outDegree(G, '99'))




#density
def density(G: nx.DiGraph) -> str:
    return('density of graph: ' + str(nx.density(G)))
print(density(G))




#cluster coefficient for specified node
def clusterCoeffficient(G: nx.DiGraph, nodeID: str) -> str:
    return('cluster coefficient of node ' + nodeID + ' :' + str(nx.clustering(G, '3')))
print(clusterCoeffficient(G, '3'))




#different dataset used for avg shortest path length and graph edit distance

characters = ["R2-D2",
                "CHEWBACCA",
                "C-3PO",
                "LUKE",
                "DARTH VADER",
                "CAMIE",
                "BIGGS",
                "LEIA",
                "BERU",
                "OWEN",
                "OBI-WAN",
                "MOTTI",
                "TARKIN",
                "HAN",
                "DODONNA",
                "GOLD LEADER",
                "WEDGE",
                "RED LEADER",
                "RED TEN"]

edges = [("CHEWBACCA", "R2-D2"),
        ("C-3PO", "R2-D2"),
        ("BERU", "R2-D2"),
        ("LUKE", "R2-D2"),
        ("OWEN", "R2-D2"),
        ("OBI-WAN", "R2-D2"),
        ("LEIA", "R2-D2"),
        ("BIGGS", "R2-D2"),
        ("HAN", "R2-D2"),
        ("CHEWBACCA", "OBI-WAN"),
        ("C-3PO", "CHEWBACCA"),
        ("CHEWBACCA", "LUKE"),
        ("CHEWBACCA", "HAN"),
        ("CHEWBACCA", "LEIA"),
        ("CAMIE", "LUKE"),
        ("BIGGS", "CAMIE"),
        ("BIGGS", "LUKE"),
        ("DARTH VADER", "LEIA"),
        ("BERU", "LUKE"),
        ("BERU", "OWEN"),
        ("BERU", "C-3PO"),
        ("LUKE", "OWEN"),
        ("C-3PO", "LUKE"),
        ("C-3PO", "OWEN"),
        ("C-3PO", "LEIA"),
        ("LEIA", "LUKE"),
        ("BERU", "LEIA"),
        ("LUKE", "OBI-WAN"),
        ("C-3PO", "OBI-WAN"),
        ("LEIA", "OBI-WAN"),
        ("MOTTI", "TARKIN"),
        ("DARTH VADER", "MOTTI"),
        ("DARTH VADER", "TARKIN"),
        ("HAN", "OBI-WAN"),
        ("HAN", "LUKE"),
        ("C-3PO", "HAN"),
        ("LEIA", "MOTTI"),
        ("LEIA", "TARKIN"),
        ("HAN", "LEIA"),
        ("DARTH VADER", "OBI-WAN"),
        ("DODONNA", "GOLD LEADER"),
        ("DODONNA", "WEDGE"),
        ("DODONNA", "LUKE"),
        ("GOLD LEADER", "WEDGE"),
        ("GOLD LEADER", "LUKE"),
        ("LUKE", "WEDGE"),
        ("BIGGS", "LEIA"),
        ("LEIA", "RED LEADER"),
        ("LUKE", "RED LEADER"),
        ("BIGGS", "RED LEADER"),
        ("BIGGS", "C-3PO"),
        ("C-3PO", "RED LEADER"),
        ("RED LEADER", "WEDGE"),
        ("GOLD LEADER", "RED LEADER"),
        ("BIGGS", "WEDGE"),
        ("RED LEADER", "RED TEN"),
        ("BIGGS", "GOLD LEADER"),
        ("LUKE", "RED TEN")]

#creating the graph
H = nx.Graph()
H.add_nodes_from(characters)
H.add_edges_from(edges)




#average shortest path length --> if graph isn't strongly connected error will show
#different data set used to show its function
def averageShortestPathLength(H: nx.DiGraph) -> float:  
    return(nx.algorithms.average_shortest_path_length(H))
print(averageShortestPathLength(H))




#Graph edit distance ---> runs very long on original dataset, found no end yet
#so different dataset is used
nodes: List = ["OBI-WAN", "HAN", "LEIA"]
H1: nx.DiGraph = H.subgraph(nodes)
def graphEditDistance(H: nx.DiGraph, H1: nx.DiGraph) -> float:
    return(nx.graph_edit_distance(H, H1))
print(graphEditDistance(H1, H))


print("hello world")
