## Rootless container:
The Dockerfile creates a non-root user (`flaskuser`) and sets it as the user to run the Flask application within the container.

## Use COPY, but only specific files:
The `COPY` instruction copies only `app.py` and `requirements.txt` into the `/app` directory of the container.

## Layer sanity:
Each instruction in the Dockerfile is designed to optimize Docker's layer caching mechanism to ensure efficient image builds.

## Use .dockerignore:
Although not explicitly shown in the Dockerfile, it's essential to have a `.dockerignore` file in the same directory as the Dockerfile to exclude unnecessary files from being copied into the Docker image during the build process.

## Use a precise version of the base image and language:
The Dockerfile specifies a precise version of the Python base image (`python:3-alpine3.15`) to ensure consistency and avoid unexpected changes from newer versions.
