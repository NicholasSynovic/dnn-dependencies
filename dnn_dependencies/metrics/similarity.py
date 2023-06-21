from argparse import Namespace
from typing import List

from networkx import DiGraph, read_gexf

from dnn_dependencies.args.similarity_args import getArgs


def countNodes(graph: DiGraph) -> int:
    return graph.number_of_nodes()


def countEdges(graph: DiGraph) -> int:
    return graph.size()


def main() -> None:
    args: Namespace = getArgs()

    graph: Digraph = read_gexf(args.input[0])


if __name__ == "__main__":
    main()
