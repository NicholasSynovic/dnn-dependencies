from argparse import Namespace
from itertools import pairwise
from typing import List

from bs4 import BeautifulSoup, ResultSet, Tag
from networkx import DiGraph
from networkx.drawing.nx_pydot import write_dot
from progress.bar import Bar

from dnn_dependencies.args.gexfNodeLabels2graph_args import getArgs


def extractNodeLabels(dom: str) -> List[str]:
    """
    The function `extractNodeLabels` takes a string representation of an XML document and returns a list
    of labels extracted from the `<node>` tags in the document.

    :param dom: The `dom` parameter is a string that represents the HTML or XML document. It is the
    input from which we want to extract node labels
    :type dom: str
    :param dom: str:
    :param dom: str:
    :returns: a list of strings, which are the labels of the nodes extracted from the given DOM.

    """
    data: List[str] = []

    soup: BeautifulSoup = BeautifulSoup(markup=dom, features="lxml")
    nodeTags: ResultSet = soup.findAll(name="node")

    with Bar("Extacting node labels... ", max=len(nodeTags)) as bar:
        tag: Tag
        for tag in nodeTags:
            data.append(str(tag.get(key="label")))
            bar.next()

    return data


def buildEdgeList(labels: List[str]) -> List[tuple[str, str]]:
    """
    The function `buildEdgeList` takes a list of labels and creates an edge list by splitting the labels
    and pairing the nodes together.

    :param labels: The `labels` parameter is a list of strings. Each string represents a label or a path
    to a node in a computational graph
    :type labels: List[str]
    :param labels: List[str]:
    :param labels: List[str]:
    :returns: The function `buildEdgeList` returns a list of tuples, where each tuple represents an edge
    in a graph. Each tuple contains two strings, representing the source and target nodes of the edge.

    """
    data: List[tuple[str, str]] = []

    rootTag: str = "onnxComputationalGraph"

    with Bar("Creating edge list... ", max=len(labels)) as bar:
        label: str
        for label in labels:
            nodeList: List[str] = [rootTag]
            splitLabel: List[str] = label.split(sep="/")

            if len(splitLabel) > 1:
                foo: str = rootTag + label
                nodeList = foo.split(sep="/")
            else:
                nodeList.append(splitLabel[0])

            edgeList: List[tuple[str, str]] = list(pairwise(nodeList))
            data.extend(edgeList)

            bar.next()
    return data


def buildDiGraph(edgeList: List[tuple[str, str]]) -> DiGraph:
    """
    The function `buildDiGraph` takes a list of tuples representing edges and returns a directed graph.

    :param edgeList: The `edgeList` parameter is a list of tuples representing the edges of a directed
    graph. Each tuple contains two elements: the source node and the target node of the edge
    :type edgeList: List: List: List[tuple[str, str]]
    :param edgeList: List[tuple[str:
    :param str: returns: a directed graph (DiGraph) object.
    :param edgeList: List[tuple[str:
    :param str]]:
    :returns: a directed graph (DiGraph) object.

    """
    graph: DiGraph = DiGraph()
    graph.add_edges_from(ebunch_to_add=edgeList)
    return graph


def main() -> None:
    """
    The main function reads an XML file, extracts node labels, builds an edge list, constructs a
    directed graph, and writes the graph to a GEXF file.


    """
    args: Namespace = getArgs()

    with open(file=args.input[0], mode="r") as xmlDoc:
        xmlDOM: str = xmlDoc.read()
        xmlDoc.close()

    nodeLabels: List[str] = extractNodeLabels(dom=xmlDOM)
    edgeList: List[tuple[str, str]] = buildEdgeList(labels=nodeLabels)
    graph: DiGraph = buildDiGraph(edgeList=edgeList)
    write_dot(graph, args.output[0])


if __name__ == "__main__":
    main()
