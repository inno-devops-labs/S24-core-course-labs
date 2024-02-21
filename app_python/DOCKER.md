# Docker Best Practices in FastAPI Application

## Introduction

This document outlines the Docker best practices implemented in the Dockerfile for the FastAPI application that displays the current time in Moscow.

## Best Practices Employed

### Non-Root User

- Created and used a non-root user (`myuser`) to run the application, enhancing the security of the Docker container.

### Specific COPY

- Copied only the necessary files (`requirements.txt` followed by application code) to minimize the image size and reduce potential attack vectors.

### Layer Optimization

- Combined user creation and requirment installation steps into a single RUN command to reduce the image size by removing unnecessary layers.

### Use of .dockerignore

- Included a `.dockerignore` file to exclude files not needed for the Docker build, such as local development environments and version control files, to speed up the build process and reduce image size.

### Precise Base Image Version

- Specified a precise version of the Python image (`3.9.18-slim-bullseye`) to ensure consistent and reliable builds across environments.
