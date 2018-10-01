#!/usr/bin/env bash
NOW="$(date +'%Y_%m_%d')_$(date +%s)"
NEW_PATH="./src/${NOW}"

mkdir -p ${NEW_PATH}
cp ./template/main.py ${NEW_PATH}/
echo "# ${NOW}" > ${NEW_PATH}/README.md
echo "# ${NOW}" > ${NEW_PATH}/SOLUTION.md

