#!/bin/bash

CURRENT_PATH=$(pwd)
IMAGE_NAME="denden047/WildPose_postprocessor"

docker build -t ${IMAGE_NAME} . && \
docker run -it --rm \
    -v "$CURRENT_PATH":/workdir \
    -v "$CURRENT_PATH"/../data:/data \
    -w /workdir \
    ${IMAGE_NAME} \
    /bin/bash
