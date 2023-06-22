from argparse import Namespace
from collections import defaultdict
from itertools import product
from json import dump
from pprint import pprint as print
from typing import Any, Generator, List, Set

from networkx import DiGraph, clustering, density, read_gexf
from networkx.algorithms.community import louvain_communities
from networkx.classes.reportviews import NodeView
from progress.bar import Bar

from dnn_dependencies.args.similarity_args import getArgs


def _sortDict(d: defaultdict | dict[Any, Any]) -> dict[Any, Any]:
    foo: dict[Any, Any] = dict(d)
    bar: dict[Any, Any] = dict(sorted(foo.items()))

    return bar


def computeDensity(graph: DiGraph) -> float:
    return density(G=graph)


def countNodes(graph: DiGraph) -> int:
    return graph.number_of_nodes()


def countEdges(graph: DiGraph) -> int:
    return graph.size()


def countCommunities(graph: DiGraph) -> int:
    communities: List[Set[str]] = louvain_communities(graph, seed=42)
    return len(communities)


def computeDegreeDistribution(graph: DiGraph, inDegree: bool = True) -> dict[int, int]:
    data: defaultdict = defaultdict(int)

    def _iterateInDegree(nodes: NodeView, bar: Bar) -> None:
        node: str
        for node in nodes:
            degree: int = graph.in_degree(node)
            data[degree] += 1
            bar.next()

    def _iterateOutDegree(nodes: NodeView, bar: Bar) -> None:
        node: str
        for node in nodes:
            degree: int = graph.out_degree(node)
            data[degree] += 1
            bar.next()

    degreeType: str = "in" if inDegree else "out"
    nodes: NodeView = graph.nodes()

    with Bar(
        f"Computing the {degreeType}-degree distribution of nodes... ", max=len(nodes)
    ) as progress:
        if inDegree:
            _iterateInDegree(nodes=nodes, bar=progress)
        else:
            _iterateOutDegree(nodes=nodes, bar=progress)

    return _sortDict(d=data)


def computeClusteringCoefficientDistribution(graph: DiGraph) -> dict[int, int]:
    data: defaultdict = defaultdict(int)

    nodes: NodeView = graph.nodes()

    with Bar(
        f"Computing the clustering coefficient distribution of nodes... ",
        max=len(nodes),
    ) as progress:
        node: str
        for node in nodes:
            coefficient: int | float = clustering(G=graph, nodes=node)
            data[coefficient] += 1
            progress.next()

    return _sortDict(d=data)


def computeNodeTypeDistribution(graph: DiGraph) -> dict[str, int]:
    data: defaultdict = defaultdict(int)

    nodes: NodeView = graph.nodes(data="Operation Type")

    with Bar(
        "Computing the distribution of node operations types... ", max=len(nodes)
    ) as progress:
        opType: str
        for _, opType in nodes:
            data[opType] += 1
            progress.next()

    return _sortDict(d=data)


def computeNodeTypePairingDistribution(graph: DiGraph) -> dict[str, int]:
    data: defaultdict = defaultdict(int)

    nodes: NodeView = graph.nodes(data="Operation Type")
    nodeIDs: List[str] = [node[0] for node in nodes]

    with Bar(
        "Computing the distribution of node operations types... ", max=len(nodes)
    ) as progress:
        nodeID: str
        for nodeID in nodeIDs:
            children: Generator = graph.successors(n=nodeID)
            nodeIDPairs: product[tuple[str, str]] = product([nodeID], children)

            pair: tuple[str, str]
            for pair in nodeIDPairs:
                key: str = f"{nodes[pair[0]]}, {nodes[pair[1]]}"
                data[key] += 1

            progress.next()

    return _sortDict(d=data)


def createJSON(graph: DiGraph) -> dict[str, Any]:
    data: dict[str, Any] = {}

    data["Graph Density"] = computeDensity(graph=graph)
    data["Node Count"] = countNodes(graph=graph)
    data["Edge Count"] = countEdges(graph=graph)
    data["Community Count"] = countCommunities(graph=graph)

    inDegreeDistribution: dict[int, int] = computeDegreeDistribution(
        graph=graph,
        inDegree=True,
    )

    outDegreeDistribution: dict[int, int] = computeDegreeDistribution(
        graph=graph,
        inDegree=False,
    )

    clusteringCoefficientDistribution: dict[
        int, int
    ] = computeClusteringCoefficientDistribution(graph=graph)

    nodeTypeDistribution: dict[str, int] = computeNodeTypeDistribution(graph=graph)

    nodeTypePairingDistribution: dict[str, int] = computeNodeTypePairingDistribution(
        graph=graph
    )

    data["In Degree Distribution"] = inDegreeDistribution
    data["Out Degree Distribution"] = outDegreeDistribution
    data["Clustering Coefficient Distribution"] = clusteringCoefficientDistribution
    data["Node Distribution"] = nodeTypePairingDistribution

    return _sortDict(d=data)


def main() -> None:
    args: Namespace = getArgs()

    graph: DiGraph = read_gexf(args.input[0])

    computeNodeTypePairingDistribution(graph=graph)

    json: dict[str, Any] = createJSON(graph=graph)

    with open(args.output[0], "w") as jsonFile:
        dump(obj=json, fp=jsonFile, indent=4)
        jsonFile.close()


if __name__ == "__main__":
    main()
