# Best practices

- I used a precise version of base image and language `python:3.9.18-alpine3.19`.
- I studied Docker multi-stage builds. I do not consider them in my project because I have interpreter and source files (no need to compile them).
- My container is rootless (all commands are runned on behalf of a non-root user).
- Layer sanity is ensured (no extra layers are added).
- COPY is used only with specific files (via .dockerignore).
- I utilized a [Dockerfile linter](https://github.com/hadolint/hadolint) for Q/A
  - `docker container run --rm -i hadolint/hadolint hadolint - < Dockerfile`
- The image and container are thoroughly tested, they function correctly.
- [Link](https://hub.docker.com/repository/docker/ieorekhov/s24-devops/general) to Dockerhub, pushing and pulling work as intended.
