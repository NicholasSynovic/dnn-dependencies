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
NODE_ID: count = count()
OUTPUT_ID: count = count()


def labelOutputs(outputs: list[str]) -> dict[int, str]:
    data: dict[int, str] = {}

    output: str
    for output in outputs:
        data[OUTPUT_ID.__next__()] = output

    return data


def main() -> None:
    args: Namespace = getArgs(
        programName="ONNX Architecture Exporter",
        description="A tool to export an ONNX model's layer architecture to a JSON file (architecture.json)",
    )

    modelNodes: list[dict] = []

    model: ModelProto = load(f=args.model[0])
    graph: GraphProto = model.graph

    with Bar("Extracting nodes information...", max=len(graph.node)) as bar:
        node: NodeProto
        for node in graph.node:
            mn: ModelNode = ModelNode(
                ID=NODE_ID.__next__(),
                Name=node.name,
                Inputs=list(node.input),
                Outputs=labelOutputs(outputs=list(node.output)),
            )
            modelNodes.append(mn._asdict())
            bar.next()

    test = dumps(modelNodes, indent=4)

    with open("architecture.json", "w") as jsonFile:
        jsonFile.writelines(test)
        jsonFile.close()


if __name__ == "__main__":
    main()
