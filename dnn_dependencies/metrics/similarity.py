from argparse import Namespace
from collections import defaultdict
from typing import List, Set

from networkx import DiGraph, read_gexf
from networkx.algorithms.community import louvain_communities
from networkx.classes.reportviews import NodeDataView, NodeView
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
    degreeType: str = "in" if inDegree else "out"

    nodes: NodeView = graph.nodes()

    with Bar(
        f"Computing the distribution of {degreeType} degree nodes... ", max=len(nodes)
    ) as bar:
        node: str
        for node in nodes:
            degree: int = graph.out_degree(node)
            data[degree] += 1
            bar.next()

    data: dict[int, int] = dict(data)
    data = dict(sorted(data.items()))

    return data


def main() -> None:
    args: Namespace = getArgs()

    graph: Digraph = read_gexf(args.input[0])

    computeDistribution_OutDegree(graph)


if __name__ == "__main__":
    main()
