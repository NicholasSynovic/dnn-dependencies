from collections import namedtuple
from itertools import count
from json import dumps
from pathlib import Path
from typing import List

from onnx import GraphProto, ModelProto, NodeProto, load
from progress.bar import Bar

MODEL: Path = Path("test.onnx/model.onnx")

ModelNode = namedtuple(
    typename="ModelNode", field_names=["ID", "Name", "Inputs", "Outputs"]
)


def main() -> None:
    modelNodes: list[dict] = []
    ID: count = count()

    model: ModelProto = load(f=MODEL)
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

    with open("test.json", "w") as jsonFile:
        jsonFile.writelines(test)
        jsonFile.close()


if __name__ == "__main__":
    main()
