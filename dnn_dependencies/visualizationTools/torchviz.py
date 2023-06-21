import re
from argparse import Namespace
from pprint import pprint as print

from torch import nn
from transformers import AutoModel
from transformers.models.gpt2.modeling_gpt2 import GPT2Model

from dnn_dependencies.args.summaryArgs import getArgs


def printLayerNames(moduleList: list[str], regexPattern) -> list:
    pattern = re.compile(regexPattern)
    layerNames = []
    for item in moduleList:
        if pattern.match(item):
            layerNames.append(item)
    return layerNames


def main() -> None:
    args: Namespace = getArgs(
        programName="HF PyTorch Model Summary Printer",
        description="A tool to print the model architecture layer summary to the console of PyTorch models hosted on HuggingFace",
    )

    model: nn.Module = AutoModel.from_pretrained(
        pretrained_model_name_or_path=args.model[0]
    )

    # print modules
    # for m in list(model.named_modules()):
    # print(m)

    module_names: list = [name for name, _ in model.named_modules()]
    pattern = r"h\.\d+$"
    layerNameList: list = printLayerNames(module_names, pattern)

    # format dictionary

    for layer in layerNameList:
        layerDict: dict[str:str] = {}
        for index, layer in enumerate(layerNameList):
            layerDict[layer] = f"Layer {index}"

    # sort dictionary

    sortedLayerDict: dict[str:str] = {}
    sortKeys = sorted(
        layerDict,
        key=lambda x: [int(d) if d.isdigit() else d for d in re.split(r"(\d+)", x)],
    )
    for k in sortKeys:
        sortedLayerDict[k] = layerDict[k]
    for l, v in sortedLayerDict.items():
        print(f"{l}: {v}")


if __name__ == "__main__":
    main()
