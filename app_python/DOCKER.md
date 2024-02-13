# Reasoning behind usage of Docker

## Practices used

1. The container is rootless - we create low-privilege user in DockerFile
2. .dockerignore file to exclude not-needed files
3. Dependencies and the app are separated in Dockerfile to better use Docker caching
4. Usage of specific (by version number) stable python base image
5. Re-using main app's requirements.txt
6. Layer sanity - commands are grouped together as much as possible (like user/group creation), and are ordered in a way to provide optimal caching
