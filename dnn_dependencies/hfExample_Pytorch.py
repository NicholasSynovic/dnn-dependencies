from pathlib import Path

from torch import Size, Tensor, onnx
from torch.nn import Module
from transformers import AutoModel

BERT_BASE_UNCASED: Path = Path("../models/bert_base_uncased")
BERT_BASE_UNCASED_REUSE: Path = Path("../models/bert_base_uncased_resue")


def main() -> None:
    model: Module = AutoModel.from_pretrained(
        pretrained_model_name_or_path=BERT_BASE_UNCASED_REUSE
    )

    print(model)

    # inputShape: Size = list(model.parameters())[0].shape

    # dummyInput:Tensor = Tensor(inputShape[0], inputShape[1])

    # onnx.export(model=model, args=dummyInput, f="test.onnx")


if __name__ == "__main__":
    main()
