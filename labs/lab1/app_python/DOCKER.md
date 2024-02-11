# Docker

## Best practices used

- Minimal Base Image: The image uses `python:3.11.6-alpine3.18`, which is a
  minimal base image suitable for Python applications.
- Non-Root User: Non-root user `appuser` is used by default
  for the container, which reduces the risk associated with running
  processes as root.
- Copy Instructions: The COPY instructions are used instead of ADD, which is
  more explicit and less error-prone.
- Explicit Entrypoint: The image specifies an ENTRYPOINT to define the default
  executable for the container, which is a good practice.
