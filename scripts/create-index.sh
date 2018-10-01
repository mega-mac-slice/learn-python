#!/usr/bin/env bash

echo "# Index" > ./INDEX.md

files=($(ls ./src/*/README.md))

for path in "${files[@]}"
do
    line=$(awk 'NR==1 {print;}' ${path})
    heading=${line:2}
    echo "- [${heading}](${path})" >> ./INDEX.md
done