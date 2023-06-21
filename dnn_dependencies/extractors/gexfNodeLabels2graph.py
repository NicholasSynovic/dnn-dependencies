from argparse import Namespace
from itertools import pairwise
from typing import List

from bs4 import BeautifulSoup, ResultSet, Tag
from networkx import DiGraph, write_gexf
from progress.bar import Bar

from dnn_dependencies.args.gexfNodeLabels2graph_args import getArgs


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
