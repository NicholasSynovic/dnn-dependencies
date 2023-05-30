#!/bin/bash

python -m transformers.onnx --model $1 --framework pt --preprocessor auto $2
