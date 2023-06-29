from typing import List

from networkx import DiGraph, read_gexf
from networkx.classes.reportviews import NodeDataView, NodeView
from progress.bar import Bar


def addNodesToSubgraph(
    headGraphNodes: NodeDataView | NodeView, subgraphNodes: List[str]
) -> DiGraph:
    subgraph: DiGraph = DiGraph()

    node: str
    for node in subgraphNodes:
        subgraph.add_node(node, **headGraphNodes[node])

    return subgraph


def main() -> None:
    subgraphList: List[DiGraph] = []

    graph: DiGraph = read_gexf("bert-base-cased.gexf")

    nodes: NodeDataView | NodeView = graph.nodes()
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
