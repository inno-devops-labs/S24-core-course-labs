# Reasoning behind usage of Docker

## Practices used

For the extensive list, see `../app_python/DOCKER.md`

In addition, in this app, multi-stage builds are used (one for building and one for running).

Also, in the built image, swagger is disabled for safety reasons - the environment is no longer Development.
