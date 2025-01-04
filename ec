#!/bin/bash

# Detect the operating system
case "$(uname)" in
    Darwin*)
        SED=gsed
        SED_OPTS=(-i '' -e)
        ;;
    Linux*|CYGWIN*|MINGW*|MSYS*|Windows_NT*)
        SED=sed
        SED_OPTS=(-i -e)
        ;;
    *)
        echo "Unsupported OS"
esac

mkfile() {
    array=()
    printf "%s" ""
    while read line ; do
        array+=("$line")
    done < <(python3 ./.ec/get_title.py "$1")
    mkdir -p -- "${array[0]}" &&
    cp .sample/* "${array[0]}"
    tester="test.py"
    while read line ; do
        array+=("$line")
    done < <(python3 ./.ec/get_content.py "$1")
    
    # remove input/output path in test.py
    gsed -i "s|problem_title|${array[0]}|g" "${array[0]}/${tester}"
    gsed -i "s|example_num|${array[1]}|g" "${array[0]}/${tester}"
    # "$SED" "${SED_OPTS[@]}" "s|problem_title|${array[0]}|g" "${array[0]}/${tester}"
    # "$SED" "${SED_OPTS[@]}" "s|example_num|${array[1]}|g" "${array[0]}/${tester}"
    # $SED "s|problem_title|${array[0]}|g" "${array[0]}/${tester}"
    # $SED "s|example_num|${array[1]}|g" "${array[0]}/${tester}"
}

mkfile "${@}"