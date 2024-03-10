# Docker Best Practices

This document outlines the best practices that were employed in the Dockerfile
for my Python application.

## 1. Use a Specific Base Image Tag

I always use a specific version for my base image to ensure consistency across
my builds and to avoid unexpected changes that might come from the latest
versions.

## 2. Leverage Build Cache

I structure my Dockerfiles to take advantage of Docker's build cache. This often
involves copying the requirements file and installing dependencies before
copying the rest of the application.

## 3. Minimize Number of Layers

I aim to minimize the number of layers in my Docker images by combining commands
using `&&` where possible.

## 4. Non-Root User

For security reasons, I run applications as a non-root user in my Docker
containers.

## 5. Copy Only Necessary Files

I only copy the necessary files into the Docker image to reduce its size and
minimize the attack surface.

## 6. Don’t Bind to a Specific UID

I avoid binding to a specific user ID (UID) to ensure that the container runs
correctly under different UIDs.

## 7. Make Executables Owned by Root and Not Writable

I ensure that all executables are owned by root and not writable by other users.
This prevents non-root users from modifying the executables.

## 8. Multi-Stage Builds

I use multi-stage builds to keep my production images small. This involves
installing dependencies and building the application in a builder image, and
then copying the virtual environment to a smaller base image.

## 9. Use the Minimal Required Base Container

I use the smallest base image that provides the functionality I need. This
reduces the size of my Docker images and minimizes the attack surface.

## 10. Use Trusted Base Images

I use base images from trusted sources to ensure that my Docker images are
secure and reliable.

## 11. Exposed Ports

I explicitly declare the ports that the application uses using the `EXPOSE`
instruction. This makes it clear which ports need to be mapped to the host.

## 12. Prefer COPY over ADD

I use `COPY` instead of `ADD` unless I need the extra functionality provided by
`ADD` (like automatic tar extraction). `COPY` is more transparent because it
only supports basic file copying.

## 13. Metadata Labels

I use labels to add metadata to my Docker images.

## 14. Linting

I use the `hadolint` linter to check my Dockerfile for common mistakes and to
ensure that I'm following best practices.
