# Receipt Processor

Submission for the Receipt Processor Challenge.

## Running the Backend

1. Download the Docker image `receipt_processor_latest.tar.gz`. Cloning the repo is not required.

2. Load the docker image:
```
docker load -i receipt_processor_latest.tar.gz
```

3. Run the docker image on port `${PORT}`:
```
docker run -it --publish ${PORT}:${PORT} --rm receipt_processor:latest --port ${PORT}
```
