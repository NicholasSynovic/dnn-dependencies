import random
from os import listdir
from pathlib import Path
from typing import Any, List, Tuple

import click
import numpy
import pandas
from networkx import DiGraph, read_gexf
from pandas import DataFrame
from progress.bar import Bar
from sqlalchemy import Engine, MetaData

from dnn_dependencies.metrics.graphProperties import _run as metricComputer
from dnn_dependencies.schemas import sql

RANDOM_SEED: int = 42

random.seed(a=RANDOM_SEED, version=2)
numpy.random.seed(seed=RANDOM_SEED)


def readFiles(directory: Path) -> List[Tuple[Path, DiGraph]]:
    """


    :param directory: Path:

    """

    data: List[DiGraph] = []

    files: List[Path] = [Path(directory, f) for f in listdir(path=directory)]

    files = files[0:2]

    with Bar("Reading files to create DiGraphs... ", max=len(files)) as bar:
        file: Path
        for file in files:
            data.append(read_gexf(file))
            bar.next()

    return list(zip(files, data))


def getModelName(path: Path) -> str:
    """


    :param path: Path:

    """
    name: str = path.stem
    splitName: List[str] = name.split("_")
    modelName: str = f"{splitName[0]}/{'_'.join(splitName[1::])}".replace(".onnx", "")

    return modelName


def dfToDB(df: DataFrame, conn: Engine, table: str) -> None:
    """


    :param df: DataFrame:
    :param conn: Engine:
    :param table: str:

    """
    df.to_sql(name=table, con=conn, if_exists="replace", index=True, index_label="ID")


@click.command()
@click.option(
    "gexfDirectory",
    "-i",
    "--input",
    type=Path,
    required=True,
    nargs=1,
    help="Path to a directory containing at least one (1) GEXF file",
)
@click.option(
    "dbFile",
    "-o",
    "--output",
    type=Path,
    required=True,
    nargs=1,
    help="Path to SQLite3 database to store data",
)
def main(gexfDirectory: Path, dbFile: Path) -> None:
    """
    Compute graph metrics for GEXF files stored in a directory
    \f

    :param gexfDirectory: Path:
    :param dbFile: Path:

    """
    if dbFile.is_file():
        print("Output database already exists. Exiting program")
        quit(1)

    dfList: List[DataFrame] = []

    from sqlalchemy import create_engine

    dbConn: Engine = create_engine(url=f"sqlite:///{dbFile.absolute().__str__()}")
    dbMetadata: MetaData = MetaData()

    # sql.schema_ModelStats(metadata=dbMetadata)
    # sql.createTables(metadata=dbMetadata, engine=dbConn)

    graphs: List[Tuple[Path, DiGraph]] = readFiles(directory=gexfDirectory)

    with Bar("Computing metrics... ", max=len(graphs)) as bar:
        pair: Tuple[Path, DiGraph]
        for pair in graphs:
            modelName: str = getModelName(path=pair[0])

            data: DataFrame = metricComputer(pair[1])

            print()
            print(data)
            quit()

            df: DataFrame = DataFrame([data])
            dfList.append(df)

            bar.next()

    df: DataFrame = pandas.concat(objs=dfList)

    dfToDB(df=df, conn=dbConn, table="ModelStats")


if __name__ == "__main__":
    main()
