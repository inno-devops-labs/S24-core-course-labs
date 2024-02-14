# Docker Best Practices in the Moscow Time Go Application

## Introduction

This document details the Docker best practices implemented within the Dockerfile for the Go application that serves the current Moscow time. Our approach ensures the application is secure, efficient, and reliable when deployed using Docker.

## Best Practices Employed

### Multi-Stage Build

- Utilized a multi-stage build process, separating the build environment from the runtime environment. This approach keeps the final image size minimal by including only the compiled application and its runtime dependencies.

### Non-Root User

- For enhanced security, the application runs as a non-root user (`user`) within the Docker container. This practice limits the potential impact of security vulnerabilities that might affect the containerized application.

### Specific COPY

- The Dockerfile is designed to copy only the necessary files into our build stage (`go.mod`, optionally `go.sum`, and the application source code). This minimizes the Docker image size and reduces the attack surface by excluding unnecessary files.

### Layer Optimization

- Optimized Docker layers by structuring commands to cache dependencies effectively and reduce the overall number of layers. For instance, dependency downloading and application building steps are separated to leverage Docker's caching mechanism efficiently.

### Use of .dockerignore

- A `.dockerignore` file is included to exclude non-essential files from the Docker context, such as development tools, source control metadata, and other unnecessary files for the build process. This speeds up the build process and further reduces the image size.

### Precise Base Image Version

- Selected a specific version of the base image (`alpine:latest` at the time of writing) to ensure the build's consistency and reliability. It's recommended to periodically review and update this to a more specific version (e.g., `alpine:3.14`) to align with best practices for reproducibility and security.

### Time Zone Data

- Included the necessary `tzdata` package in the runtime image to support time zone configurations, addressing the common issue of unknown time zones in minimal base images. This ensures our application correctly handles the Moscow time zone without additional runtime errors.
