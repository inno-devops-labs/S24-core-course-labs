# Docker Security Best Practices

- Non-root User: The Docker image runs the application using a non-root user (flaskuser) to reduce the risk of security vulnerabilities.
- Specific File Copying: The COPY command is used to copy only specific files required for the application, reducing the attack surface and optimizing build times.
- Layer Sanity: Commands are organized to minimize the number of layers in the Docker image. This helps with image size, improves caching, and reduces potential security risks.
- Precise Base Image: The image is based on python:3-alpine3.15, using a precise version of the base image to ensure consistency and security. Alpine Linux is known for its lightweight nature.
- .dockerignore: A .dockerignore file is used to exclude unnecessary files and directories from being copied into the Docker image, reducing the image size and improving security.
