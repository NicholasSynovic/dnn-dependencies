from argparse import Namespace
from itertools import count
from pathlib import Path
from typing import List

import pandas
from lxml import etree
from onnx import load
from onnx.onnx_pb import GraphProto, ModelProto, NodeProto
from pandas import DataFrame, Series
from progress.bar import Bar

from dnn_dependencies.args.architectureArgs import getArgs

NODE_ID_COUNTER: count = count()
EDGE_ID_COUNTER: count = count()
OUTPUT_DF_LIST: List[DataFrame] = []


def buildDF(nodeID: int, name: str, inputs: List[str], outputs: List[str]) -> DataFrame:
    data: dict[str, List[int | str | List[str]]] = {
        "ID": [nodeID],
        "Name": [name],
        "Inputs": [inputs],
        "Outputs": [outputs],
    }
    return DataFrame(data)


def dfIDQuery(df: DataFrame, query: str) -> tuple[str, str] | None:
    mask = df["Outputs"].apply(lambda x: query in x)
    tempDF: DataFrame = df[mask]

    try:
        return (tempDF["Name"].iloc[0], str(tempDF["ID"].iloc[0]))
    except IndexError:
        return None


def buildXML(
    df: DataFrame,
    outputPath: Path | List[Path],
    mode: str = "production",
) -> None:
    edgeList: List[tuple[tuple[str, str], str]] = []

    xmlns: str
    version: str
    if mode == "production":
        xmlns = "http://www.gexf.net/1.2draft"
        version = "1.2draft"
    else:
        xmlns = "http://www.gexf.net/1.2"
        version = "1.2"

    rootNode = etree.Element("gexf")
    rootNode.set("xmlns", xmlns)
    rootNode.set("version", version)

    graphNode = etree.SubElement(rootNode, "graph")
    graphNode.set("mode", "static")
    graphNode.set("defaultedgetype", "directed")
    graphNode.set("idtype", "integer")

    attributesNode = etree.SubElement(graphNode, "attributes")
    attributesNode.set("class", "node")

    inputAttributeNode = etree.SubElement(attributesNode, "attribute")
    inputAttributeNode.set("id", "input")
    inputAttributeNode.set("title", "Input")
    inputAttributeNode.set("type", "string")

    outputAttributeNode = etree.SubElement(attributesNode, "attribute")
    outputAttributeNode.set("id", "output")
    outputAttributeNode.set("title", "Output")
    outputAttributeNode.set("type", "string")

    layerAttributeNode = etree.SubElement(attributesNode, "attribute")
    layerAttributeNode.set("id", "layer")
    layerAttributeNode.set("title", "Layer")
    layerAttributeNode.set("type", "string")

    verticesNode = etree.SubElement(graphNode, "nodes")
    edgesNode = etree.SubElement(graphNode, "edges")

    with Bar("Creating GEXF nodes...", max=df.shape[0]) as bar:
        for ID, NAME, INPUTS, OUTPUTS in df.itertuples(index=False):
            ID: str = str(ID)
            vertexNode = etree.SubElement(verticesNode, "node")
            vertexNode.set("id", ID)
            vertexNode.set("label", NAME)

            attvaluesNode = etree.SubElement(vertexNode, "attvalues")

            i: str
            for i in INPUTS:
                attvalueNode = etree.SubElement(attvaluesNode, "attvalue")
                attvalueNode.set("for", "input")
                attvalueNode.set("value", i)

                parentNodeNameID: tuple[str, str] | None = dfIDQuery(df=df, query=i)

                if parentNodeNameID is None:
                    pass
                else:
                    nodePairing: tuple[tuple[str, str], str] = (parentNodeNameID, ID)
                    edgeList.append(nodePairing)

            o: str
            for o in OUTPUTS:
                attvalueNode = etree.SubElement(attvaluesNode, "attvalue")
                attvalueNode.set("for", "output")
                attvalueNode.set("value", o)

            bar.next()

    with Bar("Creating GEXF edges...", max=len(edgeList)) as bar:
        pair: tuple[tuple[str, str], str]
        for pair in edgeList:
            edgeNode = etree.SubElement(edgesNode, "edge")
            edgeNode.set("id", str(EDGE_ID_COUNTER.__next__()))
            edgeNode.set("source", pair[0][1])
            edgeNode.set("target", pair[1])
            edgeNode.set("label", pair[0][0])
            bar.next()

    tree = etree.ElementTree(rootNode)
    try:
        tree.write(
            outputPath, xml_declaration=True, pretty_print=True, encoding="utf-8"
        )
    except TypeError:
        tree.write(
            outputPath[0], xml_declaration=True, pretty_print=True, encoding="utf-8"
        )


def main(args: Namespace) -> None:
    model: ModelProto = load(f=args.model[0])
    graph: GraphProto = model.graph

    with Bar(
        "Extracting information from ONNX computational graph...", max=len(graph.node)
    ) as bar:
        node: NodeProto
        for node in graph.node:
            nodeID: int = NODE_ID_COUNTER.__next__()
            name: str = node.name
            outputs: List[str] = list(node.output)
            inputs: List[str] = list(node.input)
            df: DataFrame = buildDF(
                nodeID=nodeID,
                name=name,
                inputs=inputs,
                outputs=outputs,
            )
            OUTPUT_DF_LIST.append(df)
            bar.next()
    df: DataFrame = pandas.concat(OUTPUT_DF_LIST)
    buildXML(df=df, outputPath=args.output, mode=args.mode)


if __name__ == "__main__":
    args: Namespace = getArgs()
    main(args=args)
