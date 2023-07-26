import sqlite3
from argparse import Namespace
from os import listdir
from pathlib import Path
from sqlite3 import Connection
from typing import Any, List

import pandas
from pandas import DataFrame

from dnn_dependencies.args.computeMetrics_args import getArgs
from dnn_dependencies.metrics.metrics import *

RANDOM_SEED: int = 42

random.seed(a=RANDOM_SEED, version=2)
numpy.random.seed(seed=RANDOM_SEED)


def readFiles(directory: Path) -> List[DiGraph]:
    data: List[DiGraph] = []

    files: List[Path] = [Path(directory, f) for f in listdir(path=directory)]

    with Bar("Reading files to create DiGraphs... ", max=len(files)) as bar:
        file: Path
        for file in files:
            data.append(read_gexf(file))
            bar.next()

    return data


def getModelName(path: Path) -> str:
    return "fred"


def createDict(graph: DiGraph, modelName: str, modelFilepath: Path) -> dict[str, Any]:
    data: dict[str, Any] = {}

    with Bar("Computing metrics ", max=28) as bar:
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
        data["Robins Alexander Clustering"] = computeRobinsAlexanderClustering(
            graph=graph
        )
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


def dfToDB(df: DataFrame, dbPath: Path, table: str) -> None:
    conn: Connection = sqlite3.connect(database=dbPath)

    df.to_sql(
        name=table,
        con=conn,
        if_exists="append",
        index=True,
        index_label="ID",
    )

    conn.close()


def dfToCSV(df: DataFrame, output: Path) -> None:
    df.to_csv(path_or_buf=output, index=True, index_label="ID")


def main() -> None:
    args: Namespace = getArgs()

    dfList: List[DataFrame] = []
    gexfDirectory: Path = args.input[0]

    graphs: List[DiGraph] = readFiles(directory=gexfDirectory)

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

    df: DataFrame = pandas.concat(objs=dfList)
    # dfToDB(df=df, dbPath=args.output[0], table="Model Stats")
    dfToCSV(df=df, output=args.output[0])


if __name__ == "__main__":
    main()
