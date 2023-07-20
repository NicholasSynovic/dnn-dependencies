import json
import os
import random
import sqlite3
from argparse import Namespace
from collections import defaultdict
from json import dump
from typing import Any, List, Literal, Set

import numpy
import pandas as pd
from networkx import *
from networkx.algorithms import *
from networkx.algorithms.approximation import *
from networkx.algorithms.assortativity import *
from networkx.algorithms.bipartite import robins_alexander_clustering
from networkx.algorithms.community import louvain_communities
from networkx.algorithms.components import *
from networkx.algorithms.threshold import is_threshold_graph
from networkx.exception import NetworkXNoPath
from progress.bar import Bar

from dnn_dependencies.args.simScoreToDB_args import getArgs

RANDOM_SEED: int = 42

random.seed(a=RANDOM_SEED, version=2)
numpy.random.seed(seed=RANDOM_SEED)


def computeBarycenter(graph: DiGraph, bar: Bar) -> int:
    try:
        value: int = len(barycenter(G=graph))
    except NetworkXNoPath:
        value: int = -1
    bar.next()
    return value


def computeRadius(graph: DiGraph, bar: Bar) -> int:
    try:
        value: int = radius(G=graph)
    except NetworkXError:
        value: int = -1
    bar.next()
    return value


def computeDAGLongestPathLength(graph: DiGraph, bar: Bar) -> int:
    value: int = dag_longest_path_length(G=graph)
    bar.next()
    return value


def computeAverageShortestPathLength(graph: DiGraph, bar: Bar) -> float:
    value: float = average_shortest_path_length(G=graph)
    bar.next()
    return value


def computeNumberOfIsolates(graph: DiGraph, bar: Bar) -> int:
    value: int = number_of_isolates(G=graph)
    bar.next()
    return value


def checkIsTriad(graph: DiGraph, bar: Bar) -> int:
    value: int = int(is_triad(G=graph))
    bar.next()
    return value


def checkIsThresholdGraph(graph: DiGraph, bar: Bar) -> int:
    value: int = int(is_threshold_graph(G=graph))
    bar.next()
    return value


def checkIsRegular(graph: DiGraph, bar: Bar) -> int:
    value: int = int(is_regular(G=graph))
    bar.next()
    return value


def checkIsPlanar(graph: DiGraph, bar: Bar) -> int:
    value: int = int(is_planar(G=graph))
    bar.next()
    return value


def checkIsDistanceRegular(graph: DiGraph, bar: Bar) -> int:
    value: int = int(is_distance_regular(G=graph))
    bar.next()
    return value


def checkIsStronglyRegular(graph: DiGraph, bar: Bar) -> int:
    value: int = int(is_strongly_regular(G=graph))
    bar.next()
    return value


def checkIsBipartite(graph: DiGraph, bar: Bar) -> int:
    value: int = int(is_bipartite(G=graph))
    bar.next()
    return value


def computeRobinsAlexanderClustering(graph: DiGraph, bar: Bar) -> float | Literal[0]:
    value: float | Literal[0] = robins_alexander_clustering(G=graph)
    bar.next()
    return value


def computeTransitivity(graph: DiGraph, bar: Bar) -> float | Literal[0]:
    value: float | Literal[0] = transitivity(G=graph)
    bar.next()
    return value


def checkIsAperiodic(graph: DiGraph, bar: Bar) -> int:
    value: int = int(is_aperiodic(G=graph))
    bar.next()
    return value


def checkIsDirectedAcyclicGraph(graph: DiGraph, bar: Bar) -> int:
    value: int = int(is_directed_acyclic_graph(G=graph))
    bar.next()
    return value


def computeNumberOfNodes(graph: DiGraph, bar: Bar) -> int:
    """
    The function countNodes takes a directed graph as input and returns the number of nodes in the
    graph.

    :param graph: The parameter `graph` is of type `DiGraph`, which suggests that it is a directed graph
    :type graph: DiGraph
    :return: the number of nodes in the given graph.
    """
    value: int = graph.number_of_nodes()
    bar.next()
    return value


def computeDensity(graph: DiGraph, bar: Bar) -> float:
    """
    The function `computeDensity` calculates the density of a directed graph.

    :param graph: The parameter `graph` is expected to be a directed graph (DiGraph) object
    :type graph: DiGraph
    :return: a float value, which represents the density of the given directed graph.
    """
    value: int = density(G=graph)
    bar.next()
    return value


