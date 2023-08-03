import random
from typing import List, Literal, Set

import numpy
from networkx import *
from networkx.algorithms import *
from networkx.algorithms.approximation import *
from networkx.algorithms.assortativity import *
from networkx.algorithms.bipartite import robins_alexander_clustering
from networkx.algorithms.community import louvain_communities
from networkx.algorithms.components import *
from networkx.algorithms.threshold import is_threshold_graph
from networkx.exception import NetworkXNoPath, NetworkXNotImplemented
from pandas import DataFrame

RANDOM_SEED: int = 42

random.seed(a=RANDOM_SEED, version=2)
numpy.random.seed(seed=RANDOM_SEED)


def computeBarycenter(graph: DiGraph) -> int:
    """


    :param graph: DiGraph:
    :param bar: Bar:

    """
    try:
        value: int = len(barycenter(G=graph))
    except NetworkXNoPath:
        value: int = -1
    return value


def computeRadius(graph: DiGraph) -> int:
    """


    :param graph: DiGraph:
    :param bar: Bar:

    """
    try:
        value: int = radius(G=graph)
    except NetworkXError:
        value: int = -1
    return value


def computeDAGLongestPathLength(graph: DiGraph) -> int:
    """


    :param graph: DiGraph:
    :param bar: Bar:

    """
    value: int = dag_longest_path_length(G=graph)
    return value


def computeAverageShortestPathLength(graph: DiGraph) -> float | int:
    """


    :param graph: DiGraph:
    :param bar: Bar:

    """
    try:
        value: float = average_shortest_path_length(G=graph)
    except NetworkXError:
        value: int = -1
    return value


def computeNumberOfIsolates(graph: DiGraph) -> int:
    """


    :param graph: DiGraph:
    :param bar: Bar:

    """
    value: int = number_of_isolates(G=graph)
    return value


def checkIsTriad(graph: DiGraph) -> int:
    """


    :param graph: DiGraph:
    :param bar: Bar:

    """
    value: int = int(is_triad(G=graph))
    return value


def checkIsThresholdGraph(graph: DiGraph) -> int:
    """


    :param graph: DiGraph:
    :param bar: Bar:

    """
    value: int = int(is_threshold_graph(G=graph))
    return value


def checkIsRegular(graph: DiGraph) -> int:
    """


    :param graph: DiGraph:
    :param bar: Bar:

    """
    value: int = int(is_regular(G=graph))
    return value


def checkIsPlanar(graph: DiGraph) -> int:
    """


    :param graph: DiGraph:
    :param bar: Bar:

    """
    value: int = int(is_planar(G=graph))
    return value


def checkIsDistanceRegular(graph: DiGraph) -> int:
    """


    :param graph: DiGraph:
    :param bar: Bar:

    """
    try:
        value: int = int(is_distance_regular(G=graph))
    except NetworkXNotImplemented:
        value: int = -1
    return value


def checkIsStronglyRegular(graph: DiGraph) -> int:
    """


    :param graph: DiGraph:
    :param bar: Bar:

    """
    try:
        value: int = int(is_strongly_regular(G=graph))
    except NetworkXNotImplemented:
        value: int = -1
    return value


def checkIsBipartite(graph: DiGraph) -> int:
    """


    :param graph: DiGraph:
    :param bar: Bar:

    """
    value: int = int(is_bipartite(G=graph))
    return value


def computeRobinsAlexanderClustering(graph: DiGraph) -> float | Literal[0]:
    """


    :param graph: DiGraph:
    :param bar: Bar:

    """
    value: float | Literal[0] = robins_alexander_clustering(G=graph)
    return value


def computeTransitivity(graph: DiGraph) -> float | Literal[0]:
    """


    :param graph: DiGraph:
    :param bar: Bar:

    """
    try:
        value: float | Literal[0] = transitivity(G=graph)
    except NetworkXNotImplemented:
        value: float = -1.0
    return value


def checkIsAperiodic(graph: DiGraph) -> int:
    """


    :param graph: DiGraph:
    :param bar: Bar:

    """
    value: int = int(is_aperiodic(G=graph))
    return value


def checkIsDirectedAcyclicGraph(graph: DiGraph) -> int:
    """


    :param graph: DiGraph:
    :param bar: Bar:

    """
    value: int = int(is_directed_acyclic_graph(G=graph))
    return value


def computeNumberOfNodes(graph: DiGraph) -> int:
    """


    :param graph: DiGraph:
    :param bar: Bar:

    """
    value: int = graph.number_of_nodes()
    return value


