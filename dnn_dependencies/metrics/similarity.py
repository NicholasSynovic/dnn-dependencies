from argparse import Namespace
from collections import defaultdict
from pprint import pprint
from typing import Any, List, Set

from networkx import DiGraph, clustering, density, read_gexf
from networkx.algorithms import average_shortest_path_length
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


def computeClusterCoefficientDistribution(graph: DiGraph) -> dict[int, int]:
    data: defaultdict = defaultdict(int)

    nodes: NodeView = graph.nodes()

    with Bar(
        f"Computing the clustering coefficient distribution of nodes... ",
        max=len(nodes),
    ) as progress:
        node: str
        for node in nodes:
            coefficient: int = clustering(G=graph, nodes=node)
            data[coefficient] += 1
            progress.next()

    return _sortDict(d=data)


def computeNodeDistribution(graph: DiGraph) -> dict[str, int]:
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


def main() -> None:
    args: Namespace = getArgs()

    graph: DiGraph = read_gexf(args.input[0])

    pprint(computeAverageShortestPath(graph))


if __name__ == "__main__":
    main()
