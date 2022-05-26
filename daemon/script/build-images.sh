#! /bin/bash

# build basic python image
PYTHON_ENV_VERSION="1.0"
PYTHON_ENV_NAME="python-env:$PYTHON_ENV_VERSION"
PYTHON_ENV_DOCKER_NAME="titan/$PYTHON_ENV_NAME"

docker build --force-rm -t $PYTHON_ENV_DOCKER_NAME -f docker/buildPythonEnv.dockerfile .