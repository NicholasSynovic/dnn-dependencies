from collections import namedtuple
from itertools import count
from pathlib import Path
from typing import List

from onnx import GraphProto, ModelProto, NodeProto, load
from progress.bar import Bar

MODEL: Path = Path("test.onnx/model.onnx")

ModelNode = namedtuple(
    typename="ModelNode", field_names=["ID", "Name", "Inputs", "Outputs", "LayerNumber"]
)


def main() -> None:
    modelNodes: List[ModelNode] = []
    id: count = count()

    model: ModelProto = load(f=MODEL)
    graph: GraphProto = model.graph

    # print(len(graph.node))

    with Bar("Extracting nodes information...", max=len(graph.node)) as bar:
        node: NodeProto
        for node in graph.node:
            mn: ModelNode = ModelNode(
                ID=id.__next__(),
                Name=node.name,
                Inputs=node.input,
                Outputs=node.output,
                LayerNumber=0,
            )
            modelNodes.append(mn)
            bar.next()


if __name__ == "__main__":
    main()
