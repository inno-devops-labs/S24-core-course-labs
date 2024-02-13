## Docker Best Practices

- Non-root user
- Base image is official `python:3.9-slim` with specific version
- Copying only specific files (I've copied only templates directory, but it's supposed to have only html files)
