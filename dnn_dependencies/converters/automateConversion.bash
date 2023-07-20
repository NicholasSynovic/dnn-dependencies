#!/bin/bash

#Error message for no arguments
if [[ "$#" -ne 2 ]]; then
    echo "Usage: $0 inputPath outputPath"
    exit 1
fi

#input output paths
inputPath="$1"
outputPath="$2"


#Iterate through each onnx file in input folder
for inputFile in "$inputPath"/*; do
    if [ -f "$inputFile" ]; then
        #get filename w/o extension and save as gexf
        filename=$(basename "$inputFile")
        outputFile="$outputPath/${filename%.*}.gexf"
        ./onnx2gexf.py -i "$inputFile" -o "$outputFile"
    fi
done
