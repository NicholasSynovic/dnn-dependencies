from collections import defaultdict
from pprint import pprint as print
from re import Match, search
from typing import List

from networkx import DiGraph, read_gexf, write_gexf
from networkx.classes.reportviews import NodeView
from progress.bar import Bar


def main() -> None:
    data: defaultdict = defaultdict(list)
    pattern: str = r"h\.(\d+)"

    graph: DiGraph = read_gexf("gpt2.gexf")

    nodes: NodeView = graph.nodes(data="label")

    with Bar(
        "Finding all nodes within defined layers of the graph... ", max=len(nodes)
    ) as progress:
        node: tuple[str, str]
        for node in nodes:
            idx: str = node[0]
            label: str = node[1]

            match: Match = search(pattern=pattern, string=label)
            if match:
                data[match.group(1)].append(idx)

            progress.next()

    dataKeys: List[str] = list(data.keys())

    with Bar("Condensing layers... ", max=len(dataKeys)) as progress:
        key: str
        for key in dataKeys:
            condensedLayerNodeLabel: str = f"layer_{key}"
            graph.add_node(node_for_adding=condensedLayerNodeLabel)

            node: str
            for node in data[key]:
                nodeParentEdges: List[str] = list(graph.predecessors(n=node))
                nodeChildEdges: List[str] = list(graph.successors(n=node))

                layerNodeParentEdges: List[tuple[str, str]] = [
                    (edge, condensedLayerNodeLabel) for edge in nodeParentEdges
                ]
                layerNodeChildEdges: List[tuple[str, str]] = [
                    (edge, condensedLayerNodeLabel) for edge in nodeChildEdges
                ]

                graph.add_edges_from(ebunch_to_add=layerNodeParentEdges)
                graph.add_edges_from(ebunch_to_add=layerNodeChildEdges)

            graph.remove_nodes_from(nodes=data[key])

            progress.next()

    write_gexf(graph, "gpt2_large-layers.gexf")


if __name__ == "__main__":
    main()
