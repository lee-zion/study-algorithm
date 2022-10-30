#!/bin/bash

mkfile() {
    mkdir -p -- "$1"
    cp .sample/* "$1"
    sed -i "s,title,$1,g" "$1/"README.md
    if [[ $# > 1 ]];
    then
        sed -i "s~#link~$2~g" "$1/"README.md
    fi
}

mkfile "${@}"