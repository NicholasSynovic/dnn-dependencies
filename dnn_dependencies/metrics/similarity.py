from argparse import Namespace
from collections import defaultdict
from typing import List, Set

from networkx import DiGraph, clustering, read_gexf
from networkx.algorithms.community import louvain_communities
from networkx.classes.reportviews import NodeView
from progress.bar import Bar

from dnn_dependencies.args.similarity_args import getArgs


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

    foo: dict[int, int] = dict(data)
    bar: dict[int, int] = dict(sorted(foo.items()))

    return bar


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

    foo: dict[int, int] = dict(data)
    bar: dict[int, int] = dict(sorted(foo.items()))

    return bar


def computeNodeDistribution(graph: DiGraph) -> dict[str, int]:
    data: defaultdict = defaultdict(int)

    nodes: NodeView = graph.nodes(data="Operation Type")
    print(nodes)


def main() -> None:
    args: Namespace = getArgs()

    graph: DiGraph = read_gexf(args.input[0])

    computeNodeDistribution(graph)


if __name__ == "__main__":
    main()
