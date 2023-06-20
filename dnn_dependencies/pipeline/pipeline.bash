#!/bin/bash

mkdir models
mkdir gexf
mkdir layers
mkdir dot

# python3.10 downloadModelJSONList.py

# cat baseModels.txt | parallel -I % --bar optimum-cli export onnx --model % --framework pt --atol 1 --monolith models/%.onnx

cat baseModels.txt | parallel -I % --bar dnn-dependencies-onnx2gexf --mode production --model models/%.onnx/model.onnx --output gexf/%.gexf

cat baseModels.txt | parallel -I % --bar dnn-dependencies-gexfLayerExtraction --input gexf/%.gexf --output layers/%.layers.gexf

cat baseModels.txt | parallel -I % --bar python scripts/convertGEXF.py --input layers/%.layers.gexf --output dot/%.dot
