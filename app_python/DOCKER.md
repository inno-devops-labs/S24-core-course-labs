# Implemented Dockerfile best practices

+ This image is rootless. Application is run under `app` user
+ This image is not bound to specific UID
+ Python files are owned by root and not writable
+ This image uses trusted base image
+ This image uses COPY
+ This image uses dockerignore
