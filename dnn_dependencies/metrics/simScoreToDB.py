import os
import sqlite3
from argparse import Namespace
from pathlib import Path
from typing import Any

import pandas
from pandas import DataFrame

from dnn_dependencies.args.simScoreToDB_args import getArgs
from dnn_dependencies.metrics.metrics import *

RANDOM_SEED: int = 42

random.seed(a=RANDOM_SEED, version=2)
numpy.random.seed(seed=RANDOM_SEED)


def createDict(graph: DiGraph, modelName, modelFilepath) -> dict[str, Any]:
    """
    The function `createJSON` takes a directed graph as input and returns a dictionary containing
    various statistics and distributions computed from the graph.

    :param graph: The `graph` parameter is of type `DiGraph`, which represents a directed graph. It is
    used as input to compute various properties of the graph, such as density, node count, edge count,
    community count, degree distribution, clustering coefficient distribution, and node type
    distribution
    :type graph: DiGraph
    :return: The function `createJSON` returns a dictionary containing various metrics and distributions
    computed from the input graph.
    """
    data: dict[str, Any] = {}

    with Bar("Computing metrics ", max=30) as bar:
        data["Model Name"] = modelName
        data["Model Filepath"] = modelFilepath
        data["Is Semiconnected"] = checkIsSemiconnected(graph=graph, bar=bar)
        data["Is Attracting Component"] = checkIsAttractingComponent(
            graph=graph, bar=bar
        )
        data["Is Strongly Connected"] = checkIsStronglyConnected(graph=graph, bar=bar)
        data["Is Weakly Connected"] = checkIsWeaklyConnected(graph=graph, bar=bar)
        data["Is Triad"] = checkIsTriad(graph=graph, bar=bar)
        data["Is Regular"] = checkIsRegular(graph=graph, bar=bar)
        data["Is Planar"] = checkIsPlanar(graph=graph, bar=bar)
        data["Is Distance Regular"] = checkIsDistanceRegular(graph=graph, bar=bar)
        data["Is Strongly Regular"] = checkIsStronglyRegular(graph=graph, bar=bar)
        data["Is Bipartite"] = checkIsBipartite(graph=graph, bar=bar)
        data["Is Aperiodic"] = checkIsAperiodic(graph=graph, bar=bar)
        data["Is Directed Acyclic"] = checkIsDirectedAcyclicGraph(graph=graph, bar=bar)
        data["Radius"] = computeRadius(graph=graph, bar=bar)
        data["DAG Longest Path Length"] = computeDAGLongestPathLength(
            graph=graph, bar=bar
        )
        data["Number of Isolates"] = computeNumberOfIsolates(graph=graph, bar=bar)
        data["Robins Alexander Clustering"] = computeRobinsAlexanderClustering(
            graph=graph, bar=bar
        )
        data["Transitivity"] = computeTransitivity(graph=graph, bar=bar)
        data["Number of Nodes"] = computeNumberOfNodes(graph=graph, bar=bar)
        data["Density"] = computeDensity(graph=graph, bar=bar)
        data["Number of Edges"] = computeNumberOfEdges(graph=graph, bar=bar)
        data["Number of Communities"] = computeNumberOfCommunities(graph=graph, bar=bar)
        data["Degree Assortivity Coefficient"] = computeDegreeAssortativityCoefficient(
            graph=graph, bar=bar
        )
        data[
            "Attribute Assortivity Coefficient"
        ] = computeAttributeAssortativityCoefficient(graph=graph, bar=bar)
        data[
            "Number of Weakly Connected Components"
        ] = computeNumberOfWeaklyConnectedComponents(graph=graph, bar=bar)
        data[
            "Number of Strongly Computed Components"
        ] = computeNumberOfStronglyConnectedComponents(graph=graph, bar=bar)
        data["Number of Attracting Components"] = computeNumberOfAttracingComponents(
            graph=graph, bar=bar
        )
        data["Barycenter"] = computeBarycenter(graph=graph, bar=bar)
        data[
            "Degree Pearson Correlation Coefficient"
        ] = computeDegreePearsonCorrelationCoefficient(graph=graph, bar=bar)

    return data


def convertDf(databaseFile: str, tableName: str, df: DataFrame) -> int:
    sqlite = sqlite3.connect(databaseFile)

    rows: int = df.to_sql(tableName, sqlite, if_exists="append")

    return rows


def dictToDF(dict: dict) -> DataFrame:
    df = DataFrame([dict]).set_index("Model Name")
    return df


def splitInput(inputFile) -> tuple:
    file = Path(inputFile)
    name = file.stem
    return name


def main() -> None:
    args: Namespace = getArgs()

    graph: DiGraph = read_gexf(args.input[0])

    input = args.input[0]

    modelName = splitInput(input)

    modelFilepath = os.path.abspath(args.input[0])

    scoreDict: dict[str, Any] = createDict(
        graph=graph, modelName=modelName, modelFilepath=modelFilepath
    )

    df = dictToDF(dict=scoreDict)

    print(convertDf(databaseFile="models.db", tableName="scores", df=df))
    print("added to database")
    # print(df)


# databaseFile="models.db"


if __name__ == "__main__":
    main()
