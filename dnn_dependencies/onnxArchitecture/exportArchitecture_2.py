from argparse import Namespace
from collections import namedtuple
from itertools import count
from json import dumps
from pathlib import Path
from typing import List

import pandas
from onnx import GraphProto, ModelProto, NodeProto, load
from pandas import DataFrame
from progress.bar import Bar

from dnn_dependencies.args.generalArgs import getArgs

OUTPUT_ID_COUNTER: count = count()
OUTPUT_DF_LIST: List[DataFrame] = []


def buildOutputDF(output: str) -> DataFrame:
    data: dict[str, List[str]] = {
        "ID": [OUTPUT_ID_COUNTER.__next__()],
        "Output": [output],
    }
    return DataFrame(data)


def main() -> None:
    args: Namespace = getArgs(
        programName="ONNX Architecture Exporter",
        description="A tool to export an ONNX model's layer architecture to a JSON file (architecture.json)",
    )

    model: ModelProto = load(f=args.model[0])
    graph: GraphProto = model.graph

    node: NodeProto
    for node in graph.node:
        outputs: List[str] = list(node.output)

        output: str
        for output in outputs:
            OUTPUT_DF_LIST.append(buildOutputDF(output=output))

    outputDF: DataFrame = pandas.concat(objs=OUTPUT_DF_LIST, ignore_index=True)
    outputDF.drop_duplicates(subset=["Output"], inplace=True)
    print(outputDF)

    test: str = dumps({})

    with open("architecture.json", "w") as jsonFile:
        jsonFile.writelines(test)
        jsonFile.close()


if __name__ == "__main__":
    main()
