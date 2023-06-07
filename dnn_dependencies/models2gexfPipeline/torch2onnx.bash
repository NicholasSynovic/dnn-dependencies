#!/bin/bash

# $1: First argument is the path or HuggingFace repository to convert
# $2: Second argument is the path to store the ONNX model

python -m transformers.onnx --model $1 --framework pt --preprocessor auto $2
