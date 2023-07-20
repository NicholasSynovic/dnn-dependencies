#!/bin/bash

helpMessage="Run ./pytorch2onnx.bash -h for command line arguments"

source ../../utils/optparse.bash

optparse.define short=m long=model desc="Hugging Face PyTorch model to convert to ONNX" variable=model
optparse.define short=o long=output-dir desc="Output directory to store the ONXN model" variable=outputDirectory

source $( optparse.build )

if [ -z $model ]
then
    echo "No input for -m | --model"
    echo $helpMessage
    exit 1
fi

if [ -z $outputDirectory ]
then
    echo "No input for -o | --output-dir"
    echo $helpMessage
    exit 1
fi

if [ -d $outputDirectory ]
then
    echo "Output directory ($outputDirectory) already exists. Please use an empty folder"
    echo $helpMessage
    exit 1
fi

optimum-cli export onnx --model $model --framework pt --atol 1 --monolith $outputDirectory
