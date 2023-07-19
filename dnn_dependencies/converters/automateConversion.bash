#!/bin/bash

#input output paths
input="$1"
output="$2"

#Check if input dir exists
if [ ! -d "$input" ]; then
    echo "Error: Input not found"
    exit 1
fi

#Check if output exists, create one if not
if [ ! -d "$output"]; then
    mkdir -p "$output"
fi

#path to program that is being wrapped
program="poetry run python onnx2gexf.py"

#Iterate through each onnx file
for onnxFile in "$input"/*.onnx; do
    #get filename w/o extension
    filename=$(basename -- "$onnxFile")
    filename="${filename%.*}"

    #output GEXF filepath
    gexfFile="$output/${filename}.gexf"

    #Run python program
    $program "$onnxFile" "gexfFile"

    #Check if successful
    if [ $? -eq 0 ]; then
        echo "Converted $onnxFile to $gexfFile successfully"
    else
        echo "Error converting $onnxFile to GEXF"
    fi

done