def computeDensity(graph: DiGraph) -> float:
    """


    :param graph: DiGraph:
    :param bar: Bar:

    """
    value: int = density(G=graph)
    return value


def computeNumberOfEdges(graph: DiGraph) -> int:
    """


    :param graph: DiGraph:
    :param bar: Bar:

    """
    value: int = graph.number_of_edges()
    return value


def computeNumberOfCommunities(graph: DiGraph) -> int:
    """


    :param graph: DiGraph:
    :param bar: Bar:

    """
    communities: List[Set[str]] = louvain_communities(graph, seed=42)
    value: int = len(communities)
    return value


def computeDiameter(graph: DiGraph) -> int:
    """


    :param graph: DiGraph:
    :param bar: Bar:

    """
    try:
        value: int = diameter(G=graph)
    except NetworkXError:
        value: int = -1
    return value


def computeDegreeAssortativityCoefficient(graph: DiGraph) -> float:
    """


    :param graph: DiGraph:
    :param bar: Bar:

    """
    value: float = degree_assortativity_coefficient(G=graph, x="out", y="in")
    return value


def computeAttributeAssortativityCoefficient(graph: DiGraph) -> float:
    """


    :param graph: DiGraph:
    :param bar: Bar:

    """
    value: float = attribute_assortativity_coefficient(
        G=graph,
        attribute="Operation_Type",
    )
    return value


def computeDegreePearsonCorrelationCoefficient(graph: DiGraph) -> float:
    """


    :param graph: DiGraph:
    :param bar: Bar:

    """
    value: float = degree_pearson_correlation_coefficient(
        G=graph,
        x="out",
        y="in",
    )
    return value


def checkIsSemiconnected(graph: DiGraph) -> int:
    """


    :param graph: DiGraph:
    :param bar: Bar:

    """
    value: int = int(is_semiconnected(G=graph))
    return value


def checkIsAttractingComponent(graph: DiGraph) -> int:
    """


    :param graph: DiGraph:
    :param bar: Bar:

    """
    value: int = int(is_attracting_component(G=graph))
    return value


def checkIsStronglyConnected(graph: DiGraph) -> int:
    """


    :param graph: DiGraph:
    :param bar: Bar:

    """
    value: int = int(is_strongly_connected(G=graph))
    return value


def checkIsWeaklyConnected(graph: DiGraph) -> int:
    """


    :param graph: DiGraph:
    :param bar: Bar:

    """
    value: int = int(is_weakly_connected(G=graph))
    return value


def computeNumberOfWeaklyConnectedComponents(graph: DiGraph) -> int:
    """


    :param graph: DiGraph:
    :param bar: Bar:

    """
    value: int = number_weakly_connected_components(G=graph)
    return value


def computeNumberOfStronglyConnectedComponents(graph: DiGraph) -> int:
    """


    :param graph: DiGraph:
    :param bar: Bar:

    """
    value: int = number_strongly_connected_components(G=graph)
    return value


def computeNumberOfAttractingComponents(graph: DiGraph) -> int:
    """


    :param graph: DiGraph:
    :param bar: Bar:

    """
    value: int = number_attracting_components(G=graph)
    return value


def _run(graph: DiGraph, id: int = 0) -> DataFrame:
    data: dict[str, int | float] = {"Model_ID": id}

    data["Barycenter"] = computeBarycenter(graph=graph)
    data["Radius"] = computeRadius(graph=graph)
    data["DAG Longest Path Length"] = computeDAGLongestPathLength(graph=graph)
    data["Average Shortest Path Length"] = computeAverageShortestPathLength(graph=graph)
    data["Number of Isolates"] = computeNumberOfIsolates(graph=graph)
    data["Is Threshold Graph"] = checkIsThresholdGraph(graph=graph)
    data["Diameter"] = computeDiameter(graph=graph)
    data[
        "Attribute Assortativity Coefficient"
    ] = computeAttributeAssortativityCoefficient(graph=graph)
    data[
        "Degree Pearson Correlation Coefficient"
    ] = computeDegreePearsonCorrelationCoefficient(graph=graph)
    data[
        "Number of Weakly Connected Components"
    ] = computeNumberOfWeaklyConnectedComponents(graph=graph)
    data[
        "Number of Strongly Connected Components"
    ] = computeNumberOfStronglyConnectedComponents(graph=graph)
    data["Number of Attracting Components"] = computeNumberOfAttractingComponents(
        graph=graph
    )
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

    df: DataFrame = DataFrame(data=[data])

    return df
