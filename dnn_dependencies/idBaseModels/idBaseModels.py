from pathlib import Path

import click
import pandas
from numpy import NaN
from pandas import DataFrame, Series
from sqlalchemy import Connection, Engine

from dnn_dependencies.schemas import sql

COLUMN: str = "Model Filepath"


def readDB(dbFile: Path) -> DataFrame:
    dbEngine: Engine = sql.createEngine(path=dbFile.__str__())
    dbConn: Connection = dbEngine.connect()

    df: DataFrame = pandas.read_sql_table(table_name="ModelStats", con=dbConn)

    return df


def createMask(df: DataFrame, column: str) -> Series:
    series: Series = df[column]
    mask: Series = (series.str.find("huggingface.co")) > -1
    return mask


def applyMask(df: DataFrame, mask: Series, column: str) -> DataFrame:
    df.loc[~mask, column] = NaN
    df.dropna(inplace=True, ignore_index=True)
    print(df)


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
    mask: Series = createMask(df=dbDF, column=COLUMN)
    applyMask(df=dbDF, mask=mask, column=COLUMN)


if __name__ == "__main__":
    main()
