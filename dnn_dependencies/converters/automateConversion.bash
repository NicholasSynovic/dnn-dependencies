#!/bin/bash

# #Error message for no arguments
# if [[ "$#" -ne 2 ]]; then
#     echo "Usage: $0 inputPath outputPath"
#     exit 1
# fi

#input output paths
inputPath="$1"
outputPath="$2"


#Iterate through each onnx file in input folder
for inputFile in $(ls $inputPath); do
    echo $inputFile
    if [ -f "$inputFile" ]; then
        echo "file exists"
        #get filename w/o extension and save as gexf
        filename=$(basename "$inputFile")
        echo "$inputFile"
        outputFile="$outputPath/${filename%.*}.gexf"
        echo "converted file name"
        onnx2gexf -i "$inputFile" -o "$outputFile"
        echo "called program"
    else
        echo "can't find file"
    fi
done
