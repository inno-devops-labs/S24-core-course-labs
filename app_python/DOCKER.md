# Dockerfile Best Practices

## Implemented Best Practices

### 1. Layer sanity

The number of image layers has been minimized by combining related commands using multi-stage builds. This helps reduce
the final image size and enhances build performance.

### 2. Use Minimal Base Images

The Alpine Linux base image (`python:3.9.18-alpine3.19`) has been chosen as the base image, providing a minimal and
lightweight environment, reducing the overall image size and attack surface.

### 3. Non-Root User

A non-root user (`newuser`) has been created and set as the default user for running the application. This mitigates
potential security risks by minimizing privileges within the container.

### 4. Dependency Management

Dependency installation has been separated into a separate step to take
advantage of Docker layer caching. This helps improve build performance, especially during iterative development cycles.

### 5. EXPOSE Instruction

The `EXPOSE` instruction has been used to document the port that the application listens on. While it doesn't
actually publish the port, it provides clear information to users on which ports to expose when running the container.
