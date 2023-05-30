import networkx as nx 
from pprint import pprint as print
import matplotlib.pyplot as plt


# characters = ["R2-D2",
#                 "CHEWBACCA",
#                 "C-3PO",
#                 "LUKE",
#                 "DARTH VADER",
#                 "CAMIE",
#                 "BIGGS",
#                 "LEIA",
#                 "BERU",
#                 "OWEN",
#                 "OBI-WAN",
#                 "MOTTI",
#                 "TARKIN",
#                 "HAN",
#                 "DODONNA",
#                 "GOLD LEADER",
#                 "WEDGE",
#                 "RED LEADER",
#                 "RED TEN"]


# edges = [("CHEWBACCA", "R2-D2"),
#         ("C-3PO", "R2-D2"),
#         ("BERU", "R2-D2"),
#         ("LUKE", "R2-D2"),
#         ("OWEN", "R2-D2"),
#         ("OBI-WAN", "R2-D2"),
#         ("LEIA", "R2-D2"),
#         ("BIGGS", "R2-D2"),
#         ("HAN", "R2-D2"),
#         ("CHEWBACCA", "OBI-WAN"),
#         ("C-3PO", "CHEWBACCA"),
#         ("CHEWBACCA", "LUKE"),
#         ("CHEWBACCA", "HAN"),
#         ("CHEWBACCA", "LEIA"),
#         ("CAMIE", "LUKE"),
#         ("BIGGS", "CAMIE"),
#         ("BIGGS", "LUKE"),
#         ("DARTH VADER", "LEIA"),
#         ("BERU", "LUKE"),
#         ("BERU", "OWEN"),
#         ("BERU", "C-3PO"),
#         ("LUKE", "OWEN"),
#         ("C-3PO", "LUKE"),
#         ("C-3PO", "OWEN"),
#         ("C-3PO", "LEIA"),
#         ("LEIA", "LUKE"),
#         ("BERU", "LEIA"),
#         ("LUKE", "OBI-WAN"),
#         ("C-3PO", "OBI-WAN"),
#         ("LEIA", "OBI-WAN"),
#         ("MOTTI", "TARKIN"),
#         ("DARTH VADER", "MOTTI"),
#         ("DARTH VADER", "TARKIN"),
#         ("HAN", "OBI-WAN"),
#         ("HAN", "LUKE"),
#         ("C-3PO", "HAN"),
#         ("LEIA", "MOTTI"),
#         ("LEIA", "TARKIN"),
#         ("HAN", "LEIA"),
#         ("DARTH VADER", "OBI-WAN"),
#         ("DODONNA", "GOLD LEADER"),
#         ("DODONNA", "WEDGE"),
#         ("DODONNA", "LUKE"),
#         ("GOLD LEADER", "WEDGE"),
#         ("GOLD LEADER", "LUKE"),
#         ("LUKE", "WEDGE"),
#         ("BIGGS", "LEIA"),
#         ("LEIA", "RED LEADER"),
#         ("LUKE", "RED LEADER"),
#         ("BIGGS", "RED LEADER"),
#         ("BIGGS", "C-3PO"),
#         ("C-3PO", "RED LEADER"),
#         ("RED LEADER", "WEDGE"),
#         ("GOLD LEADER", "RED LEADER"),
#         ("BIGGS", "WEDGE"),
#         ("RED LEADER", "RED TEN"),
#         ("BIGGS", "GOLD LEADER"),
#         ("LUKE", "RED TEN")]

# G = nx.Graph()

# #creating the graph
# G.add_nodes_from(characters)
# G.add_edges_from(edges)

# #list of nodes
# print(list(G.nodes))
# print('')
# #list of edges
# print(list(G.edges))
# print('')
# #lists nodes adjacent to specified node
# print(list(G.adj["LUKE"]))
# #prints how many edges a certain node has
# print(G.degree["LUKE"])

# #remove specific node
# G.remove_node("OBI-WAN")
# print('removing OBI-WAN')
# print(G.degree["LUKE"])

# #remove specific edge
# G.remove_edge("R2-D2", "LUKE")
# print('removing edge between R2D2 and Luke')
# print(G.degree["LUKE"])

# #specifying attributes to a specific node
# G.add_node("Karolina", attribute='me')
# print(G.nodes["Karolina"])

# #adding an attribute to a preexisting node
# G.nodes["Karolina"]['attribute2'] = "hi"

# #printing/accessing just the attributes of a node
# print(G.nodes["Karolina"])

# #writing / reading graphs into in a file
# #nx.write_gml(red, "path.to.file")
# #mygraph = nx.read_gml("path.to.file")

# #create directed graph
# DG = nx.DiGraph()
# #adding edges between nodes w/ weights while creating all three elements
# DG.add_weighted_edges_from([(1, 2, 0.5), (3, 1, 0.75)])
# #weight of edges pointing out of specified node
# print(DG.out_degree(1, weight='weight'))
# #sum of edge weights
# print(DG.degree(1, weight='weight'))
# #directed edges from 1
# print(list(DG.successors(1)))
# #same as above
# print(list(DG.neighbors(1)))


# G = nx.petersen_graph()
# subax1 = plt.subplot(121)
# nx.draw(G, with_labels=True, font_weight='bold')
# subax2 = plt.subplot(122)
# nx.draw_shell(G, nlist=[range(5, 10), range(5)], with_labels=True, font_weight='bold')
# plt.show()

mygraph = nx.read_gexf("architecture.gexf")


