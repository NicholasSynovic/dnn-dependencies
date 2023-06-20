from argparse import Namespace
from pprint import pprint as print

from torch import nn
from transformers import AutoModel
from transformers.models.gpt2.modeling_gpt2 import GPT2Model

from dnn_dependencies.args.summaryArgs import getArgs


def main() -> None:
    args: Namespace = getArgs(
        programName="HF PyTorch Model Summary Printer",
        description="A tool to print the model architecture layer summary to the console of PyTorch models hosted on HuggingFace",
    )

    model: nn.Module = AutoModel.from_pretrained(
        pretrained_model_name_or_path=args.model[0]
    )

    for m in list(model.named_modules()):
        print(m)


if __name__ == "__main__":
    main()
