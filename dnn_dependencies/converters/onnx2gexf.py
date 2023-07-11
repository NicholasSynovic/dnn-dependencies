from argparse import Namespace
from itertools import count
from pathlib import Path, PosixPath
from re import Match, search
from typing import List
from xml.etree.ElementTree import Element, ElementTree

import pandas
from lxml import etree
from matplotlib.colors import XKCD_COLORS
from onnx import load
from onnx.onnx_pb import GraphProto, ModelProto, NodeProto
from pandas import DataFrame, Series
from progress.bar import Bar

from dnn_dependencies.args.onnx2gexf_args import getArgs

NODE_ID_COUNTER: count = count()
EDGE_ID_COUNTER: count = count()
OUTPUT_DF_LIST: List[DataFrame] = []


def extractLayer(nodeName: str) -> str:
    """
    The function `extractLayer` takes a `nodeName` as input and returns the layer number extracted from
    the node name using a regular expression pattern.

    :param nodeName: The `nodeName` parameter is a string that represents the name of a node
    :type nodeName: str
    :return: a string that represents the layer extracted from the given `nodeName`.
    """
    pattern: str = r"layer\.(\d+)"

    layer: str
    try:
        layer = search(pattern=pattern, string=nodeName).group(0)
    except AttributeError:
        layer = ""

    return layer


def buildDF(
    nodeID: int,
    name: str,
    opType: str,
    layer: str,
    inputs: List[str],
    outputs: List[str],
    color: List[str],
) -> DataFrame:
    """
    The function `buildDF` takes in various parameters and returns a DataFrame object with the provided
    data.

    :param nodeID: The `nodeID` parameter is an integer that represents the ID of the node. It is used
    to uniquely identify a node in a graph or network
    :type nodeID: int
    :param name: The `name` parameter is a string that represents the name of the node
    :type name: str
    :param opType: The `opType` parameter represents the operation type of the node. It can be a string
    that describes the type of operation being performed by the node, such as "add", "multiply",
    "convolution", etc
    :type opType: str
    :param layer: The "layer" parameter represents the layer in which the node is located. It is a
    string that specifies the layer name or number
    :type layer: str
    :param inputs: A list of strings representing the input nodes to the current node
    :type inputs: List[str]
    :param outputs: The "outputs" parameter is a list of strings that represents the output nodes of the
    current node. Each string in the list represents the ID of an output node
    :type outputs: List[str]
    :param color: The "color" parameter is a list of strings that represents the color of the node. Each
    string in the list corresponds to a specific color
    :type color: List[str]
    :return: a DataFrame object.
    """
    data: dict[str, List[int | str | List[str]]] = {
        "ID": [nodeID],
        "Name": [name],
        "Op Type": [opType],
        "Layer": [layer],
        "Inputs": [inputs],
        "Outputs": [outputs],
        "Color": [color],
    }
    return DataFrame(data)


def dfIDQuery(df: DataFrame, query: str) -> tuple[str, str] | None:
    """
    The `dfIDQuery` function takes a DataFrame and a query string as input, and returns a tuple
    containing the name and ID of the first row that matches the query in the "Outputs" column, or None
    if no match is found.

    :param df: DataFrame - The input DataFrame containing the data
    :type df: DataFrame
    :param query: The `query` parameter is a string that represents the search query. It is used to
    search for a specific value in the "Outputs" column of the DataFrame
    :type query: str
    :return: The function `dfIDQuery` returns a tuple containing the name and ID of the first row in the
    DataFrame `df` that matches the given query. The name is returned as a string and the ID is returned
    as a string. If no matching row is found, the function returns `None`.
    """
    mask = df["Outputs"].apply(lambda x: query in x)
    tempDF: DataFrame = df[mask]

    try:
        return (tempDF["Name"].iloc[0], str(tempDF["ID"].iloc[0]))
    except IndexError:
        return None


