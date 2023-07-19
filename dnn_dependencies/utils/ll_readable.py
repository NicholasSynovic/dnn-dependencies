from os import listdir
from pathlib import Path
from pprint import pprint as print
from typing import List

from progress.bar import Bar


def getFileList(directory: Path) -> List[Path]:
    data: List[Path] = [Path(directory, f) for f in listdir(path=directory)]
    return data


def main() -> None:
    REPLACEMENT_STR: str = (
        "./PTM-Torrent/ptm_torrent/huggingface/data/huggingface/repos/"
    )
    DIR: Path = Path("HF_TextFiles")

    modelInfo: dict[str, str] = {}

    fileList: List[Path] = getFileList(directory=DIR)

    with Bar("Extacting Model Name: Model File Path... ", max=len(fileList)) as bar:
        filepath: Path
        for filepath in fileList:
            if filepath.suffix != ".txt":
                bar.next()
                continue

            with open(filepath, "r") as file:
                data: List[str] = file.readlines()
                file.close()

            line: str
            for line in data:
                rawModelPath: str = line.strip().split(" ")[-1]
                modelPath: Path = Path(rawModelPath)

                rawModelName: str = rawModelPath.replace(REPLACEMENT_STR, "")
                modelName: str = "/".join(rawModelName.split("/")[0:2])

                modelInfo[modelName] = REPLACEMENT_STR + modelName

            bar.next()

    print(modelInfo)


if __name__ == "__main__":
    main()
