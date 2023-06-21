from argparse import Namespace
from typing import List, Set

from networkx import DiGraph, read_gexf
from networkx.algorithms.community import louvain_communities

from dnn_dependencies.args.similarity_args import getArgs


def countNodes(graph: DiGraph) -> int:
    return graph.number_of_nodes()


def countEdges(graph: DiGraph) -> int:
    return graph.size()


def countCommunities(graph: DiGraph) -> int:
    communities: List[Set[str]] = louvain_communities(graph, seed=42)
    return len(communities)


def main() -> None:
    args: Namespace = getArgs()

    graph: Digraph = read_gexf(args.input[0])


if __name__ == "__main__":
    main()
