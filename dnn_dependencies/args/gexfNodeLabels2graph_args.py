from argparse import ArgumentParser, Namespace
from importlib.metadata import version
from pathlib import Path

from dnn_dependencies import args as argVars

PROGRAM_NAME: str = "GEXF XML Node Labels to Graphviz Dot File Extractor"


def getArgs() -> Namespace:
    parser: ArgumentParser = ArgumentParser(
        prog=PROGRAM_NAME,
        description="A program to extract node labels from a graph stored in a GEXF XML formatted file to a graph represented in a Graphviz Dot file format",
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
        help="Path to GEXF file",
    )
    parser.add_argument(
        "-o",
        "--output",
        nargs=1,
        type=Path,
        required=True,
        help="Path to store Graphviz file (.dot file)",
    )

    return parser.parse_args()
