# Given a protobuf Graph model, print out each layer within the model using

from json import load
from pathlib import Path

from keras.models import load_model, model_from_json

MODEL: Path = Path("../models/bert_base_uncased.h5")
CONFIG: Path = Path("../models/config.json")


def main() -> None:
    with open(file=CONFIG, mode="r") as modelConfig:
        mc: str = modelConfig.read()
        modelConfig.close()

    # model = model_from_json(json_string=mc)
    model = load_model(filepath=MODEL)
    print(type(model))

    pass


if __name__ == "__main__":
    main()
