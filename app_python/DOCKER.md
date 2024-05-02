# Dockerfile for `app_python`

## Best practices employed

-   Explicit base image tag version.

-   An alpine base image is used, so as to reduce the resulting image
    size.

-   .dockerignore is used and is symlinked to .gitignore. What's not to
    appear in the repo is also not to be included in the image.

-   Static build commands are early in the Dockerfile so that changes
    to the project do not require those steps rebuild.

-   Run instructions in the dockerfile are in the exec form, not shell
    form.

-   Root owns project files that are not supposed to be modifiable.

-   A non-root user installs dependencies and runs the project.

-   The port to be exposed is explicitly mentioned in the Dockerfile.

Not sure what else to say, but just look at it: it's almost perfect!

There is just one trade-off: one could have reduced the build time by first
copying requirements and installing dependencies, then copying project files
and doing the rest: requirements are less likely to change than the source code.
However, this would increase the number of layers due to two distinct COPY
operations, which is likely a higher priority than build time (not to mention
complications of the Dockerfile, which would require at least 3 user switchings
if one wants to keep that libraries are installed for user, project files are
owned by root and the application is run by user).
