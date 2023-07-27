from pathlib import Path

import click
import pandas
from pandas import DataFrame


@click.command()
@click.option(
    "dbFile",
    "-i",
    "--input",
    nargs=1,
    type=Path,
    help="Path to database to read from and write to",
)
def main(dbFile: Path) -> None:
    pass


if __name__ == "__main__":
    main()