def computeNumberOfEdges(graph: DiGraph, bar: Bar) -> int:
    """
    The function countEdges takes a directed graph as input and returns the number of edges in the
    graph.

    :param graph: The parameter `graph` is expected to be an instance of a directed graph (DiGraph)
    :type graph: DiGraph
    :return: the number of edges in the given directed graph.
    """
    value: int = graph.number_of_edges()
    bar.next()
    return value


def computeNumberOfCommunities(graph: DiGraph, bar: Bar) -> int:
    """
    The function `computeNumberOfCommunities` takes a directed graph as input and returns the number of
    communities detected using the Louvain algorithm.

    :param graph: The `graph` parameter is a directed graph object. It represents a network or a set of
    connections between nodes. The graph can be represented using a data structure such as an adjacency
    matrix or an adjacency list
    :type graph: DiGraph
    :param bar: A `progess.bar.Bar` object
    :type bar: Bar
    :return: the number of communities detected in the given graph.
    """
    communities: List[Set[str]] = louvain_communities(graph, seed=42)
    value: int = len(communities)
    bar.next()
    return value


def computeDiameter(graph: DiGraph, bar: Bar) -> int:
    value: int = diameter(G=graph)
    bar.next()
    return value


def computeDegreeAssortativityCoefficient(graph: DiGraph, bar: Bar) -> float:
    value: float = degree_assortativity_coefficient(G=graph, x="out", y="in")
    bar.next()
    return value


def computeAttributeAssortativityCoefficient(graph: DiGraph, bar: Bar) -> float:
    value: float = attribute_assortativity_coefficient(
        G=graph,
        attribute="Operation_Type",
    )
    bar.next()
    return value


def computeDegreePearsonCorrelationCoefficient(graph: DiGraph, bar: Bar) -> float:
    value: float = degree_pearson_correlation_coefficient(
        G=graph,
        x="out",
        y="in",
    )
    bar.next()
    return value


def checkIsSemiconnected(graph: DiGraph, bar: Bar) -> int:
    value: int = int(is_semiconnected(G=graph))
    bar.next()
    return value


def checkIsAttractingComponent(graph: DiGraph, bar: Bar) -> int:
    value: int = int(is_attracting_component(G=graph))
    bar.next()
    return value


def checkIsStronglyConnected(graph: DiGraph, bar: Bar) -> int:
    value: int = int(is_strongly_connected(G=graph))
    bar.next()
    return value


def checkIsWeaklyConnected(graph: DiGraph, bar: Bar) -> int:
    value: int = int(is_weakly_connected(G=graph))
    bar.next()
    return value


def computeNumberOfWeaklyConnectedComponents(graph: DiGraph, bar: Bar) -> int:
    value: int = number_weakly_connected_components(G=graph)
    bar.next()
    return value


def computeNumberOfStronglyConnectedComponents(graph: DiGraph, bar: Bar) -> int:
    value: int = number_strongly_connected_components(G=graph)
    bar.next()
    return value


def computeNumberOfAttracingComponents(graph: DiGraph, bar: Bar) -> int:
    value: int = number_attracting_components(G=graph)
    bar.next()
    return value


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


def convertJson(jsonFile: str) -> pd.DataFrame:
    return pd.read_json(jsonFile)


def convertDf(databaseFile: str, tableName: str, df: pd.DataFrame) -> int:
    sqlite = sqlite3.connect(databaseFile)

    rows: int = df.to_sql(tableName, sqlite, if_exists="append")

    return rows


def dictToDF(dict: dict) -> pd.DataFrame:
    df = pd.DataFrame([dict]).set_index("Model Name")
    return df


def convertDf(databaseFile: str, tableName: str, df: pd.DataFrame) -> int:
    sqlite = sqlite3.connect(databaseFile)

    rows: int = df.to_sql(tableName, sqlite, if_exists="append")

    return rows


def splitInput(inputFile) -> tuple:
    fileString = str(inputFile)
    split = fileString.split(".")
    return tuple(split)


def main() -> None:
    args: Namespace = getArgs()

    graph: DiGraph = read_gexf(args.input[0])

    input = args.input[0]

    modelName, extension = splitInput(input)

    modelFilepath = os.path.abspath(args.input[0])

    scoreDict: dict[str, Any] = createDict(
        graph=graph, modelName=modelName, modelFilepath=modelFilepath
    )

    df = dictToDF(dict=scoreDict)

    print(convertDf(databaseFile=args.output[0], tableName="scores", df=df))
    print(df)


# databaseFile="models.db"


if __name__ == "__main__":
    main()
