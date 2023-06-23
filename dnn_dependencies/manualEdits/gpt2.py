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
            startNode: str = data[key][0]
            endNode: str = data[key][-1]

            parents: List[str] = list(graph.predecessors(n=startNode))
            children: List[str] = list(graph.successors(n=endNode))

            parentEdges: List[tuple[str, str]] = [
                (parent, condensedLayerNodeLabel) for parent in parents
            ]
            childrenEdges: List[tuple[str, str]] = [
                (child, condensedLayerNodeLabel) for child in children
            ]

            graph.add_node(node_for_adding=condensedLayerNodeLabel)

            graph.add_edges_from(ebunch_to_add=parentEdges)
            graph.add_edges_from(ebunch_to_add=childrenEdges)

            progress.next()

    write_gexf(graph, "gpt2_large-layers.gexf")


if __name__ == "__main__":
    main()
