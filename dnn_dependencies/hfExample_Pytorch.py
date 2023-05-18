from collections import OrderedDict
from pathlib import Path

import torch
from torch.nn import Embedding, Module, Sequential
from torchinfo import summary
from transformers import AutoModel, BertModel

MODEL: Path = Path("../models/pytorch_model.bin")


def main() -> None:
    model: Module = AutoModel.from_pretrained(
        pretrained_model_name_or_path="../models/"
    )

    print(model)

    # print(type(modules))


if __name__ == "__main__":
    main()
