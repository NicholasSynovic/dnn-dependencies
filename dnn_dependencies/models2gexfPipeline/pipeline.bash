#!/bin/bash

python3.10 downloadModelJSONList.py

cat baseModels.txt | xargs -I % python3.10 -m transformers.onnx --model % --framework pt --preprocessor auto %.onnx

cat baseModels.txt | xargs -I % dnn-dependencies-onnx2gexf --mode production --model %.onnx/model.onnx --output %.gexf
