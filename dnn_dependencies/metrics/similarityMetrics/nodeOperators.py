import xml.etree.ElementTree as ET
from pprint import pprint as print
from typing import List

import matplotlib.pyplot as plt
import networkx as nx


# Specifies only the operator from node labels
def extractOpFromLabel(label) -> str:
    if "/" in label:
        # Extract operator from label
        label = label.rsplit("/", 1)[-1]
    if "_" in label:
        # Extract just operator, not its 'index'
        label = label.split("_", 1)[0]
    return label


# Gets operators from node labels and puts them in a list
def getNodeOperators(filePath) -> List:
    nodeLabels = {}
    tree = ET.parse(filePath)
    root = tree.getroot()

    # Namespace used in the GEXF file
    ns = {"gexf": "http://www.gexf.net/1.2draft"}

    # Find all nodes in the GEXF file
    nodes = root.findall(".//gexf:node", ns)

    # Extract the labels for each node
    operatorList: List[str] = []
    for node in nodes:
        # nodeID = node.get('id')
        label = node.get("label")
        label = extractOpFromLabel(label)
        operatorList.append(label)
        # nodeLabels[nodeID] = label

    return operatorList


# Path to GEXF file
gexfFilePath = "/Users/karolinaryzka/Documents/dnn-dependencies/dnn_dependencies/onnxArchitecture/gpt2.gexf"

# Get List of node operators
labels = getNodeOperators(gexfFilePath)


# Create Histogram of operate distribution
def plotNodeOperators(gexfFilePath) -> plt:
    plt.hist(getNodeOperators(gexfFilePath))
    plt.xlabel("Node Operators")
    plt.ylabel("# of Operator Iterations")
    plt.title("Distribution of Node Operators in Graph")
    plt.show()


# Make plot
plotNodeOperators(gexfFilePath)
