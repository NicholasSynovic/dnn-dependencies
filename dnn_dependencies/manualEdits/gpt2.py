from collections import defaultdict
from re import Match, search
from typing import List

from networkx import DiGraph, read_gexf, write_gexf
from networkx.classes.reportviews import NodeView
from progress.bar import Bar


def findRelevantNodes(
    graph: DiGraph, pattern: str, attribute: str = "label"
) -> defaultdict[str, List[str]]:
    data: defaultdict = defaultdict(list)

    nodes: NodeView = graph.nodes(data=attribute)

    with Bar(
        f"Finding all relevant nodes (matching regex pattern {pattern})... ",
        max=len(nodes),
    ) as progress:
        node: tuple[str, str]
        for node in nodes:
            idx: str = node[0]
            label: str = node[1]

            match: Match = search(pattern=pattern, string=label)
            if match:
                data[match.group(0)].append(idx)

            progress.next()

    return data


def main() -> None:
    pattern: str = r"h\.(\d+)"

    graph: DiGraph = read_gexf("gpt2.gexf")

    definedLayerNodes: defaultdict[str, List[str]] = findRelevantNodes(
        graph=graph, pattern=pattern
    )

    dataKeys: List[str] = list(definedLayerNodes.keys())

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

    rootNodes: defaultdict = defaultdict(list)

    nodes: NodeView = graph.nodes(data="label")
    with Bar("Identifying smaller layers... ", max=len(nodes)) as progress:
        node: tuple[str, str]
        for node in nodes:
            idx: str = node[0]
            label: str = node[1]

            if idx.__contains__("layer"):
                progress.next()
                continue

            try:
                label.index("/")
            except ValueError:
                progress.next()
                continue

            splitLabel: List[str] = label.split("/")[1::]

            if len(splitLabel) == 1:
                progress.next()
                continue

            rootNodes[splitLabel[0]].append(idx)
            progress.next()

    dataKeys: List[str] = list(rootNodes.keys())

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
