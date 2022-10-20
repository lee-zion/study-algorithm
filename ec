#!/bin/bash

lssample() {
    for entry in ".sample"/*
    do
        echo "$entry"
        filename=entry | sed 's/^\.\///g'
        echo "$filename"
    done
}

# mkfile() {
#     mkdir -p -- "$1"
#     for entry in "./sample"/*
#     do
#         filename=entry | sed 's/^\.\///g'
#         echo $filename
#         # cp "$entry" "$1"/ 

#     cp ./.sample/README.md "$1"/README.md && cp ./.sample/main.py "$1"/main.py && cp ./.sample/input.txt "$1"/input.txt ;
# }

# README='\#Test\n\rhello, world'
# echo "Test" > ./test/README.md

# mkfile "${@}"
lssample