from argparse import ArgumentParser, Namespace
from importlib.metadata import version
from pathlib import Path

from dnn_dependencies import args as argVars

PROGRAM_NAME: str = "GEXF XML to Graphviz Dot Converter"


def getArgs() -> Namespace:
    """
    The function `getArgs()` is used to parse command line arguments for a program that converts a graph
    in GEXF file format to a Graphviz Dot file.
    :return: an instance of the `Namespace` class, which contains the parsed command-line arguments.
    """
    parser: ArgumentParser = ArgumentParser(
        prog=PROGRAM_NAME,
        description="A program to convert a graph in GEXF file format to a Graphviz Dot file",
        epilog=f"Created by: {', '.join(argVars.authorsList)}",
        formatter_class=argVars.AlphabeticalOrderHelpFormatter,
    )
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=f"{PROGRAM_NAME}: {version(distribution_name='dnn-dependencies')}",
    )
    parser.add_argument(
        "-i",
        "--input",
        nargs=1,
        type=Path,
        required=True,
        help="Path to a GEXF file",
    )
    parser.add_argument(
        "-o",
        "--output",
        nargs=1,
        type=Path,
        required=True,
        help="Path to store data in database",
    )
    return parser.parse_args()
