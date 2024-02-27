```markdown
## Docker Best Practices

### No Root User
We created a non-root user in the Dockerfile to enhance the security of the container. Running processes as a non-root user reduces the risk of privilege escalation attacks.

### .dockerignore
We used a .dockerignore file to exclude unnecessary files and directories from the Docker build context. This helps reduce the size of the Docker image and improves build performance.
```
