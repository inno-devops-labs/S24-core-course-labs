# Dockerizing the Application

- Available on Docker Hub: [abuwho/app_python](https://hub.docker.com/r/abuwho/app_python)
- To pull the image: `docker pull abuwho/app_python:latest`

## Build
Instructions are available in the [README.md](./README.md#docker) file.

## Best practices implemented:

1. **Rootless container**: The application runs as a non-root user.
    
    ![Rootless container](https://i.imgur.com/vRJVfYG.png)

2. **Use `COPY`, but only specific files**: Only the necessary files are copied into the image.
3. **Layer sanity**: The Dockerfile is crafted to minimize the number of layers. This is done by combining multiple commands into a single `RUN` command.
4. **Use `.dockerignore`**: The `.dockerignore` file is used to exclude unnecessary files from the image. It is done in order to reduce the size of the image and to avoid unnecessary files being copied into the image. 
5. **Use a precise version of base image and language**: The base image is `python:3.9.18-alpine3.19@sha256:7e53de21917d6793787bc67483838360404bb2fd70d9c3e38ccc243790c323b2`. This ensures stability and reproducibility.
6. **Lint the Dockerfile**: The Dockerfile is linted using [hadolint](https://hadolint.github.io/hadolint/) to ensure best practices are followed.



