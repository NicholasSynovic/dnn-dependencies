from argparse import ArgumentParser, Namespace
from importlib.metadata import version
from pathlib import Path

from dnn_dependencies import args as argVars

PROGRAM_NAME: str = "HuggingFace Models to GEXF"


def getArgs() -> Namespace:
    parser: ArgumentParser = ArgumentParser(
        prog=PROGRAM_NAME,
        description="A program to export a HuggingFace model to a GEXF formatted XML file",
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
        type=Path,
        required=True,
        help="Path to a HuggingFace model (Can also be a HuggingFace repository for hosted projects)",
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
    parser.add_argument(
        "--onnx",
        action="store_true",
        help="Flag to keep the generated ONNX model (DEFAULT: Delete the ONNX model)",
    )
    return parser.parse_args()
