from concurrent.futures import ThreadPoolExecutor
from typing import List

from networkx import DiGraph, read_gexf
from networkx.classes.reportviews import NodeDataView, NodeView, OutEdgeView
from progress.bar import Bar


def _addNodesToSubgraph(
    subgraph: Digraph,
    headGraphNodes: NodeDataView | NodeView,
    subgraphNodes: List[str],
) -> None:
    node: str
    for node in subgraphNodes:
        subgraph.add_node(node, **headGraphNodes[node])

    return subgraph


def _addEdgesToSubgraph(
    subgraph: DiGraph,
    edgeData: OutEdgeView,
    subgraphNodes: List[str],
) -> DiGraph:
    u: str
    v: str
    edgeAttributes: dict

    for u, v, edgeAttributes in edgeData:
        if u in subgraphNodes and v in subgraphNodes:
            subgraph.add_edge(u, v, **edgeAttributes)

    return subgraph


def createSubgraph(
    headGraphNodes: NodeDataView | NodeView,
    headGraphEdgeData: OutEdgeView,
    subgraphNodes: List[str],
) -> DiGraph:
    subgraph: DiGraph = DiGraph()

    _addNodesToSubgraph(
        subgraph=subgraph,
        headGraphNodes=headGraphNodes,
        subgraphNodes=subgraphNodes,
    )
    _addEdgesToSubgraph(
        subgraph=subgraph,
        edgeData=headGraphEdgeData,
        subgraphNodes=subgraphNodes,
    )

    return subgraph


def main() -> None:
    subgraphList: List[DiGraph] = []

    graph: DiGraph = read_gexf("bert-base-cased.gexf")

    nodes: NodeDataView | NodeView = graph.nodes()
    edgeData: OutEdgeView = graph.edges.data()

    nodeList: List = list(nodes)

    with Bar("Computing all possible subgraphs... ", max=len(nodes)) as progress:
        tortiseNode: str
        hareNode: str

        for tortiseNode in nodes:
            foo: int = int(tortiseNode)

            for hareNode in nodes:
                bar: int = int(hareNode)

                if foo > bar:
                    continue

                subgraph: DiGraph = DiGraph()
                subgraphNodes: List[str] = nodeList[foo:bar]

                zoo: str
                for zoo in subgraphNodes:
                    subgraph.add_node(zoo, **nodes[zoo])

            progress.next()


if __name__ == "__main__":
    main()
