import random
from pathlib import Path
from typing import List, Tuple

import click
import numpy
import pandas
from numpy import array, float64, ndarray
from pandas import DataFrame
from progress.bar import Bar
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler
from sqlalchemy import Engine

from dnn_dependencies.schemas import sql

random.seed(42)
numpy.random.seed(42)


def readDatabase(dbEngine: Engine) -> DataFrame:
    df: DataFrame = pandas.read_sql_table(
        table_name="Graph Properties",
        con=dbEngine,
    )
    return df


def preprocessDataFrame(df: DataFrame) -> Tuple[DataFrame, DataFrame]:
    columns: List[str] = ["ID", "Model_ID"]

    metadata: DataFrame = df[columns]
    df.drop(columns=columns, inplace=True)

    return (metadata, df)


def computeNeighbors(df: DataFrame) -> Tuple[ndarray, ndarray]:
    print("Computing neighbors...")
    data: ndarray = df.to_numpy()

    scaler: StandardScaler = StandardScaler()
    nn: NearestNeighbors = NearestNeighbors(
        n_neighbors=df.shape[0],
        metric="euclidean",
        n_jobs=-1,
    )

    scaler.fit(data)
    scaledData: ndarray = scaler.transform(data)

    nn.fit(scaledData)

    neighbors: Tuple[ndarray, ndarray] = nn.kneighbors(scaledData)

    return neighbors


def postProcessNeighbors(
    metadata: DataFrame, neighbors: Tuple[ndarray, ndarray]
) -> DataFrame:
    dfList: List[DataFrame] = []

    distances, idx = neighbors
    neighborPairs: List[Tuple[array, array]] = list(zip(idx, distances))

    with Bar("Post-processing data... ", max=len(neighborPairs)) as bar:
        pair: Tuple[array, array]
        for pair in neighborPairs:
            idx, distances = pair
            alignedPairs: List[Tuple[int, float64]] = list(zip(idx, distances))

            rawDict: dict[int, float64] = {key: value for key, value in alignedPairs}
            sortedDict: dict[int, float64] = dict(sorted(rawDict.items()))

            rowDF: DataFrame = DataFrame(data=[sortedDict])
            dfList.append(rowDF)
            bar.next()

    df: DataFrame = pandas.concat(objs=dfList, ignore_index=True)
    df.add_prefix(prefix="Model_ID_")
    df.insert(loc=0, column="Model_ID", value=metadata["Model_ID"])
    return df


def dist(row: int, df: DataFrame) -> None:
    rowIndex = row
    rowSort = df.iloc[rowIndex, :]
    sortRowVals = sorted(rowSort)
    df.iloc[rowIndex, :] = sortRowVals
    printRow = df.iloc[rowIndex, :]
    print(printRow)


@click.command()
@click.option(
    "dbFile",
    "-i",
    "--input",
    type=Path,
    required=True,
    nargs=1,
    help="Path to a SQLite3 database to read graph properties from",
)
@click.option(
    "outputPath",
    "-o",
    "--output",
    type=Path,
    required=True,
    nargs=1,
    help="Path to a CSV file to store results",
)
def main(dbFile: Path, outputPath: Path) -> None:
    dbEngine: Engine = sql.openDBEngine(dbPath=dbFile)
    rawDF: DataFrame = readDatabase(dbEngine=dbEngine)

    metadata, df = preprocessDataFrame(df=rawDF)

    neighbors: Tuple[ndarray, ndarray] = computeNeighbors(df=df)

    df: DataFrame = postProcessNeighbors(metadata=metadata, neighbors=neighbors)

    df.to_csv(path_or_buf=outputPath, index=False)


if __name__ == "__main__":
    main()
