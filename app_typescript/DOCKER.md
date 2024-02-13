# Docker Best Practices
- Docker image was built in rootless mode
- Docker image uses stable, reliable and trusted base image with specific hash
- Haskell Dockerfile Linter (hadolint) is used to detect bad practices (with gh action)
- GH Action is being run to automatically upload image to Docker Hub after linting
