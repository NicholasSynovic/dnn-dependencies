#!/bin/bash

helpMessage="Run ./computeMetrics.bash -h for command line arguments"

source ../../utils/optparse.bash

optparse.define short=d long=directory desc="Path to directory containing directories holding GEXF files" variable=directory
optparse.define short=o long=database desc="Path to database to store information" variable=database

source $( optparse.build )

if [ -z $directory ]
then
    echo "No input for -d | --directory"
    echo $helpMessage
    exit 1
fi

if [ -z $database ]
then
    echo "No input for -o | --database"
    echo $helpMessage
    exit 1
fi

for path in $(ls $directory/*/*.gexf);
do
    computeMetrics --input $path --output $database
done
