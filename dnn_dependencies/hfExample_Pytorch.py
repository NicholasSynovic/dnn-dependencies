from pathlib import Path

from torch.nn import Module
from transformers import AutoModel

MODEL: Path = Path("../models/")


def main() -> None:
    model: Module = AutoModel.from_pretrained(pretrained_model_name_or_path=MODEL)

    print(model)


if __name__ == "__main__":
    main()
