# Docker Best Practices

This document outlines the Docker best practices we've implemented in our Dockerfile.

## Use a Minimal Base Image

We use `python:3.9-slim` as our base image. This is a minimal image that provides just the Python runtime, reducing the attack surface and the size of the final image.

## Multi-Stage Builds

We use multi-stage builds to separate the build-time and runtime dependencies. This reduces the size and attack surface of the final image. In the first stage, we install our dependencies and in the second stage, we copy over just the installed dependencies and our application code.

## Run as a Non-Root User

We create a non-root user `myuser` and switch to this user before running the application. This limits the potential damage that can be done if the container is compromised.

## No Cache for Pip Install

We use the `--no-cache-dir` option when installing dependencies with pip. This prevents pip from caching packages which can significantly reduce the size of the image.

## Copy Only Necessary Files

We only copy the necessary files into our Docker image. This reduces the size of the final image and prevents unnecessary files from being included.

## Regularly Update and Patch Your Images

Although not directly visible in the Dockerfile, it's important to regularly rebuild your Docker images to include the latest patches and updates from the base image and the installed dependencies.