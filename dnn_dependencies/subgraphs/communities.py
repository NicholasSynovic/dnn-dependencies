import os
from typing import List

import networkx as nx
from networkx import DiGraph, read_gexf
from networkx.algorithms.community import louvain_communities


def getCommunities(graph: DiGraph) -> List[set[int]]:
    communitySubgraphs: List[nx.Graph] = []
    communities: List[set[int]] = louvain_communities(graph, seed=None)

    for community in communities:
        subgraph = graph.subgraph(community).copy()
        communitySubgraphs.append(subgraph)

    return communitySubgraphs


def createSubgraphs(graph: DiGraph, communities: List[set[int]]):
    folderPath = "/Users/karolinaryzka/Documents/dnn-dependencies/dnn_dependencies/subgraphs/gpt2"
    for i, community in enumerate(communities):
        filePath = os.path.join(folderPath, f"{i}.gexf")
        nx.write_gexf(community, filePath)


def getOperators(folderPath: str) -> List[str]:
    for communitySubgraph in os.listdir(folderPath):
        filePath = os.path.join(folderPath, communitySubgraph)
        subgraph: DiGraph = read_gexf(filePath)
        nodeOperations: List[str] = subgraph.nodes(data="type")

    return nodeOperations


# creating a list of subgraph.gexf files
# reading .gexf files into digraphs
# creating dictionary from subgraph


def getDictionaries() -> dict:
    folderPath1 = "/Users/karolinaryzka/Documents/dnn-dependencies/dnn_dependencies/subgraphs/bert-base-cased"
    folderPath2 = "/Users/karolinaryzka/Documents/dnn-dependencies/dnn_dependencies/subgraphs/gpt2"

    model1Subgraphs = {}
    model2Subgraphs = {}

    for communitySubgraph in os.listdir(folderPath1):
        filePath = os.path.join(folderPath1, communitySubgraph)
        subgraph: DiGraph = read_gexf(filePath)
        nodeOperations: List[str] = subgraph.nodes(data="type")
        key = communitySubgraph.replace(".gexf", "")
        model1Subgraphs[key] = nodeOperations
    print(model1Subgraphs)

    for communitySubgraph in os.listdir(folderPath2):
        filePath = os.path.join(folderPath2, communitySubgraph)
        subgraph: DiGraph = read_gexf(filePath)
        nodeOperations: List[str] = subgraph.nodes(data="type")
        key = communitySubgraph.replace(".gexf", "")
        model2Subgraphs[key] = nodeOperations
    print(model2Subgraphs)

    return model1Subgraphs, model2Subgraphs


def compareDicts(model1Subgraphs: dict, model2Subgraphs: dict):
    # match = [key for key in model1Subgraphs if key in model2Subgraphs and model1Subgraphs[key] == model2Subgraphs[key]]
    match = [
        key
        for key in model1Subgraphs
        if key in model2Subgraphs
        and set(model1Subgraphs[key]) == set(model2Subgraphs[key])
    ]
    return match


def main() -> None:
    # graph: DiGraph = read_gexf("gpt2.gexf")
    # communities = getCommunities(graph)
    # createSubgraphs(graph, communities)
    model1Subgraphs, model2Subgraphs = getDictionaries()
    matches = compareDicts(**model1Subgraphs, **model2Subgraphs)
    print("keys with matching values: ", matches)


main()
