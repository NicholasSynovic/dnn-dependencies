#!/bin/bash

#Error message for no arguments
# if [[ "$#" -ne 2 ]]; then
#     echo "Usage: $0 inputPath outputPath"
#     exit 1
# fi

#Iterate through each onnx file in input folder
for f in $(ls $1/*.onnx);
do
    onnx2gexf --input $f --mode production --output "$f.gexf"
done

    # if [ -f "$inputFile" ]; then
        #get filename w/o extension and save as gexf
    #     filename=$(basename "$inputFile")
    #     outputFile="$outputPath/${filename%.*}.gexf"
    #     ./onnx2gexf.py -i "$inputFile" -o "$outputFile"
    # fi
