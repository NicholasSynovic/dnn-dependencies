from argparse import Namespace
from itertools import count
from pathlib import Path
from typing import List

import pandas
from lxml import etree
from onnx import load
from onnx.onnx_pb import GraphProto, ModelProto, NodeProto
from pandas import DataFrame
from progress.bar import Bar

from dnn_dependencies.args.architectureArgs import getArgs

NODE_ID_COUNTER: count = count()
OUTPUT_DF_LIST: List[DataFrame] = []


def buildDF(nodeID: int, name: str, inputs: List[str], outputs: List[str]) -> DataFrame:
    data: dict[str, List[int | str | List[str]]] = {
        "ID": [nodeID],
        "Name": [name],
        "Inputs": [inputs],
        "Outputs": [outputs],
    }
    return DataFrame(data)


def buildXML(df: DataFrame, outputPath: Path | List[Path]) -> None:
    rootNode = etree.Element("gexf")
    rootNode.set("xmlns", "http://www.gexf.net/1.2draft")
    rootNode.set("version", "1.2draft")

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

    verticesNode = etree.SubElement(graphNode, "nodes")

    with Bar("Creating GEXF nodes...", max=df.shape[0]) as bar:
        for ID, NAME, INPUTS, OUTPUTS in df.itertuples(index=False):
            vertexNode = etree.SubElement(verticesNode, "node")
            vertexNode.set("id", str(ID))
            # vertexNode.set("title", NAME)

            attvaluesNode = etree.SubElement(vertexNode, "attvalues")

            i: str
            for i in INPUTS:
                attvalueNode = etree.SubElement(attvaluesNode, "attvalue")
                attvalueNode.set("for", "input")
                attvalueNode.set("value", i)

            o: str
            for o in OUTPUTS:
                attvalueNode = etree.SubElement(attvaluesNode, "attvalue")
                attvalueNode.set("for", "output")
                attvalueNode.set("value", o)

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

    buildXML(df=pandas.concat(OUTPUT_DF_LIST), outputPath=args.output)


if __name__ == "__main__":
    args: Namespace = getArgs()
    main(args=args)
