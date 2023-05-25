from argparse import ArgumentParser, Namespace
from importlib.metadata import version
from pathlib import Path

from dnn_dependencies import args as argVars

PROGRAM_NAME: str = "ONNX Layer Architecture GEXF Exporter"


def getArgs() -> Namespace:
    parser: ArgumentParser = ArgumentParser(
        prog=PROGRAM_NAME,
        description="A program to export an ONNX model's layer architecture as a GEXF file",
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
        "-m",
        "--model",
        nargs=1,
        type=str,
        required=True,
        help="Path to an ONNX model",
    )
    parser.add_argument(
        "-o",
        "--output",
        nargs=1,
        type=Path,
        default=Path("architecture.gexf"),
        required=False,
        help="Filepath to store GEXF output",
    )
    return parser.parse_args()
