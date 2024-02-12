# Dockerfile Documentation
## Best Practices
1. Base Image Version:

* Utilized a precise version of the base image and language: python:3.9.18-slim-bullseye.

2. Rootless Container:

* Ensured a rootless container where all commands are executed on behalf of a non-root user (app).

4. Layer Sanity:

* Maintained layer sanity by avoiding the addition of unnecessary layers. Each instruction is carefully structured to minimize image size.

5. Selective COPY:

* Used the COPY instruction selectively, copying only specific files by leveraging the .dockerignore file to exclude unnecessary files.

6. Dockerfile Linter:

* Implemented linting for quality assurance using hadolint.
Command to lint the Dockerfile: docker container run --rm -i hadolint/hadolint hadolint - < Dockerfile.

7. Thorough Testing:

* Conducted thorough testing of both the image and the container to ensure proper functionality. The application runs correctly within the Docker environment.

8. Dockerhub Integration:

* Utilized Dockerhub for image repository.
Verified successful pushing and pulling of the image, ensuring smooth integration with Dockerhub.