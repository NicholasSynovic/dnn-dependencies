from argparse import ArgumentParser, Namespace
from importlib.metadata import version
from pathlib import Path

from dnn_dependencies import args as argVars

PROGRAM_NAME: str = "GEXF to Model FS"


def getArgs() -> Namespace:
    parser: ArgumentParser = ArgumentParser(
        prog=PROGRAM_NAME,
        description="A program to export a GEXF file to a directory path",
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
        "-r",
        "--root",
        nargs=1,
        type=Path,
        required=True,
        help="Root folder to store information in",
    )

    return parser.parse_args()
