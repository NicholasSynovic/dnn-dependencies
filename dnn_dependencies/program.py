from os import listdir
from pathlib import Path
from typing import List

from pandas import DataFrame
from progress.bar import Bar
from sqlalchemy import Engine, create_engine


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
    tempDF.reset_index()
    df: DataFrame = tempDF.reindex(columns=["ID", "Model Name", "Model Filepath"])

    return df


def main() -> None:
    dbPath: Path = Path("test.db")
    gexfDirectory: Path = Path("../data/gexfFiles_7-27-2023")

    dbEngine: Engine = openDBEngine(dbPath=dbPath)

    modelsDF: DataFrame = createModelsDF(directory=gexfDirectory)
    print(modelsDF)

    pass


if __name__ == "__main__":
    main()
