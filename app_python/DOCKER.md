# Docker

___

## Best practices used

1. Multi-stage build. Dockerfile utilizing predefined base image that already has installed python with requirements.
2. Python version. We avoid to use alpine linux in our image to make build faster on python. (Check problems with
   alphine and python)
3. Security. Dockerfile creates non-privileged user with UID and GUID predefined to avoid security issues.
4. `COPY` instead of `ADD` command. `COPY` is more explicit.
5. I tried to reduce number of `RUN` instructions to avoid number of layers in the end docker image.
6. `.dockerignore` file. I've used it to exclude unnecessary files in the end image.