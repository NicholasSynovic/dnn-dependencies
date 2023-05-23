from argparse import Namespace
from collections import namedtuple
from itertools import count
from json import dumps
from pathlib import Path
from typing import List

from onnx import GraphProto, ModelProto, NodeProto, load
from progress.bar import Bar

from dnn_dependencies.args.generalArgs import getArgs

ModelNode = namedtuple(
    typename="ModelNode", field_names=["ID", "Name", "Inputs", "Outputs"]
)


def main() -> None:
    args: Namespace = getArgs(
        programName="ONNX Architecture Exporter",
        description="A tool to export an ONNX model's layer architecture to a JSON file (architecture.json)",
    )

    modelNodes: list[dict] = []
    ID: count = count()

    model: ModelProto = load(f=args.model)
    graph: GraphProto = model.graph

    with Bar("Extracting nodes information...", max=len(graph.node)) as bar:
        node: NodeProto
        for node in graph.node:
            mn: ModelNode = ModelNode(
                ID=ID.__next__(),
                Name=node.name,
                Inputs=list(node.input),
                Outputs=list(node.output),
            )
            modelNodes.append(mn._asdict())
            bar.next()

    test = dumps(modelNodes, indent=4)

    with open("architecture.json", "w") as jsonFile:
        jsonFile.writelines(test)
        jsonFile.close()


if __name__ == "__main__":
    main()
