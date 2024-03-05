# Answers to Lab 2

## 1. Best practices applied within my Dockerfile

### Minimal Image

I have used a minimal base image to keep the size of my Docker image small.

### Caching

I have used caching to speed up the build process.
I have only added the necessary files and directories to the image.

### User

I have used a non-root user to run my application inside the container.
It is a best practice to run the application as a non-root user for security reasons.

### Layer Sanity

I have kept the number of layers in my Docker image to a minimum.
It makes the image easier to understand and maintain.

### Publishing

I have published my Docker image to a container registry.
It makes it easy to share and deploy my application.

### Dockerfile Linting

I used the online tool to lint my Dockerfile and ensure that it follows best practices.

### Dockerignore

I have used a `.dockerignore` file to exclude unnecessary files and directories from the Docker context.
This is useful to speed up the build process and reduce the size of the Docker image.