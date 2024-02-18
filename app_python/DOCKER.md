# Docker Best Practices for `app_python` Dockerfile

This document outlines the Docker best practices implemented in the Dockerfile for the `app_python` application. These practices help in creating efficient, secure, and reliable Docker images.

- Using a Specific Version of the Base Image
- Running as a Non-Root User
- Organizing the Application into a Virtual Environment
- Minimizing the Number of Layers by command stacking and Caching Dependencies
- Cleaning Up Unnecessary Files (--no-cache-dir)
- Exposing Only Necessary Ports
- Explicit Command and Parameters
- Copying into docker container only neccessary files by avoiding wildcards in COPY
- I did not manage to make multi-stage dockerfile because python application can be statically builded

