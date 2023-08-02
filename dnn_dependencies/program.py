from os import listdir
from pathlib import Path
from typing import List

import pandas
from networkx import DiGraph, read_gexf
from pandas import DataFrame
from progress.bar import Bar
from sqlalchemy import Connection, Engine, MetaData, create_engine

from dnn_dependencies.metrics import graphProperties
from dnn_dependencies.schemas import sqlDev


def openDBEngine(dbPath: Path) -> Engine:
    dbURI: str = f"sqlite:///{dbPath.absolute().__str__()}"
    return create_engine(url=dbURI)


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
    return df


def createBaseModelsDF(modelsDF: DataFrame) -> DataFrame:
    tempDF: DataFrame = DataFrame(
        modelsDF[modelsDF["Model Name"].str.contains("huggingface.co_")]
    )
    tempDF.drop(columns=["Model Name", "Model Filepath"], inplace=True)
    tempDF.columns = ["Model_ID"]
    df: DataFrame = tempDF.reset_index(drop=True)

    return df


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

    return pandas.concat(objs=dfList, ignore_index=True)


def main() -> None:
    dbPath: Path = Path("test.db")
    gexfDirectory: Path = Path("../data/gexfFiles_7-27-2023")

    dbEngine: Engine = openDBEngine(dbPath=dbPath)
    dbMetadata: MetaData = MetaData()

    sqlDev.createSchema_Models(metadata=dbMetadata)
    sqlDev.createSchema_BaseModels(metadata=dbMetadata)

    dbMetadata.create_all(bind=dbEngine)

    modelsDF: DataFrame = createModelsDF(directory=gexfDirectory)
    modelsDF.to_sql(name="Models", con=dbEngine, if_exists="append", index=False)

    baseModelsDF: DataFrame = createBaseModelsDF(modelsDF=modelsDF)
    baseModelsDF.to_sql(
        name="Base Models", con=dbEngine, if_exists="append", index=False
    )

    # modelPropertiesDF: DataFrame = createModelPropertiesDF(modelsDF=modelsDF)
    modelPropertiesDF: DataFrame = pandas.read_csv(
        filepath_or_buffer="modelProperties.csv"
    )


if __name__ == "__main__":
    main()
