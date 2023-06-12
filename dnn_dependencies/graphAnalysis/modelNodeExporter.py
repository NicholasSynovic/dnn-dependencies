import os
from argparse import Namespace
from pathlib import Path
from typing import List

from bs4 import BeautifulSoup, ResultSet, Tag
from progress.bar import Bar
from treelib import Node, Tree

from dnn_dependencies.args.modelTreeExporterArgs import getArgs


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
                foo: Node = tree.create_node(tag=edge, parent=parentID)
                parentID = foo.identifier
            bar.next()

    return tree


def main() -> None:
    args: Namespace = getArgs()

    with open(file=args.input[0], mode="r") as xmlDoc:
        xmlDOM: str = xmlDoc.read()
        xmlDoc.close()

    nodeLabels: List[str] = extractNodeLabels(dom=xmlDOM)

    tree: Tree = buildTree(labels=nodeLabels)
    tree.to_graphviz(filename=args.output[0])


if __name__ == "__main__":
    main()
