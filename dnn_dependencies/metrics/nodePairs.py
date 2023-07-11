from collections import defaultdict
from itertools import pairwise
from pprint import pprint as print
from typing import List

import matplotlib.pyplot as plt
import networkx as nx

# G: nx.DiGraph = nx.read_gexf(
#     "pt2.gexf"
# )


def nxToTuples(G: nx.DiGraph) -> list:
    """
    The function `nxToTuples` takes a directed graph `G` as input and returns a list of tuples, where
    each tuple contains a node from `G` and its corresponding children.

    :param G: The parameter G is a directed graph represented using the NetworkX library's DiGraph class
    :type G: nx.DiGraph
    :return: The function `nxToTuples` returns a list of tuples. Each tuple contains a node from the
    input graph `G` and a list of its children nodes.
    """
    nodePairs: List = []
    for node in G.nodes:
        children = list(G.successors(node))
        nodePairs.append((node, children))
    return nodePairs


def tuplesToPairDict(nodePairs: list):
    """
    The function `tuplesToPairDict` takes a list of node pairs and returns a dictionary that counts how
    many times each pair occurs, where each pair consists of a parent label and a child label.

    :param nodePairs: The parameter `nodePairs` is a list of tuples. Each tuple represents a pair of
    nodes, where the first element is the parent node ID and the second element is a list of children
    node IDs
    :type nodePairs: list
    :return: The function `tuplesToPairDict` returns a dictionary `data` that contains the count of how
    many times each pair occurs in the `nodePairs` list. The keys of the dictionary are tuples
    representing the parent-child pairs, and the values are the counts.
    """
    data = defaultdict(int)

    for pair in nodePairs:
        parentID = pair[0]
        childrenIDs = pair[1]

        # Get the parent label
        parentLabel = G.nodes[parentID]["label"]
        parentLabelExtracted = parentLabel.rsplit("/", 1)[-1].split("_", 1)[0]

        # Get the children labels
        childrenLabels = [G.nodes[childID]["label"] for childID in childrenIDs]
        childrenLabelsExtracted = [
            childLabel.rsplit("/", 1)[-1].split("_", 1)[0]
            for childLabel in childrenLabels
        ]

        # Count how many times each pair occurs
        for childLabel in childrenLabelsExtracted:
            data[(parentLabelExtracted, childLabel)] += 1

    return data


def plotDict(data: defaultdict) -> plt:
    """
    The function `plotDict` takes a dictionary as input and plots a horizontal bar chart to visualize
    the distribution of key-value pairs in the dictionary.

    :param data: The "data" parameter is a defaultdict object, which is a dictionary-like object that
    provides a default value for keys that do not exist in the dictionary. In this case, the keys are
    node-pairs and the values are the counts of those node-pairs
    :type data: defaultdict
    """
    pairs = list(data.keys())
    counts = list(data.values())
    plt.barh(
        range(len(pairs)),
        counts,
    )
    plt.yticks(range(len(pairs)), pairs)
    plt.ylabel("Node-Pairs")
    plt.xlabel("Count")
    plt.title("Distribution of Node-Pairs")
    plt.show()


# plotDict(tuplesToPairDict(nxToTuples(G)))
