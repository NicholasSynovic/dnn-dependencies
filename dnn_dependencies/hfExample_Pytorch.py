from pathlib import Path

import torch

MODEL: Path = Path("../models/pytorch_model.bin")


def main() -> None:
    model = torch.load(f=MODEL)

    print(model)


if __name__ == "__main__":
    main()
