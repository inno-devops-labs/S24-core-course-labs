# Docker Best Practices

## Using a Specific Base Image Version

```dockerfile
FROM python:3.9.2-slim
```

Specifying a precise version of the base image (`python:3.9.2-slim`) instead of using tags like `latest` ensures
reproducibility and consistency across different environments. It helps avoid unexpected behavior caused by updates in
the base image.

## Rootless container

```dockerfile
RUN useradd -m myuser
USER myuser
```

Running the container as a non-root user (rootless) enhances security. If attackers compromise the container, their
ability to escalate privileges and exploit the host system is significantly limited.

## Layer sanity

```dockerfile
COPY --chown=myuser:myuser requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY --chown=myuser:myuser ./templates ./templates
COPY --chown=myuser:myuser app.py PYTHON.md README.md ./
```

By copying only the `requirements.txt` file and running `pip install` before copying the rest of the application files,
we take advantage of Docker's cache mechanism. If the `requirements.txt` file hasn't changed since the last build,
Docker can reuse the cached layer for the `pip install` step, speeding up the build process. Copying files with specific
ownership (`--chown=myuser:myuser`) also adheres to the principle of running as a non-root user.

## Explicitly Exposing Ports

```dockerfile
EXPOSE 8000
```

This documents which ports the application listens on and is useful for someone running the container to understand how
to map ports on their host system to the container.

## Setting environment variables

```dockerfile
ENV NAME World
```

Environment variables are a common way to configure Docker containers. They can be used by the application to modify its
behavior in different environments without changing the code.