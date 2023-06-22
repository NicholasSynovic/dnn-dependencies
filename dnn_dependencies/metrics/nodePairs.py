from collections import defaultdict
from itertools import pairwise
from pprint import pprint as print
from typing import List

import matplotlib.pyplot as plt
import networkx as nx

G: nx.DiGraph = nx.read_gexf(
    "/Users/karolinaryzka/Documents/dnn-dependencies/dnn_dependencies/onnxArchitecture/gpt2.gexf"
)


# NX list of tuples with every node and its children
def nxToTuples(G: nx.DiGraph) -> list:
    nodePairs: List = []
    for node in G.nodes:
        children = list(G.successors(node))
        nodePairs.append((node, children))
    return nodePairs


# Takes list of nodes and their children and puts it into a default dict first pairing node to child and then converting into
# its node operator labels. Puts into a default dict and counts how many times each pair occurs
def tuplesToPairDict(nodePairs: list):
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


# Plot data
def plotDict(data: defaultdict) -> plt:
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


plotDict(tuplesToPairDict(nxToTuples(G)))
