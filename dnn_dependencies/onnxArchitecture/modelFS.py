import os
from argparse import Namespace
from pathlib import Path

from lxml import etree

from dnn_dependencies.args.modelFSArgs import getArgs

args = getArgs()
# Load the GEXF file
gexfFilePath: Path = Path(args.input[0])

tree = etree.parse(gexfFilePath)

# Define the namespace
ns = {"gexf": "http://www.gexf.net/1.2draft"}

# Select all 'node' elements
nodes = tree.findall(".//gexf:node", namespaces=ns)


updatedNodes: list[str] = [
    Path(args.root[0], gexfFilePath.stem + node.attrib.get("label")) for node in nodes
]

p: Path
for p in updatedNodes:
    directoryComponent: Path = Path(p.parent)
    os.makedirs(directoryComponent, exist_ok=True)
    open(file=p, mode="w")
