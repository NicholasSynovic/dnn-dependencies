from argparse import ArgumentParser, Namespace
from importlib.metadata import version

from dnn_dependencies import args as argVars


def getArgs(programName: str, description: str = "") -> Namespace:
    parser: ArgumentParser = ArgumentParser(
        prog=programName,
        description=description,
        epilog=f"Created by: {', '.join(argVars.authorsList)}",
        formatter_class=argVars.AlphabeticalOrderHelpFormatter,
    )
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=f"{programName}: {version(distribution_name='dnn-dependencies')}",
    )
    parser.add_argument(
        "-m",
        "--model",
        nargs=1,
        required=True,
        help="Path to or HuggingFace repository name to utilize model from",
    )
    return parser.parse_args()