def buildXML(
    df: DataFrame,
    mode: str = "production",
) -> str:
    """
    The `buildXML` function takes a DataFrame as input and generates an XML string in GEXF format based
    on the data in the DataFrame.

    :param df: The `df` parameter is a DataFrame object that contains the data to be used for building
    the XML. It is expected to have the following columns: `ID`, `NAME`, `OPTYPE`, `LAYER`, `INPUTS`,
    `OUTPUTS`, and `COLOR`
    :type df: DataFrame
    :param mode: The `mode` parameter in the `buildXML` function is used to specify the mode in which
    the XML is being built. It has a default value of "production", but can be overridden by passing a
    different value, defaults to production
    :type mode: str (optional)
    :return: The function `buildXML` returns a string representation of an XML document.
    """
    edgeList: List[tuple[tuple[str, str], str]] = []

    version: str
    if mode == "production":
        version = "1.2draft"
    else:
        version = "1.2"

    xmlns: str = f"http://www.gexf.net/{version}"
    xmlnsViz: str = f"http://gexf.net/{version}/viz"

    rootNode: Element = etree.Element("gexf", nsmap={None: xmlns, "viz": xmlnsViz})
    rootNode.set("version", version)

    graphNode: Element = etree.SubElement(rootNode, "graph")
    graphNode.set("mode", "static")
    graphNode.set("defaultedgetype", "directed")
    graphNode.set("idtype", "integer")

    attributesNode: Element = etree.SubElement(graphNode, "attributes")
    attributesNode.set("class", "node")

    inputAttributeNode: Element = etree.SubElement(attributesNode, "attribute")
    inputAttributeNode.set("id", "type")
    inputAttributeNode.set("title", "Operation_Type")
    inputAttributeNode.set("type", "string")

    inputAttributeNode: Element = etree.SubElement(attributesNode, "attribute")
    inputAttributeNode.set("id", "input")
    inputAttributeNode.set("title", "Input")
    inputAttributeNode.set("type", "string")

    outputAttributeNode: Element = etree.SubElement(attributesNode, "attribute")
    outputAttributeNode.set("id", "output")
    outputAttributeNode.set("title", "Output")
    outputAttributeNode.set("type", "string")

    layerAttributeNode: Element = etree.SubElement(attributesNode, "attribute")
    layerAttributeNode.set("id", "layer")
    layerAttributeNode.set("title", "Layer")
    layerAttributeNode.set("type", "string")

    verticesNode: Element = etree.SubElement(graphNode, "nodes")
    edgesNode: Element = etree.SubElement(graphNode, "edges")

    with Bar("Creating GEXF nodes...", max=df.shape[0]) as bar:
        for ID, NAME, OPTYPE, LAYER, INPUTS, OUTPUTS, COLOR in df.itertuples(
            index=False
        ):
            ID: str = str(ID)
            vertexNode: Element = etree.SubElement(verticesNode, "node")
            vertexNode.set("id", ID)
            vertexNode.set("label", NAME)

            vizColorNode: Element = etree.SubElement(vertexNode, "color")
            vizColorNode.set("hex", COLOR)

            attvaluesNode: Element = etree.SubElement(vertexNode, "attvalues")

            attvalueNode: Element = etree.SubElement(attvaluesNode, "attvalue")
            attvalueNode.set("for", "type")
            attvalueNode.set("value", OPTYPE)

            attvalueNode: Element = etree.SubElement(attvaluesNode, "attvalue")
            attvalueNode.set("for", "layer")
            attvalueNode.set("value", LAYER)

            i: str
            for i in INPUTS:
                attvalueNode: Element = etree.SubElement(attvaluesNode, "attvalue")
                attvalueNode.set("for", "input")
                attvalueNode.set("value", i.replace(":", "-"))

                parentNodeNameID: tuple[str, str] | None = dfIDQuery(df=df, query=i)

                if parentNodeNameID is None:
                    pass
                else:
                    nodePairing: tuple[tuple[str, str], str] = (parentNodeNameID, ID)
                    edgeList.append(nodePairing)

            o: str
            for o in OUTPUTS:
                attvalueNode: Element = etree.SubElement(attvaluesNode, "attvalue")
                attvalueNode.set("for", "output")
                attvalueNode.set("value", o.replace(":", "-"))

            bar.next()

    with Bar("Creating GEXF edges...", max=len(edgeList)) as bar:
        pair: tuple[tuple[str, str], str]
        for pair in edgeList:
            edgeNode: Element = etree.SubElement(edgesNode, "edge")
            edgeNode.set("id", str(EDGE_ID_COUNTER.__next__()))
            edgeNode.set("source", pair[0][1])
            edgeNode.set("target", pair[1])
            edgeNode.set("label", pair[0][0])
            bar.next()

    xmlStr: str = etree.tostring(rootNode, pretty_print=True).decode()
    xmlStr = xmlStr.replace("<color", "<viz:color")

    return xmlStr


def main() -> None:
    """
    The main function extracts information from an ONNX computational graph, builds a DataFrame, and
    writes the data to an XML file.
    """
    args: Namespace = getArgs()
    colors: List[str] = list(XKCD_COLORS.values())

    model: ModelProto = load(f=args.input[0])
    graph: GraphProto = model.graph

    with Bar(
        "Extracting information from ONNX computational graph...", max=len(graph.node)
    ) as bar:
        previousLayer: str = ""
        colorIDX: int = 0

        node: NodeProto
        for node in graph.node:
            nodeID: int = NODE_ID_COUNTER.__next__()
            name: str = node.name
            opType: str = node.op_type
            layer: str = extractLayer(nodeName=name)

            if layer != previousLayer:
                colorIDX += 1
                previousLayer = layer

            color: str = colors[colorIDX]
            outputs: List[str] = list(node.output)
            inputs: List[str] = list(node.input)
            df: DataFrame = buildDF(
                nodeID=nodeID,
                name=name,
                opType=opType,
                layer=layer,
                inputs=inputs,
                outputs=outputs,
                color=color,
            )
            OUTPUT_DF_LIST.append(df)
            bar.next()
    df: DataFrame = pandas.concat(OUTPUT_DF_LIST)
    xmlStr = buildXML(df=df, mode=args.mode)

    with open(file=args.output[0], mode="w") as xmlFile:
        xmlFile.write(xmlStr)
        xmlFile.close()


if __name__ == "__main__":
    main()
