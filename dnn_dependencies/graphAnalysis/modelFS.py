import os
from argparse import Namespace
from pathlib import Path
from typing import List

from bs4 import BeautifulSoup, ResultSet, Tag
from progress.bar import Bar

from dnn_dependencies.args.modelFSArgs import getArgs


def extractNodeLabels(dom: str) -> List[Path]:
    data: List[Path] = []

    soup: BeautifulSoup = BeautifulSoup(markup=dom, features="lxml")
    nodeTags: ResultSet = soup.findAll(name="node")

    with Bar("Extacting node labels... ", max=len(nodeTags)) as bar:
        tag: Tag
        for tag in nodeTags:
            data.append(Path(tag.get(key="label")))
            bar.next()

    return data


def main() -> None:
    args: Namespace = getArgs()

    with open(file=args.input[0], mode="r") as xmlDoc:
        xmlDOM: str = xmlDoc.read()
        xmlDoc.close()

    nodeLabels: List[Path] = extractNodeLabels(dom=xmlDOM)

    updatedNodes: list[Path] = [
        Path(args.root[0], gexfFilePath.stem + node.attrib.get("label"))
        for node in nodes
    ]

    p: Path

    for p in updatedNodes:
        directoryComponent: Path = Path(p.parent)
        os.makedirs(directoryComponent, exist_ok=True)
        open(file=p, mode="w")


if __name__ == "__main__":
    main()
