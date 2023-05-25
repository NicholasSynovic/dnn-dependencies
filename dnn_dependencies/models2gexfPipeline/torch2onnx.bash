#!/bin/bash

# Takes in user input to either a file path or a HuggingFace repository name and an output filename

python -m transformers.onnx -m $1 --framework pt --preprocessor auto $2
