#!/bin/bash

# for f in $(ls $1/*.gexf);
# do
#     simScoreToDB --input $f
# done

for f in "$1"/*/*.gexf; do
    simScoreToDB --input "$f"
done
