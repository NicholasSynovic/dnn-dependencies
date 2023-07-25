#!/bin/bash

helpMessage="Run ./computeMetrics.bash -h for command line arguments"

source ../../utils/optparse.bash

optparse.define short=d long=directory desc="Path to directory containing directories holding GEXF files" variable=directory

source $( optparse.build )

if [ -z $directory ]
then
    echo "No input for -d | --directory"
    echo $helpMessage
    exit 1
fi

for path in $(ls $directory/*/*.gexf);
do
    computeMetrics --input $path
done
