from pathlib import Path

import click
import pandas
from pandas import DataFrame
from sqlalchemy import Connection, Engine

from dnn_dependencies.schemas import sql


def readDB(dbFile: Path) -> DataFrame:
    dbEngine: Engine = sql.createEngine(path=dbFile.__str__())
    dbConn: Connection = dbEngine.connect()

    df: DataFrame = pandas.read_sql_table(table_name="ModelStats", con=dbConn)

    return df


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
    dbDF: DataFrame = readDB(dbFile=dbFile)
    print(dbDF)


if __name__ == "__main__":
    main()
