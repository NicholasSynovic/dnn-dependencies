from collections import Counter, deque
from functools import partial
from itertools import permutations, product
from multiprocessing.pool import Pool
from pprint import pprint as print
from typing import List

from networkx import DiGraph, read_gexf, subgraph
from networkx.algorithms.community import louvain_communities
from networkx.algorithms.isomorphism import DiGraphMatcher
from progress.bar import Bar
from progress.spinner import Spinner


def createGraphStack(
    graphList1: List[DiGraph], graphList2: List[DiGraph]
) -> List[tuple[DiGraph, DiGraph]]:
    """
    The function `createGraphStack` takes two lists of directed graphs and returns a list of tuples,
    where each tuple contains one graph from the first list and one graph from the second list.

    :param graphList1: A list of DiGraph objects
    :type graphList1: List1: List1: List[DiGraph]
    :param graphList2: graphList2 is a list of DiGraph objects
    :type graphList2: List2: List2: List[DiGraph]
    :param graphList1: List[DiGraph]:
    :param graphList2: List[DiGraph]:
    :param graphList1: List[DiGraph]:
    :param graphList2: List[DiGraph]:
    :returns: a list of tuples, where each tuple contains a pair of DiGraph objects from the input lists
    graphList1 and graphList2.

    """
    return list(product(graphList1, graphList2))


def compareCommunities(graph1: DiGraph, graph2: DiGraph) -> List[bool]:
    """
    The function `compareCommunities` compares the communities of two directed graphs using the Louvain
    algorithm and checks if the subgraphs within each community are isomorphic.

    :param graph1: The parameter `graph1` is a directed graph (DiGraph) representing the first graph
    :type graph1: DiGraph
    :param graph2: The `graph2` parameter is a directed graph (`DiGraph`) that represents a community
    structure. It is used to compare the community structure of `graph1` with `graph2`
    :type graph2: DiGraph
    :param graph1: DiGraph:
    :param graph2: DiGraph:
    :param graph1: DiGraph:
    :param graph2: DiGraph:
    :returns: The function `compareCommunities` returns a list of boolean values. Each boolean value
    represents whether the corresponding pair of communities in `graph1` and `graph2` are isomorphic
    (structurally identical) or not.

    """
    graph1_Communities: List[set[int]] = louvain_communities(graph1, seed=42)
    graph2_Communities: List[set[int]] = louvain_communities(graph2, seed=42)

    graph1_Subgraphs: List[DiGraph] = [
        subgraph(G=graph1, nbunch=community) for community in graph1_Communities
    ]
    graph2_Subgraphs: List[DiGraph] = [
        subgraph(G=graph2, nbunch=community) for community in graph2_Communities
    ]

    pairs: List[tuple[DiGraph, DiGraph]] = createGraphStack(
        graphList1=graph1_Subgraphs, graphList2=graph2_Subgraphs
    )
    matchers: List[DiGraphMatcher] = [DiGraphMatcher(G1=g1, G2=g2) for g1, g2 in pairs]

    results: List[bool] = []
    with Bar(
        "Calculating isomorphisms between graph communities... ", max=len(matchers)
    ) as bar:
        m: DiGraphMatcher
        for m in matchers:
            results.append(m.is_isomorphic())
            bar.next()

    return results


def compareGraphs(graph1: DiGraph, graph2: DiGraph) -> bool:
    """
    The function `compareGraphs` takes two directed graphs as input and returns a boolean value
    indicating whether the graphs are isomorphic.

    :param graph1: The parameter `graph1` is a directed graph (DiGraph) that represents the first graph
    to be compared
    :type graph1: DiGraph
    :param graph2: The parameter `graph2` is a directed graph (DiGraph) that you want to compare with
    `graph1`
    :type graph2: DiGraph
    :param graph1: DiGraph:
    :param graph2: DiGraph:
    :param graph1: DiGraph:
    :param graph2: DiGraph:
    :returns: a boolean value indicating whether the two input graphs, `graph1` and `graph2`, are
    isomorphic.

    """
    matcher: DiGraphMatcher = DiGraphMatcher(G1=graph1, G2=graph2)
    return matcher.is_isomorphic()


def main() -> None:
    """The main function reads a graph from a GEXF file and compares its communities to itself."""
    graph1: DiGraph = read_gexf("architecture.gexf")
    compareCommunities(graph1, graph1)


if __name__ == "__main__":
    main()
