import subprocess
from argparse import Namespace
from pathlib import Path
from shutil import rmtree
from subprocess import Popen

from dnn_dependencies.args.pipelineArgs import getArgs
from dnn_dependencies.onnxArchitecture import exportArchitecture


def torch2onnx(path: Path, outputFolder: Path) -> None:
    command: str = f"python -m transformers.onnx --model {path} --framework pt --preprocessor auto {outputFolder}"
    p1: Popen = Popen(args=command, shell=True)
    p1.wait()


def main() -> None:
    args: Namespace = getArgs()

    modelPath: Path = args.model[0]
    onnxConversionPath: Path = Path(modelPath.name + ".onnx")
    onnxModelPath: Path = Path(onnxConversionPath, "model.onnx")

    exporterArgs: Namespace = Namespace(model=[onnxModelPath], output=args.output[0])

    torch2onnx(path=modelPath, outputFolder=onnxConversionPath)
    exportArchitecture.main(args=exporterArgs)

    if args.onnx:
        pass
    else:
        rmtree(path=onnxConversionPath)


if __name__ == "__main__":
    main()
