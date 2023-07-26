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
from networkx.exception import NetworkXNoPath
from progress.bar import Bar

RANDOM_SEED: int = 42

random.seed(a=RANDOM_SEED, version=2)
numpy.random.seed(seed=RANDOM_SEED)


def computeBarycenter(graph: DiGraph, bar: Bar) -> int:
    """


    :param graph: DiGraph:
    :param bar: Bar:

    """
    try:
        value: int = len(barycenter(G=graph))
    except NetworkXNoPath:
        value: int = -1
    bar.next()
    return value


def computeRadius(graph: DiGraph, bar: Bar) -> int:
    """


    :param graph: DiGraph:
    :param bar: Bar:

    """
    try:
        value: int = radius(G=graph)
    except NetworkXError:
        value: int = -1
    bar.next()
    return value


def computeDAGLongestPathLength(graph: DiGraph, bar: Bar) -> int:
    """


    :param graph: DiGraph:
    :param bar: Bar:

    """
    value: int = dag_longest_path_length(G=graph)
    bar.next()
    return value


def computeAverageShortestPathLength(graph: DiGraph, bar: Bar) -> float:
    """


    :param graph: DiGraph:
    :param bar: Bar:

    """
    value: float = average_shortest_path_length(G=graph)
    bar.next()
    return value


def computeNumberOfIsolates(graph: DiGraph, bar: Bar) -> int:
    """


    :param graph: DiGraph:
    :param bar: Bar:

    """
    value: int = number_of_isolates(G=graph)
    bar.next()
    return value


def checkIsTriad(graph: DiGraph, bar: Bar) -> int:
    """


    :param graph: DiGraph:
    :param bar: Bar:

    """
    value: int = int(is_triad(G=graph))
    bar.next()
    return value


def checkIsThresholdGraph(graph: DiGraph, bar: Bar) -> int:
    """


    :param graph: DiGraph:
    :param bar: Bar:

    """
    value: int = int(is_threshold_graph(G=graph))
    bar.next()
    return value


def checkIsRegular(graph: DiGraph, bar: Bar) -> int:
    """


    :param graph: DiGraph:
    :param bar: Bar:

    """
    value: int = int(is_regular(G=graph))
    bar.next()
    return value


def checkIsPlanar(graph: DiGraph, bar: Bar) -> int:
    """


    :param graph: DiGraph:
    :param bar: Bar:

    """
    value: int = int(is_planar(G=graph))
    bar.next()
    return value


def checkIsDistanceRegular(graph: DiGraph, bar: Bar) -> int:
    """


    :param graph: DiGraph:
    :param bar: Bar:

    """
    value: int = int(is_distance_regular(G=graph))
    bar.next()
    return value


def checkIsStronglyRegular(graph: DiGraph, bar: Bar) -> int:
    """


    :param graph: DiGraph:
    :param bar: Bar:

    """
    value: int = int(is_strongly_regular(G=graph))
    bar.next()
    return value


def checkIsBipartite(graph: DiGraph, bar: Bar) -> int:
    """


    :param graph: DiGraph:
    :param bar: Bar:

    """
    value: int = int(is_bipartite(G=graph))
    bar.next()
    return value


def computeRobinsAlexanderClustering(graph: DiGraph, bar: Bar) -> float | Literal[0]:
    """


    :param graph: DiGraph:
    :param bar: Bar:

    """
    value: float | Literal[0] = robins_alexander_clustering(G=graph)
    bar.next()
    return value


def computeTransitivity(graph: DiGraph, bar: Bar) -> float | Literal[0]:
    """


    :param graph: DiGraph:
    :param bar: Bar:

    """
    value: float | Literal[0] = transitivity(G=graph)
    bar.next()
    return value


def checkIsAperiodic(graph: DiGraph, bar: Bar) -> int:
    """


    :param graph: DiGraph:
    :param bar: Bar:

    """
    value: int = int(is_aperiodic(G=graph))
    bar.next()
    return value


