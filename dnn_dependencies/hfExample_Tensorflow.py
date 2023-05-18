from pathlib import Path

from transformers import TFAutoModel

MODEL: Path = Path("../models/")


def main() -> None:
    model = TFAutoModel.from_pretrained(pretrained_model_name_or_path=MODEL)
    model.summary()


if __name__ == "__main__":
    main()
