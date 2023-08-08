from collections import defaultdict
from typing import Generator, List, Tuple

from networkx import DiGraph
from networkx.classes.graph import NodeView
from pandas import DataFrame


def extractNodeChildren(graph: DiGraph) -> List[Tuple[str, Generator]]:
    nodePairs: List[Tuple[str, Generator]] = []
    nodes: NodeView = graph.nodes

    node: str
    for node in nodes:
        children: Generator = graph.successors(n=node)
        nodePairs.append((node, children))
    return nodePairs


def generateHistogramOfNodePairs(
    graph: DiGraph,
    pairs: List[Tuple[str, Generator]],
    modelID: int,
) -> defaultdict[str, int]:
    data: defaultdict[str, int] = defaultdict(int)

    data["Model_ID"] = modelID

    nodes: NodeView = graph.nodes

    pair: Tuple[str, Generator]
    for pair in pairs:
        parentID: str = pair[0]
        childrenIDs: Generator = pair[1]

        parentLabel: str = nodes[parentID]["label"]
        parentLabel: str = parentLabel.rsplit("/", 1)[-1].split("_", 1)[0]

        childrenLabels: List[str] = [nodes[childID]["label"] for childID in childrenIDs]
        childrenLabels: List[str] = [
            childLabel.rsplit("/", 1)[-1].split("_", 1)[0]
            for childLabel in childrenLabels
        ]

        childLabel: str
        for childLabel in childrenLabels:
            data[str((parentLabel, childLabel))] += 1

    return data


def _run(graph: DiGraph, id: int = 0) -> DataFrame:
    nodeChildren: List[Tuple[str, Generator]] = extractNodeChildren(graph=graph)
    histogram: defaultdict[str, int] = generateHistogramOfNodePairs(
        graph=graph,
        pairs=nodeChildren,
        modelID=id,
    )

    df: DataFrame = DataFrame().from_dict(data=histogram, orient="index")
    df.reset_index(inplace=True)
    df.columns = ["Node Type Pairs", "Count"]
    df.sort_values(by="Count", inplace=True, ignore_index=True)

    return df


if __name__ == "__main__":
    main()
