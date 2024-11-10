# Dockerfile Best Practices

### 1. Use a Minimal Base Image

We use the base image `python:3.9-alpine3.15` to keep the Docker image small and secure. Alpine Linux is a minimalistic distribution, which helps us reduce the overall size of the image while still providing the necessary environment for Python 3.9. Using a precise version (`python:3.9-alpine3.15`) ensures that the image is stable and free of unnecessary bloat.

```dockerfile
FROM python:3.9-alpine
```

### 2. Specify a Working Directory
The `WORKDIR /app` instruction sets the working directory within the container to `/app`. All subsequent commands will be executed from this directory, ensuring that the application files are organized and the working context is clear.

```dockerfile
WORKDIR /app
```

### 3.  Create and Use a Non-Root User
For security purposes, containers should not run as root. The `RUN adduser -D test && chown -R test /app` command creates a non-root user named `test` and grants ownership of the `/app` directory to this user. After this, the container switches to running as the `test` user.

```dockerfile
RUN adduser -D test && chown -R test /app
USER test
```
Running containers as non-root users minimizes potential security risks, making the system less vulnerable to exploits.

### 4. Use COPY Instead of ADD
We use the `COPY` command to copy files from the host into the container. Unlike `ADD`, `COPY` is a more explicit and predictable command. It doesn't automatically extract compressed files or fetch remote URLs, reducing the potential for unexpected behaviors.

```dockerfile
COPY requirements.txt .
```

### 5.  Install Dependencies Before Copying Application Code
The `COPY requirements.txt` . step is followed by the installation of Python dependencies. By separating the dependency installation from copying the rest of the application files, Docker can cache the installation step. This means if `requirements.txt` hasn't changed, Docker will reuse the cached layer, speeding up future builds.

```dockerfile
RUN pip install --no-cache-dir -r requirements.txt
```

### 6. Use CMD for Defining Default Command

Use `CMD` for Defining the Default Command
The CMD instruction defines the default command to run when the container starts. Here, we are using it to start the Flask web server, making the application available on all network interfaces (`0.0.0.0`) and port `5000`. This command can be overridden when running the container if needed.

```dockerfile
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=5000"]
