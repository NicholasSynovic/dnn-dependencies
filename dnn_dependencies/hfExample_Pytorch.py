from pathlib import Path

from torch.nn import Module
from transformers import AutoModel

MODEL: Path = Path("../models/pytorch_model.bin")


def main() -> None:
    model: Module = AutoModel.from_pretrained(
        pretrained_model_name_or_path="../models/"
    )

    print(model)

    # print(type(modules))


if __name__ == "__main__":
    main()
