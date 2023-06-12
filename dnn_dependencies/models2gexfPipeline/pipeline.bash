#!/bin/bash

python3.10 downloadModelJSONList.py

cat baseModels.txt | xargs -I % optimum-cli export onnx --model % --framework pt %.onnx

cat baseModels.txt | xargs -I % dnn-dependencies-onnx2gexf --mode production --model %.onnx/model.onnx --output %.gexf
