from typing import List, Set

import networkx as nx
from networkx import DiGraph, density, read_gexf
from networkx.algorithms import bipartite
from networkx.algorithms.community import louvain_communities
from networkx.algorithms.threshold import is_threshold_graph
from progress.bar import Bar


def barycenter(G: DiGraph, bar: Bar):
    result = nx.barycenter(G)
    bar.next()
    return result


def radius(G: DiGraph, bar: Bar) -> any:
    result = nx.radius(G)
    bar.next()
    return result


def longestPathLength(G: DiGraph, bar: Bar) -> int:
    result = nx.dag_longest_path_length(G)
    bar.next()
    return result


# graph is not strongly connected
def shortestPathLength(G: DiGraph, bar: Bar):
    result = nx.average_shortest_path_length(G)
    bar.next()
    return result


def numberOfIsolates(G: DiGraph, bar: Bar) -> int:
    result = nx.number_of_isolates(G)
    bar.next()
    return result


def isTriad(G: DiGraph, bar: Bar) -> bool:
    result = nx.is_triad(G)
    bar.next()
    return result


def isThresholdGraph(G: DiGraph, bar: Bar) -> bool:
    result = is_threshold_graph(G)
    bar.next()
    return result


def isRegular(G: DiGraph, bar: Bar) -> bool:
    result = nx.is_regular(G)
    bar.next()
    return result


def isPlanar(G: DiGraph, bar: Bar) -> bool:
    result = nx.is_planar(G)
    bar.next()
    return result


def isDistanceRegular(G: DiGraph, bar: Bar) -> bool:
    result = nx.is_distance_regular(G)
    bar.next()
    return result


def isStronglyRegular(G: DiGraph, bar: Bar) -> bool:
    result = nx.is_strongly_regular(G)
    bar.next()
    return result


def averageClustering(G: DiGraph, bar: Bar) -> float:
    result = nx.average_clustering(G)
    bar.next()
    return result


def isBapartite(G: DiGraph, bar: Bar) -> bool:
    result = nx.is_bipartite(G)
    bar.next()
    return result


def robinsAlexanderClustering(G: DiGraph, bar: Bar) -> float:
    result = bipartite.robins_alexander_clustering(G)
    bar.next()
    return result


def transitivity(G: DiGraph, bar: Bar) -> float:
    result = nx.transitivity(G)
    bar.next()
    return result


# not strongly connected
def travelingSalesmanProbSolnSize(G: DiGraph, bar: Bar) -> int:
    answer = nx.approximation.traveling_salesman_problem(G)
    result = answer.__sizeof__
    bar.next()
    return result


def isAperiodic(G: DiGraph, bar: Bar) -> bool:
    result = nx.is_aperiodic(G)
    bar.next()
    return result


def isDAG(G: DiGraph, bar: Bar) -> bool:
    result = nx.is_directed_acyclic_graph(G)
    bar.next()
    return result


def countNodes(graph: DiGraph) -> int:
    """
    The function countNodes takes a directed graph as input and returns the number of nodes in the
    graph.

    :param graph: The parameter `graph` is of type `DiGraph`, which suggests that it is a directed graph
    :type graph: DiGraph
    :return: the number of nodes in the given graph.
    """
    return graph.number_of_nodes()


def computeDensity(graph: DiGraph) -> float:
    """
    The function `computeDensity` calculates the density of a directed graph.

    :param graph: The parameter `graph` is expected to be a directed graph (DiGraph) object
    :type graph: DiGraph
    :return: a float value, which represents the density of the given directed graph.
    """
    return density(G=graph)


def countEdges(graph: DiGraph) -> int:
    """
    The function countEdges takes a directed graph as input and returns the number of edges in the
    graph.

    :param graph: The parameter `graph` is expected to be an instance of a directed graph (DiGraph)
    :type graph: DiGraph
    :return: the number of edges in the given directed graph.
    """
    return graph.size()


def countCommunities(graph: DiGraph) -> int:
    """
    The function `countCommunities` takes a directed graph as input and returns the number of
    communities detected using the Louvain algorithm.

    :param graph: The `graph` parameter is a directed graph object. It represents a network or a set of
    connections between nodes. The graph can be represented using a data structure such as an adjacency
    matrix or an adjacency list
    :type graph: DiGraph
    :return: the number of communities detected in the given graph.
    """
    communities: List[Set[str]] = louvain_communities(graph, seed=42)
    return len(communities)


def main() -> None:
    G: DiGraph = read_gexf("gpt2.gexf")
    with Bar("Calculating metrics") as bar:
        print("\n", barycenter(G, bar))
        print("\n", radius(G, bar))
        print("\n", longestPathLength(G, bar))
        print("\n", shortestPathLength(G, bar))
        print("\n", numberOfIsolates(G, bar))
        print("\n", isTriad(G, bar))
        print("\n", isThresholdGraph(G, bar))
        print("\n", isRegular(G, bar))
        print("\n", isPlanar(G, bar))
        print("\n", isDistanceRegular(G, bar))
        print("\n", isStronglyRegular(G, bar))
        print("\n", averageClustering(G, bar))
        print("\n", robinsAlexanderClustering(G, bar))
        print("\n", transitivity(G, bar))
        print("\n", travelingSalesmanProbSolnSize(G, bar))
        print("\n", isAperiodic(G, bar))
        print("\n", isDAG(G, bar))


main()
