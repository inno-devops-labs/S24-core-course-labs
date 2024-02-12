
## Best Practices for writing Dockerfile

Enhance Docker Image with Security Best Practices

- Non-root user: Ensure that the Docker image runs with a non-root user to minimize security risks.
- Use precise base image version: Specify a precise version (`python:3.11-alpine3.18`) of both the base image and language to ensure consistency and avoid potential vulnerabilities in newer versions
- Use COPY with specific files: When copying files into the Docker image, only include the necessary files and directories. This reduces the size of the image and minimizes the risk of including sensitive information.
- Use .dockerignore: Utilize a .dockerignore to exclude unnecessary paths from being copied into the Docker image. This reduces the image size and improves security.
- Layer sanity: Optimize Dockerfile instructions to minimize the number of layers in the image. This improves build performance and reduces the attack surface.
- Multi-Stage Build: The Dockerfile utilizes a multi-stage build approach to separate the build environment from the final runtime environment
