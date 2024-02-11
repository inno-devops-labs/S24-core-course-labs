# Lab 2: Containerization - Docker

## Bonus Task

- I have created a Dockerfile for JavaScript application and pushed it to my [dockerhub repository](https://hub.docker.com/repository/docker/ozurexus/my-js-app) using the following commands.

```bash
docker build -t my-js-app .
docker run -p 8080:8080 my-js-app
docker login
docker tag my-js-app ozurexus/my-js-app
docker push ozurexus/my-js-app
```

- I used a specific version of my base image and language, to be precise `node:14-alpine3.15`.
- I created a `.dockerignore` file to exclude unnecessary files from the context.
- I used `COPY` to copy only specific files.
- I checked the structure using a Dockerfile linter.
- I created a user inside the container to avoid running the application as root.
