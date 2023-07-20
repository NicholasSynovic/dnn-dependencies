#!/bin/bash

for f in $(ls $1/*.gexf);
do
    simScoreToDB --input $f
done
