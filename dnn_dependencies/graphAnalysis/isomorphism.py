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
    return list(product(graphList1, graphList2))


def compareCommunities(graph1: DiGraph, graph2: DiGraph) -> List[bool]:
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


def main() -> None:
    graph1: DiGraph = read_gexf("architecture.gexf")
    compareCommunities(graph1, graph1)


if __name__ == "__main__":
    main()
