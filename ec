#!/bin/bash

mkfile() {
    mkdir -p -- "$1"
    cp .sample/* "$1"
}

mkfile "${@}"