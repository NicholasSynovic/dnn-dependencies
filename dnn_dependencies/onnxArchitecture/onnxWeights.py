from pathlib import Path
from pprint import pprint as print

import onnx
from onnx import numpy_helper
from onnx.onnx_ml_pb2 import TensorProto
from onnx.onnx_pb import ModelProto


def main() -> None:
    weights: dict = {}
    modelPath: Path = Path("model.onnx")

    model: ModelProto = onnx.load(f=modelPath.__str__())
    init = model.graph.initializer

    i: TensorProto
    for i in init:
        weight = numpy_helper.to_array(tensor=i)
        weights[i.name] = weight

    print(weights)


if __name__ == "__main__":
    main()