def checkIsDirectedAcyclicGraph(graph: DiGraph, bar: Bar) -> int:
    """


    :param graph: DiGraph:
    :param bar: Bar:

    """
    value: int = int(is_directed_acyclic_graph(G=graph))
    bar.next()
    return value


def computeNumberOfNodes(graph: DiGraph, bar: Bar) -> int:
    """


    :param graph: DiGraph:
    :param bar: Bar:

    """
    value: int = graph.number_of_nodes()
    bar.next()
    return value


def computeDensity(graph: DiGraph, bar: Bar) -> float:
    """


    :param graph: DiGraph:
    :param bar: Bar:

    """
    value: int = density(G=graph)
    bar.next()
    return value


def computeNumberOfEdges(graph: DiGraph, bar: Bar) -> int:
    """


    :param graph: DiGraph:
    :param bar: Bar:

    """
    value: int = graph.number_of_edges()
    bar.next()
    return value


def computeNumberOfCommunities(graph: DiGraph, bar: Bar) -> int:
    """


    :param graph: DiGraph:
    :param bar: Bar:

    """
    communities: List[Set[str]] = louvain_communities(graph, seed=42)
    value: int = len(communities)
    bar.next()
    return value


def computeDiameter(graph: DiGraph, bar: Bar) -> int:
    """


    :param graph: DiGraph:
    :param bar: Bar:

    """
    value: int = diameter(G=graph)
    bar.next()
    return value


def computeDegreeAssortativityCoefficient(graph: DiGraph, bar: Bar) -> float:
    """


    :param graph: DiGraph:
    :param bar: Bar:

    """
    value: float = degree_assortativity_coefficient(G=graph, x="out", y="in")
    bar.next()
    return value


def computeAttributeAssortativityCoefficient(graph: DiGraph, bar: Bar) -> float:
    """


    :param graph: DiGraph:
    :param bar: Bar:

    """
    value: float = attribute_assortativity_coefficient(
        G=graph,
        attribute="Operation_Type",
    )
    bar.next()
    return value


def computeDegreePearsonCorrelationCoefficient(graph: DiGraph, bar: Bar) -> float:
    """


    :param graph: DiGraph:
    :param bar: Bar:

    """
    value: float = degree_pearson_correlation_coefficient(
        G=graph,
        x="out",
        y="in",
    )
    bar.next()
    return value


def checkIsSemiconnected(graph: DiGraph, bar: Bar) -> int:
    """


    :param graph: DiGraph:
    :param bar: Bar:

    """
    value: int = int(is_semiconnected(G=graph))
    bar.next()
    return value


def checkIsAttractingComponent(graph: DiGraph, bar: Bar) -> int:
    """


    :param graph: DiGraph:
    :param bar: Bar:

    """
    value: int = int(is_attracting_component(G=graph))
    bar.next()
    return value


def checkIsStronglyConnected(graph: DiGraph, bar: Bar) -> int:
    """


    :param graph: DiGraph:
    :param bar: Bar:

    """
    value: int = int(is_strongly_connected(G=graph))
    bar.next()
    return value


def checkIsWeaklyConnected(graph: DiGraph, bar: Bar) -> int:
    """


    :param graph: DiGraph:
    :param bar: Bar:

    """
    value: int = int(is_weakly_connected(G=graph))
    bar.next()
    return value


def computeNumberOfWeaklyConnectedComponents(graph: DiGraph, bar: Bar) -> int:
    """


    :param graph: DiGraph:
    :param bar: Bar:

    """
    value: int = number_weakly_connected_components(G=graph)
    bar.next()
    return value


def computeNumberOfStronglyConnectedComponents(graph: DiGraph, bar: Bar) -> int:
    """


    :param graph: DiGraph:
    :param bar: Bar:

    """
    value: int = number_strongly_connected_components(G=graph)
    bar.next()
    return value


def computeNumberOfAttracingComponents(graph: DiGraph, bar: Bar) -> int:
    """


    :param graph: DiGraph:
    :param bar: Bar:

    """
    value: int = number_attracting_components(G=graph)
    bar.next()
    return value
