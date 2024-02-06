# Docker

I have created `Dockerfile` and built docker image for this application.

## Best Practices

I have applied the following [Docker Best Practices](https://docs.docker.com/develop/develop-images/instructions/)

### Avoid Unnecessary privileges
To avoid unnecessary privileges, I've created user `ramprin` in order to run container without privileges.
All executables are owned by root and not writable. 
### Reduce Attack Surface
I've used multistage building with official [golang image](https://hub.docker.com/_/golang) from developers. There is only one port exposed.
### Prevent Confidential Data Leaks
These applications do not work with confidential data. Thus there are no possible data leaks.
I used `.dockerignore` in order to avoid copying unnecessary files and build from the `app_python` directory.
### Others
I tried to minimize the amount of layers. Also added some labels and used [Dockerfile Linter](https://hadolint.github.io/hadolint/) to check
Dockerfile correctness.