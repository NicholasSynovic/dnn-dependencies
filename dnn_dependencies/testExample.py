from pathlib import Path

from keras.engine.sequential import Sequential
from keras.models import load_model

MODEL: Path = Path("../models/veaaCNN.h5")


def main() -> None:
    model: Sequential = load_model(filepath=MODEL)

    with open(file="veaaCNN_Summary.json", mode="w") as jsonModel:
        jsonModel.write(model.to_json(indent=4))


if __name__ == "__main__":
    main()
