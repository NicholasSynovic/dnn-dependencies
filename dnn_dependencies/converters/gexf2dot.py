from argparse import Namespace

from networkx import Graph, read_gexf
from networkx.drawing.nx_pydot import write_dot

from dnn_dependencies.args.gexf2dot_args import getArgs


def main() -> None:
    args: Namespace = getArgs()

    graph: Graph = read_gexf(args.input[0])
    write_dot(graph, args.output[0])


if __name__ == "__main__":
    main()
