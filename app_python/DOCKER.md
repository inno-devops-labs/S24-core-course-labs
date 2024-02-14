# Docker Best Practices

In this document, we'll discuss the best practices employed within the Dockerfile for our Flask web application.

## 1. Use of Official Base Image

We start with the official Python Slim base image (`python:3.9-slim`). Official images are regularly updated, well-maintained, and come with security patches.

## 2. Non-Root User

To enhance security, we create a non-root user within the Dockerfile using the `adduser` command. This helps mitigate the risk of privilege escalation attacks.

```Dockerfile
# Create a non-root user
RUN adduser --disabled-password --gecos '' appuser
USER appuser
```