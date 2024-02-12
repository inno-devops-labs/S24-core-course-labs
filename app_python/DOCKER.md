# Dockerfile Best Practices
- The use of .dockerignore: .dockerignore file helps to exclude unnecessary files and directories from being copied into the image, 
reducing the image size and build time.
- Run as a non-root user: Application is run as a non-root user to minimize the potential security risks.
- The use of stable base image: Precise version `python:3.9.18-alpine3.18` is used to ensure consistency and avoid potential compatibility issues between different versions.
- Keeping layers immutable: Files or dependencies are not changed in the middle of the Dockerfile, as it can lead to inconsistencies and security vulnerabilities.