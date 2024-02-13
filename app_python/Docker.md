# Docker Best Practices

## User Privileges

The Dockerfile employs best practices by avoiding the use of the root user within the container. Instead, a non-root user named `myuser` is created for running the application. This practice enhances security by minimizing potential risks associated with running processes as the root user.

```dockerfile
# Create a non-root user for running the application
RUN adduser -D myuser
USER myuser
```

## File Ownership

The `COPY` instruction is used with the `--chown` option to set the ownership of the copied files to the non-root user (`myuser`). This ensures that the application files and directories within the container are owned by a less privileged user.

```dockerfile
COPY --chown=myuser:myuser app.py requirements.txt /app_python/
COPY --chown=myuser:myuser templates /app_python/templates
```