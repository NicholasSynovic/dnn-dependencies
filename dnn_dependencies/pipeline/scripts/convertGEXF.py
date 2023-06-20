from argparse import ArgumentParser, Namespace

from networkx import Graph, read_gexf
from networkx.drawing.nx_pydot import write_dot


def getArgs() -> Namespace:
    parser: ArgumentParser = ArgumentParser(
        prog="GEXF 2 Dot file converter",
        description="A small tool to convert a GEXF file (for Gephi) to Dot (for Graphviz)",
    )
    parser.add_argument(
        "-i",
        "--input",
        required=True,
        help="Input GEXF file",
    )
    parser.add_argument(
        "-o",
        "--output",
        required=True,
        help="Output Dot file location path",
    )
    return parser.parse_args()


def main() -> None:
    args: Namespace = getArgs()

    graph: Graph = read_gexf(args.input)
    write_dot(graph, args.output)


if __name__ == "__main__":
    main()
