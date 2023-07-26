from argparse import Namespace
from collections import defaultdict
from json import dump
from typing import Any, List, Set

from networkx import DiGraph, clustering, density, node_attribute_xy, read_gexf
from networkx.algorithms.community import louvain_communities
from networkx.classes.reportviews import NodeView
from progress.bar import Bar

from dnn_dependencies.args.similarity_args import getArgs


def _sortDict(d: defaultdict | dict[Any, Any]) -> dict[Any, Any]:
    """
    The function `_sortDict` takes a dictionary or defaultdict as input, creates a copy of it, sorts the
    copy by keys, and returns the sorted dictionary.

    :param d: The parameter `d` is expected to be either a `defaultdict` or a regular `dict` with keys
    and values of any type
    :type d: defaultdict | dict[Any, Any]
    :param d: defaultdict | dict[Any:
    :param Any: returns: The function `_sortDict` returns a sorted dictionary.
    :param d: defaultdict | dict[Any:
    :param Any]:
    :returns: The function `_sortDict` returns a sorted dictionary.

    """
    foo: dict[Any, Any] = dict(d)
    bar: dict[Any, Any] = dict(sorted(foo.items()))

    return bar


def computeDensity(graph: DiGraph) -> float:
    """
    The function `computeDensity` calculates the density of a directed graph.

    :param graph: The parameter `graph` is expected to be a directed graph (DiGraph) object
    :type graph: DiGraph
    :param graph: DiGraph:
    :param graph: DiGraph:
    :returns: a float value, which represents the density of the given directed graph.

    """
    return density(G=graph)


def countNodes(graph: DiGraph) -> int:
    """
    The function countNodes takes a directed graph as input and returns the number of nodes in the
    graph.

    :param graph: The parameter `graph` is of type `DiGraph`, which suggests that it is a directed graph
    :type graph: DiGraph
    :param graph: DiGraph:
    :param graph: DiGraph:
    :returns: the number of nodes in the given graph.

    """
    return graph.number_of_nodes()


def countEdges(graph: DiGraph) -> int:
    """
    The function countEdges takes a directed graph as input and returns the number of edges in the
    graph.

    :param graph: The parameter `graph` is expected to be an instance of a directed graph (DiGraph)
    :type graph: DiGraph
    :param graph: DiGraph:
    :param graph: DiGraph:
    :returns: the number of edges in the given directed graph.

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
    :param graph: DiGraph:
    :param graph: DiGraph:
    :returns: the number of communities detected in the given graph.

    """
    communities: List[Set[str]] = louvain_communities(graph, seed=42)
    return len(communities)


def computeDegreeDistribution(graph: DiGraph, inDegree: bool = True) -> dict[int, int]:
    """
    The `computeDegreeDistribution` function computes the degree distribution of nodes in a directed
    graph, either in-degree or out-degree, and returns the result as a dictionary.

    :param graph: The `graph` parameter is a directed graph object of type `DiGraph`. It represents a
    graph with nodes and edges, where each edge has a direction
    :type graph: DiGraph
    :param inDegree: The `inDegree` parameter is a boolean flag that determines whether to compute the
    in-degree distribution or the out-degree distribution of the nodes in the graph. If `inDegree` is
    `True`, the function will compute the in-degree distribution. If `inDegree` is `False`, the
    function, defaults to True
    :type inDegree: bool (optional)
    :param graph: DiGraph:
    :param inDegree: bool:  (Default value = True)
    :param graph: DiGraph:
    :param inDegree: bool:  (Default value = True)
    :returns: a dictionary that represents the degree distribution of nodes in the graph. The keys of the
    dictionary are the degrees of the nodes, and the values are the number of nodes with that degree.

    """
    data: defaultdict = defaultdict(int)

    def _iterateInDegree(nodes: NodeView, bar: Bar) -> None:
        """
        The function `_iterateInDegree` iterates over nodes in a graph, calculates the in-degree of each
        node, and updates a dictionary with the count of each in-degree value.

        :param nodes: The `nodes` parameter is a `NodeView` object, which represents a view of the nodes
        in a graph. It allows you to iterate over the nodes in the graph
        :type nodes: NodeView
        :param bar: The parameter "bar" is of type "Bar". It is likely used to track the progress of the
        iteration
        :type bar: Bar
        :param nodes: NodeView:
        :param bar: Bar:
        :param nodes: NodeView:
        :param bar: Bar:

        """
        node: str
        for node in nodes:
            degree: int = graph.in_degree(node)
            data[degree] += 1
            bar.next()

    def _iterateOutDegree(nodes: NodeView, bar: Bar) -> None:
        """
        The function `_iterateOutDegree` iterates over a collection of nodes, calculates the out-degree
        of each node in a graph, and updates a dictionary with the count of each out-degree.

        :param nodes: The `nodes` parameter is a `NodeView` object, which represents a view of the nodes
        in a graph. It allows you to iterate over the nodes in the graph
        :type nodes: NodeView
        :param bar: The "bar" parameter is an instance of the "Bar" class. It is used to track the
        progress of the iteration
        :type bar: Bar
        :param nodes: NodeView:
        :param bar: Bar:
        :param nodes: NodeView:
        :param bar: Bar:

        """
        node: str
        for node in nodes:
            degree: int = graph.out_degree(node)
            data[degree] += 1
            bar.next()

    degreeType: str = "in" if inDegree else "out"
    nodes: NodeView = graph.nodes()

    with Bar(
        f"Computing the {degreeType}-degree distribution of nodes... ", max=len(nodes)
    ) as progress:
        if inDegree:
            _iterateInDegree(nodes=nodes, bar=progress)
        else:
            _iterateOutDegree(nodes=nodes, bar=progress)

    return _sortDict(d=data)


