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


def main() -> None:
    graph: DiGraph = read_gexf("bert-base-cased.gexf")

    with Bar("Computing metrics ({})... ", max=30) as bar:
        checkIsSemiconnected(graph=graph, bar=bar)
        checkIsAttractingComponent(graph=graph, bar=bar)
        sc: int = checkIsStronglyConnected(graph=graph, bar=bar)
        checkIsWeaklyConnected(graph=graph, bar=bar)
        checkIsTriad(graph=graph, bar=bar)
        checkIsRegular(graph=graph, bar=bar)
        checkIsPlanar(graph=graph, bar=bar)
        checkIsDistanceRegular(graph=graph, bar=bar)
        checkIsStronglyRegular(graph=graph, bar=bar)
        checkIsBipartite(graph=graph, bar=bar)
        checkIsAperiodic(graph=graph, bar=bar)
        checkIsDirectedAcyclicGraph(graph=graph, bar=bar)
        computeRadius(graph=graph, bar=bar)
        computeDAGLongestPathLength(graph=graph, bar=bar)
        computeNumberOfIsolates(graph=graph, bar=bar)
        computeRobinsAlexanderClustering(graph=graph, bar=bar)
        computeTransitivity(graph=graph, bar=bar)
        computeNumberOfNodes(graph=graph, bar=bar)
        computeDensity(graph=graph, bar=bar)
        computeNumberOfEdges(graph=graph, bar=bar)
        computeNumberOfCommunities(graph=graph, bar=bar)
        computeDegreeAssortativityCoefficient(graph=graph, bar=bar)
        computeAttributeAssortativityCoefficient(graph=graph, bar=bar)
        computeNumberOfWeaklyConnectedComponents(graph=graph, bar=bar)
        computeNumberOfStronglyConnectedComponents(graph=graph, bar=bar)
        computeNumberOfAttracingComponents(graph=graph, bar=bar)
        computeBarycenter(graph=graph, bar=bar)

        if sc == 1:
            computeAverageShortestPathLength(graph=graph, bar=bar)
            computeDiameter(graph=graph, bar=bar)
        else:
            bar.next(n=2)

        computeDegreePearsonCorrelationCoefficient(graph=graph, bar=bar)


if __name__ == "__main__":
    main()
