from concurrent.futures import ThreadPoolExecutor
from os import listdir
from pathlib import Path
from typing import Any, List

import click
import pandas
from networkx import DiGraph
from pandas import DataFrame
from progress.bar import Bar
from sqlalchemy import Engine, MetaData

from dnn_dependencies.metrics.metrics import *
from dnn_dependencies.schemas import sql

RANDOM_SEED: int = 42

random.seed(a=RANDOM_SEED, version=2)
numpy.random.seed(seed=RANDOM_SEED)


def readFiles(directory: Path) -> List[DiGraph]:
    """


    :param directory: Path:

    """

    data: List[DiGraph] = []

    files: List[Path] = [Path(directory, f) for f in listdir(path=directory)]

    with Bar("Reading files to create DiGraphs... ", max=len(files)) as bar:
        file: Path
        for file in files:
            data.append(read_gexf(file))
            bar.next()

    return data


def getModelName(path: Path) -> str:
    """


    :param path: Path:

    """
    return "fred"


def createDict(graph: DiGraph, modelName: str, modelFilepath: Path) -> dict[str, Any]:
    """


    :param graph: DiGraph:
    :param modelName: str:
    :param modelFilepath: Path:

    """
    data: dict[str, Any] = {}

    data["Model Name"] = modelName
    data["Model Filepath"] = modelFilepath.__str__()
    data["Is Semiconnected"] = checkIsSemiconnected(graph=graph)
    data["Is Attracting Component"] = checkIsAttractingComponent(graph=graph)
    data["Is Strongly Connected"] = checkIsStronglyConnected(graph=graph)
    data["Is Weakly Connected"] = checkIsWeaklyConnected(graph=graph)
    data["Is Triad"] = checkIsTriad(graph=graph)
    data["Is Regular"] = checkIsRegular(graph=graph)
    data["Is Planar"] = checkIsPlanar(graph=graph)
    data["Is Distance Regular"] = checkIsDistanceRegular(graph=graph)
    data["Is Strongly Regular"] = checkIsStronglyRegular(graph=graph)
    data["Is Bipartite"] = checkIsBipartite(graph=graph)
    data["Is Aperiodic"] = checkIsAperiodic(graph=graph)
    data["Is Directed Acyclic"] = checkIsDirectedAcyclicGraph(graph=graph)
    data["Radius"] = computeRadius(graph=graph)
    data["DAG Longest Path Length"] = computeDAGLongestPathLength(graph=graph)
    data["Number of Isolates"] = computeNumberOfIsolates(graph=graph)
    data["Robins Alexander Clustering"] = computeRobinsAlexanderClustering(graph=graph)
    data["Transitivity"] = computeTransitivity(graph=graph)
    data["Number of Nodes"] = computeNumberOfNodes(graph=graph)
    data["Density"] = computeDensity(graph=graph)
    data["Number of Edges"] = computeNumberOfEdges(graph=graph)
    data["Number of Communities"] = computeNumberOfCommunities(graph=graph)
    data["Degree Assortivity Coefficient"] = computeDegreeAssortativityCoefficient(
        graph=graph
    )
    data[
        "Attribute Assortivity Coefficient"
    ] = computeAttributeAssortativityCoefficient(graph=graph)
    data[
        "Number of Weakly Connected Components"
    ] = computeNumberOfWeaklyConnectedComponents(graph=graph)
    data[
        "Number of Strongly Connected Components"
    ] = computeNumberOfStronglyConnectedComponents(graph=graph)
    data["Number of Attracting Components"] = computeNumberOfAttracingComponents(
        graph=graph
    )
    data["Barycenter"] = computeBarycenter(graph=graph)
    data[
        "Degree Pearson Correlation Coefficient"
    ] = computeDegreePearsonCorrelationCoefficient(graph=graph)

    return data


def dfToDB(df: DataFrame, conn: Engine, table: str) -> None:
    """


    :param df: DataFrame:
    :param conn: Engine:
    :param table: str:

    """
    df.to_sql(
        name=table,
        con=conn,
        if_exists="fail",
        index=False,
    )


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
    dfList: List[DataFrame] = []

    dbConn: Engine = sql.createEngine(path=dbFile.__str__())
    dbMetadata: MetaData = MetaData()

    sql.schema_ModelStats(metadata=dbMetadata)
    sql.createTables(metadata=dbMetadata, engine=dbConn)

    graphs: List[DiGraph] = readFiles(directory=gexfDirectory)

    with Bar("Computing metrics... ", max=len(graphs)) as bar:
        graph: DiGraph
        for graph in graphs:
            modelName: str = getModelName(path=gexfDirectory)  # TODO: Fix this

            data: dict[str, Any] = createDict(
                graph=graph,
                modelName=modelName,
                modelFilepath=gexfDirectory,
            )

            df: DataFrame = DataFrame([data])
            dfList.append(df)

            bar.next()

    df: DataFrame = pandas.concat(objs=dfList)

    dfToDB(df=df, conn=dbConn, table="ModelStats")


if __name__ == "__main__":
    main()
