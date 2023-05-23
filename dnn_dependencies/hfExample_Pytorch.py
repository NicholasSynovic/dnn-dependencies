from argparse import Namespace
from pathlib import Path

from torch.nn import Module
from transformers import AutoModel

from dnn_dependencies.args.generalArgs import getArgs


def main() -> None:
    args: Namespace = getArgs(
        programName="HF PyTorch Model Summary Printer",
        description="A tool to print the model architecture layer summary to the console of PyTorch models hosted on HuggingFace",
    )

    model: Module = AutoModel.from_pretrained(pretrained_model_name_or_path=args.model)

    print(model)


if __name__ == "__main__":
    main()
