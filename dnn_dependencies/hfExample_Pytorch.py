from pathlib import Path

from torch.nn import Module
from transformers import AutoModel

BERT_BASE_UNCASE: Path = Path("../models/bert_base_uncased")
BERT_BASE_UNCASE_REUSE: Path = Path("../models/bert_base_uncased_reuse")


def main() -> None:
    model: Module = AutoModel.from_pretrained(
        pretrained_model_name_or_path=BERT_BASE_UNCASE
    )

    print(model)


if __name__ == "__main__":
    main()
