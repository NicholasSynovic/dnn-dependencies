from argparse import ArgumentParser, Namespace
from importlib.metadata import version
from pathlib import Path

from dnn_dependencies import args as argVars

PROGRAM_NAME: str = "ONNX Computational Graph to GEXF XML Converter"


def getArgs() -> Namespace:
    parser: ArgumentParser = ArgumentParser(
        prog=PROGRAM_NAME,
        description="A program to convert an ONNX model's computational graph from a Protobuf format to a GEXF XML format",
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
        help="Filepath to store GEXF XML output",
    )
    parser.add_argument(
        "--mode",
        default="production",
        type=str,
        choices=["production", "validation"],
        required=False,
        help="Output a GEXF XML file for usage in NetworkX or Gephi (production), or for validation (validation)",
    )
    return parser.parse_args()
