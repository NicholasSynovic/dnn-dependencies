from argparse import Namespace
from itertools import pairwise
from typing import List

from bs4 import BeautifulSoup, ResultSet, Tag
from networkx import DiGraph, write_gexf
from progress.bar import Bar
from treelib import Node, Tree
from treelib.exceptions import DuplicatedNodeIdError

from dnn_dependencies.args.exportLayersArgs import getArgs


def extractNodeLabels(dom: str) -> List[str]:
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
    graph: DiGraph = DiGraph()
    graph.add_edges_from(ebunch_to_add=edgeList)
    return graph


def buildTree(labels: List[str]) -> Tree:
    rootTag: str = "onnxComputationalGraph"
    rootID: str = "ocg"
    edges: List[List[str]] = []

    tree: Tree = Tree()
    tree.create_node(tag=rootTag, identifier=rootID)

    with Bar("Creating edge list... ", max=len(labels)) as bar:
        label: str
        for label in labels:
            edgeList: List[str] = [rootID]
            splitLabel: List[str] = label.split(sep="/")

            if len(splitLabel) > 1:
                foo: str = rootID + label
                edgeList = foo.split(sep="/")
            else:
                edgeList.append(splitLabel[0])

            edges.append(edgeList)
            bar.next()

    with Bar("Populating tree... ", max=len(edges)) as bar:
        idx: int
        edgeList: List[str]
        for edgeList in edges:
            parentID: str = rootID
            for idx in range(len(edgeList)):
                if idx == 0:
                    continue

                edge: str = edgeList[idx]
                edgeID: str = edge.lower()

                try:
                    baz: Node = tree.create_node(
                        tag=edge, identifier=edgeID, parent=parentID
                    )
                except DuplicatedNodeIdError:
                    pass

                parentID = edgeID
            bar.next()

    return tree


def main() -> None:
    args: Namespace = getArgs()

    with open(file=args.input[0], mode="r") as xmlDoc:
        xmlDOM: str = xmlDoc.read()
        xmlDoc.close()

    nodeLabels: List[str] = extractNodeLabels(dom=xmlDOM)
    edgeList: List[tuple[str, str]] = buildEdgeList(labels=nodeLabels)
    graph: DiGraph = buildDiGraph(edgeList=edgeList)
    write_gexf(graph, args.output[0])


if __name__ == "__main__":
    main()
