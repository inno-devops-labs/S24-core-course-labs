## Docker Best Practices

### Using non-root user

As recommended in [Docker Security Best Practices](https://sysdig.com/blog/dockerfile-best-practices/), there is a new user created in the docker image, and no root user is used there for extra security.

### Layer sanity

Copying and installing requirements is a process that can be easily cached. Thus, it is isolated from the other commands.

### Specific version of python is used

More precisely, python:3.8-slim is being used in the image.

### Explicit copies

Each directory is copied explictly with no wildcards.