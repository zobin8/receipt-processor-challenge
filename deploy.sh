#!/usr/bin/env bash

# Create wheel file
rm dist/*.whl
python3 setup.py bdist_wheel

# Build docker image
docker build -t receipt_processor:latest -f docker/Dockerfile .

docker save receipt_processor:latest -o receipt_processor_latest.tar.gz
