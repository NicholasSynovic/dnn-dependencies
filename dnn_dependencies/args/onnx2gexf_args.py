from argparse import ArgumentParser, Namespace
from importlib.metadata import version
from pathlib import Path

from dnn_dependencies import args as argVars

PROGRAM_NAME: str = "ONNX Computational Graph to GEXF XML Converter"


def getArgs() -> Namespace:
    """The function `getArgs()` is used to parse command line arguments for a program that converts an ONNX
    model's computational graph from a Protobuf format to a GEXF XML format.
    :return: an instance of the `Namespace` class, which contains the parsed command-line arguments.


    """
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
        "-i",
        "--input",
        nargs=1,
        type=Path,
        required=True,
        help="Path to an ONNX model",
    )
    parser.add_argument(
        "-o",
        "--output",
        nargs=1,
        type=Path,
        required=True,
        help="Path to store GEXF XML output",
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
