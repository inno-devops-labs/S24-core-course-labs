# Docker Best Practices

## Non-Root User

To enhance security, the Docker image runs as a non-root user (`myuser`), reducing potential risks.

## COPY with Specific Files

The Dockerfile uses COPY with specific files to minimize unnecessary copying and reduce image size.

## Layer Sanity

Each instruction in the Dockerfile creates a new layer, ensuring better caching and improved build efficiency.

## .dockerignore

A `.dockerignore` file is used to exclude unnecessary files and directories from the image, reducing its size.

## Precise Base Image Version

The Dockerfile specifies a precise version of the base image and language, such as `python:3.8-alpine3.15`.
