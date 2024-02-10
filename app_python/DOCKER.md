# Lab 2: Containerization - Docker

## Task 1: Dockerize Your Application

- After Writing the Dockerfile, I build the image, test it and then push to my [dockerhub repository](https://hub.docker.com/repository/docker/ozurexus/my-flask-app) using the following commands.

```bash
docker build -t my-flask-app .
docker run -p 5000:5000 my-flask-app
docker login
docker tag my-flask-app ozurexus/my-flask-app
docker push ozurexus/my-flask-app
docker pull ozurexus/my-flask-app
docker run -p 5000:5000 ozurexus/my-flask-app
```

## Task 2: Docker Best Practices

- I have implemented the following best practices in my Dockerfile:
  - No root user inside the container.
  - Used COPY, but only specific files.
  - Layer sanity.
  - Used `.dockerignore`.
  - Used a precise version of my base image and language, to be precise `python:3-alpine3.15`.
  - Structure is checked using a Dockerfile linter.
