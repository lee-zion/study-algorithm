#!/bin/bash

mkfile() {
    array=()
    printf "%s" ""
    while read line ; do
        array+=("$line")
    done < <(python3 ./get_title.py "$1")
    mkdir -p -- "${array[0]}" &&
    cp .sample/* "${array[0]}" &&
    while read line ; do
        array+=("$line")
    done < <(python3 ./get_content.py "$1")
    
    # remove input/output path in test.py
    sed -i "s,problem_title,${array[0]},g" "${array[0]}/"test.py
    sed -i "s,example_num,${array[1]},g" "${array[0]}/"test.py
}

mkfile "${@}"