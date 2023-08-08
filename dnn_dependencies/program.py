from os import listdir
from pathlib import Path
from typing import List

import click
import pandas
from networkx import DiGraph, read_gexf
from pandas import DataFrame
from progress.bar import Bar
from sqlalchemy import Connection, Engine, MetaData, create_engine

from dnn_dependencies.metrics import graphProperties
from dnn_dependencies.schemas import sql
from dnn_dependencies.schemas.df import (BaseModelsDF, GraphPropertiesDF,
                                         ModelsDF)


def createModelsDF(directory: Path) -> DataFrame:
    data: dict[str, List[str]] = {"Model Name": [], "Model Filepath": []}

    files: List[Path] = [Path(directory, file) for file in listdir(path=directory)]

    with Bar(
        "Creating DataFrame of model names and filepaths... ", max=len(files)
    ) as bar:
        file: Path
        for file in files:
            data["Model Filepath"].append(file.__str__())

            modelName: str = file.stem.replace(".onnx", "")
            data["Model Name"].append(modelName)

            bar.next()

    tempDF: DataFrame = DataFrame(data=data)
    tempDF["ID"] = tempDF.index
    tempDF.reset_index(inplace=True, drop=True)
    df: DataFrame = tempDF.reindex(columns=["ID", "Model Name", "Model Filepath"])

    typedDF: DataFrame = ModelsDF.convert(df=df, add_optional_cols=False).df

    return typedDF


def createBaseModelsDF(modelsDF: DataFrame) -> DataFrame:
    tempDF: DataFrame = DataFrame(
        modelsDF[modelsDF["Model Name"].str.contains("huggingface.co_")]
    )
    tempDF.drop(columns=["Model Name", "Model Filepath"], inplace=True)
    tempDF.columns = ["Model_ID"]
    df: DataFrame = tempDF.reset_index(drop=True)
    df["ID"] = df.index

    typedDF: DataFrame = BaseModelsDF.convert(df=df, add_optional_cols=False).df

    return typedDF


def createModelPropertiesDF(modelsDF: DataFrame) -> DataFrame:
    dfList: List[DataFrame] = []

    with Bar("Computing properties of models... ", max=modelsDF.shape[0]) as bar:
        MODEL_ID: int
        MODEL_FILEPATH: str
        for MODEL_ID, _, MODEL_FILEPATH in modelsDF.itertuples(index=False):
            graph: DiGraph = read_gexf(MODEL_FILEPATH)

            df: DataFrame = graphProperties._run(graph=graph, id=MODEL_ID)
            dfList.append(df)
            bar.next()

    df: DataFrame = pandas.concat(objs=dfList, ignore_index=True)

    typedDF: DataFrame = GraphPropertiesDF.convert(df=df, add_optional_cols=False).df

    return typedDF


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

    dbEngine: Engine = sql.openDBEngine(dbPath=dbFile)
    dbMetadata: MetaData = MetaData()

    sql.createSchema_Models(metadata=dbMetadata)
    sql.createSchema_BaseModels(metadata=dbMetadata)
    sql.createSchema_GraphProperties(metadata=dbMetadata)

    dbMetadata.create_all(bind=dbEngine)

    modelsDF: DataFrame = createModelsDF(directory=gexfDirectory)
    modelsDF.to_sql(
        name="Models",
        con=dbEngine,
        if_exists="append",
        index=False,
    )

    baseModelsDF: DataFrame = createBaseModelsDF(modelsDF=modelsDF)
    baseModelsDF.to_sql(
        name="Base Models",
        con=dbEngine,
        if_exists="append",
        index=False,
    )

    graphPropertiesDF: DataFrame = createModelPropertiesDF(modelsDF=modelsDF)
    graphPropertiesDF.to_sql(
        name="Graph Properties",
        con=dbEngine,
        if_exists="append",
        index=False,
    )


if __name__ == "__main__":
    main()
