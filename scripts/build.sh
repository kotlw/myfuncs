#!/bin/bash

FUNC=$1

mkdir -p ./dist
cp -r ./src/$FUNC ./dist
cd ./dist/$FUNC
poetry export --without-hashes --without-urls --only $FUNC | awk '{ print $1 }' FS=';' > requirements.txt
poetry run pip download -r requirements.txt -d wheelhouse
