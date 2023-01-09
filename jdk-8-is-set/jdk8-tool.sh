#!/usr/bin/env bash

cmd=$3

if [[ "$cmd" = "run" ]] ; then
    echo "["

    javaPath=$(javac -version 2>&1)
    if [[ $javaPath =~ "javac 1.8" ]]; then
        echo "{ \"type\": \"JavaPath\", \"line\": 0, \"message\": \"$javaPath\", \"file\": \"none\" }"
    fi

    echo "]"
fi

if [[ "$cmd" = "name" ]] ; then
    echo "jdk8-checker"
fi

if [[ "$cmd" = "applicable" ]] ; then
    echo "true"
fi

if [[ "$cmd" = "version" ]] ; then
    echo "1"
fi