def computeClusteringCoefficientDistribution(graph: DiGraph) -> dict[int, int]:
    """
    The function `computeClusteringCoefficientDistribution` computes the clustering coefficient
    distribution of nodes in a directed graph.

    :param graph: The parameter `graph` is a directed graph (DiGraph) object. It represents a network or
    a graph where the nodes are connected by directed edges
    :type graph: DiGraph
    :param graph: DiGraph:
    :param graph: DiGraph:
    :returns: a dictionary that represents the clustering coefficient distribution of nodes in the given
    graph. The keys of the dictionary are the clustering coefficients, and the values are the
    frequencies of those coefficients in the graph.

    """
    data: defaultdict = defaultdict(int)

    nodes: NodeView = graph.nodes()

    with Bar(
        f"Computing the clustering coefficient distribution of nodes... ",
        max=len(nodes),
    ) as progress:
        node: str
        for node in nodes:
            coefficient: int | float = clustering(G=graph, nodes=node)
            data[coefficient] += 1
            progress.next()

    return _sortDict(d=data)


def computeNodeTypeDistribution(graph: DiGraph) -> dict[str, int]:
    """
    The function `computeNodeTypeDistribution` takes a directed graph as input and computes the
    distribution of node operation types, returning a dictionary with the count of each operation type.

    :param graph: A directed graph (DiGraph) representing a network or system. Each node in the graph
    has an associated "Operation Type" attribute, which indicates the type of operation performed by
    that node
    :type graph: DiGraph
    :param graph: DiGraph:
    :param graph: DiGraph:
    :returns: a dictionary that represents the distribution of node operation types in the given graph.
    The keys of the dictionary are the operation types, and the values are the counts of nodes with each
    operation type.

    """
    data: defaultdict = defaultdict(int)

    nodes: NodeView = graph.nodes(data="Operation_Type")

    with Bar(
        "Computing the distribution of node operations types... ", max=len(nodes)
    ) as progress:
        opType: str
        for _, opType in nodes:
            data[opType] += 1
            progress.next()

    return _sortDict(d=data)


def computeNodeTypePairingDistribution(graph: DiGraph) -> dict[str, int]:
    """


    :param graph: DiGraph:
    :param graph: DiGraph:

    """
    data: defaultdict = defaultdict(int)

    nodeAttributePairs: List[tuple[str, str]] = list(
        node_attribute_xy(G=graph, attribute="Operation_Type")
    )

    with Bar(
        "Computing the distribution of node operations types... ",
        max=len(nodeAttributePairs),
    ) as progress:
        pair: tuple[str, str]
        for pair in nodeAttributePairs:
            key: str = f"{pair[0]}, {pair[1]}"
            data[key] += 1
            progress.next()

    return _sortDict(d=data)


def createJSON(graph: DiGraph) -> dict[str, Any]:
    """
    The function `createJSON` takes a directed graph as input and returns a dictionary containing
    various statistics and distributions computed from the graph.

    :param graph: The `graph` parameter is of type `DiGraph`, which represents a directed graph. It is
    used as input to compute various properties of the graph, such as density, node count, edge count,
    community count, degree distribution, clustering coefficient distribution, and node type
    distribution
    :type graph: DiGraph
    :param graph: DiGraph:
    :param graph: DiGraph:
    :returns: The function `createJSON` returns a dictionary containing various metrics and distributions
    computed from the input graph.

    """
    data: dict[str, Any] = {}

    data["Graph Density"] = computeDensity(graph=graph)
    data["Node Count"] = countNodes(graph=graph)
    data["Edge Count"] = countEdges(graph=graph)
    data["Community Count"] = countCommunities(graph=graph)

    inDegreeDistribution: dict[int, int] = computeDegreeDistribution(
        graph=graph,
        inDegree=True,
    )

    outDegreeDistribution: dict[int, int] = computeDegreeDistribution(
        graph=graph,
        inDegree=False,
    )

    clusteringCoefficientDistribution: dict[
        int, int
    ] = computeClusteringCoefficientDistribution(graph=graph)

    nodeTypeDistribution: dict[str, int] = computeNodeTypeDistribution(graph=graph)

    nodeTypePairingDistribution: dict[str, int] = computeNodeTypePairingDistribution(
        graph=graph
    )

    data["In Degree Distribution"] = inDegreeDistribution
    data["Out Degree Distribution"] = outDegreeDistribution
    data["Clustering Coefficient Distribution"] = clusteringCoefficientDistribution
    data["Node Distribution"] = nodeTypeDistribution
    data["Node Pairing Distribution"] = nodeTypePairingDistribution

    return _sortDict(d=data)


def main() -> None:
    """
    The main function reads a graph from a GEXF file, creates a JSON representation of the graph, and
    writes it to an output file.


    """
    args: Namespace = getArgs()

    graph: DiGraph = read_gexf(args.input[0])

    computeNodeTypePairingDistribution(graph=graph)

    json: dict[str, Any] = createJSON(graph=graph)

    with open(args.output[0], "w") as jsonFile:
        dump(obj=json, fp=jsonFile, indent=4)
        jsonFile.close()


if __name__ == "__main__":
    main()
