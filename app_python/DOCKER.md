# Docker Best Practices
In this Dockerfile, I strive to adhere to best practices to ensure efficiency, security, and maintainability of my containerized application.

## Utilizing Alpine Base Image
I've opted for the Alpine Linux base image for Python, specifically python:3.9-alpine3.18. Alpine images are lightweight and come with a minimal set of packages, reducing the attack surface and overall container size.

## Minimizing Layers
To optimize the build process and minimize the final image size, I've combined multiple RUN commands wherever possible. This reduces the number of layers generated during the build process, making the image smaller and more efficient.

## Non-Root User
Running containers as the root user can pose security risks. Therefore, I create a non-root user (nonroot) and set it as the default user for running the application. This mitigates potential security vulnerabilities.

## Copying Only Necessary Files
I copy only essential files (requirements.txt and app.py) into the container, reducing unnecessary file transfers and keeping the image lightweight.

## Caching Dependencies
By copying requirements.txt separately and installing dependencies before copying the application code, I leverage Docker's layer caching mechanism. This ensures faster builds by utilizing cached layers when dependencies haven't changed.

## Explicitly Exposing Ports
I explicitly expose port 5000, which is the port my Flask application listens on. This improves clarity and ensures that the required ports are appropriately documented and accessible.

## Clearing Cache
To maintain a smaller image size, I use the --no-cache-dir flag when installing Python dependencies via pip. This prevents caching of downloaded packages, reducing the final image size.

## Clean-Up
After installing dependencies and setting up the application, I ensure to clean up unnecessary files and directories within the container. This further reduces the image size and ensures a clean environment for running the application.