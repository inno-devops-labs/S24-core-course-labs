# Docker Best Practices

## Multi-Stage Builds
We utilize multi-stage builds to separate the build phase from the runtime environment. This results in a smaller final image size and prevents unnecessary build tools from being included in the production image.

## Non-Root User
To enhance security, we create a non-root user (`myuser`) and switch to it for running the application. Running containers as root is a security risk and should be avoided.

## Minimal Base Image
We use the slim version of the Node alpine image (`node:14-alpine`) to keep the image size small.

## Specific Copy Commands
Only the necessary files are copied into the container. This includes the compiled JavaScript files and the `package*.json` files.

## Caching Optimization
Dependencies are installed before copying the application code, which allows Docker to cache the layer with the installed packages. This means that if the `package*.json` files haven't changed, Docker won't reinstall the packages every time the image is built.

## Exposing Ports
The application's port is explicitly exposed using the `EXPOSE` directive. This informs Docker that the container listens on the specified network port at runtime.
