from argparse import Namespace
from pprint import pprint
from typing import Generator, List

import torchinfo
from torch import nn
from transformers import AutoConfig, AutoModel

from dnn_dependencies.args.summaryArgs import getArgs


def extractModules(model: nn.Module) -> List[tuple]:
    nm: List[tuple[str, nn.Module]] = list(model.named_modules(remove_duplicate=True))[
        1::
    ]
    moduleNames: List[str] = [pair[0] for pair in nm]

    name: str
    for name in moduleNames:
        submodule: nn.Module = model.get_submodule(target=name)

        try:
            name: str = submodule._get_name()
        except AttributeError:
            continue

        print(name, submodule)
        input()


def main() -> None:
    args: Namespace = getArgs(
        programName="HF PyTorch Model Summary Printer",
        description="A tool to print the model architecture layer summary to the console of PyTorch models hosted on HuggingFace",
    )

    model: nn.Module | AutoModel = AutoModel.from_pretrained(
        pretrained_model_name_or_path=args.model[0]
    )

    print("===")
    print()
    torchinfo.summary(model)
    print(model)

    extractModules(model)


if __name__ == "__main__":
    main()
