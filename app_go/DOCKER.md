# Dockerfile for `app_go`

## Best practices employed

-   Explicit base image tag version.

-   An alpine base image is used, so as to reduce the resulting image
    size.

-   .dockerignore is used and is symlinked to .gitignore. What's not to
    appear in the repo is also not to be included in the image.

-   Run instructions in the dockerfile are in the exec form, not shell
    form.

-   A multi-stage build is used. The final stage consists of just two
    layers and takes up about 8MB.

-   Root owns the executable file, which is not to be modified.

-   A non-root user executes the app.

-   The port to be exposed is explicitly mentioned in the Dockerfile.

Not sure what else to say, but just look at it: it's almost perfect!

The only thing one can argue about is the use of a hardcoded UID in the
Dockerfile. But, firstly, there is no native way to add a user in a bare
image, secondly, there is nothing to exchange with between host and container,
so there's no reason to.
