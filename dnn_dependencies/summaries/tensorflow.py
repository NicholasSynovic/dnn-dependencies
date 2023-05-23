from argparse import Namespace

from transformers import TFAutoModel

from dnn_dependencies.args.generalArgs import getArgs


def main() -> None:
    args: Namespace = getArgs(
        programName="HF TensorFlow Model Summary Printer",
        description="A tool to print the model architecture layer summary to the console of TensorFlow models hosted on HuggingFace",
    )

    model = TFAutoModel.from_pretrained(pretrained_model_name_or_path=args.model[0])

    model.summary()


if __name__ == "__main__":
    main()
