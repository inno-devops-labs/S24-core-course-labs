# Dockerizing the Application

- Available on Docker Hub: [abuwho/app_go](https://hub.docker.com/r/abuwho/app_go)
- To pull the image: `docker pull abuwho/app_go:latest`

## Build
Instructions are available in the [README.md](./README.md#docker) file.

## Best practices implemented:

- **Use trusted base images**: The base image is from the official Go repository on Docker Hub. 
- **Use a precise version of base image and language**: The base image is `golang:1.21.3-alpine`. This ensures stability, compatibility and reproducibility. 
- **Rootless container**: The application runs as a non-root user.

    ![Rootless container](https://i.imgur.com/HGM14dl.png)

- **Use `COPY`, but only specific files**: Only the necessary files are copied into the image.
- **Layer sanity**: The Dockerfile is crafted to minimize the number of layers. This is done by combining multiple commands into a single `RUN` command.
- **Use `.dockerignore`**: The `.dockerignore` file is used to exclude unnecessary files from the image. It is done in order to reduce the size of the image and to avoid unnecessary files being copied into the image. 
- **Lint the Dockerfile**: The Dockerfile is linted using [hadolint](https://hadolint.github.io/hadolint/) to ensure best practices are followed.
