from pathlib import Path

from transformers import TFAutoModel, TFBertModel

MODEL: Path = Path("../models/")


model: TFBertModel = TFAutoModel.from_pretrained(pretrained_model_name_or_path=MODEL)

with open(file="test2.json", mode="w") as jsonModel:
    jsonModel.write(model.to_json(indent=4))

model.summary()
