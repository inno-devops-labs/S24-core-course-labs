# Docker Best Practices for application

This document explains the Docker best practices applied in this project.

### 1. Minimal Base Image

**Base Image**: `python:3.11-slim`

Using a lightweight base image, such as `python:3.11-slim`, reduces the overall size of the Docker image. This minimizes the container's attack surface, speeds up build times, and lowers resource usage. A smaller image is easier to distribute and requires less storage.

### 2. Non-Root User for Security

**Non-root User**: `appuser`

Running processes as the root user inside containers is a security risk, as it can allow for privilege escalation. We create a non-root user, `appuser`, using the `useradd -m appuser` command and switch to this user with the `USER` directive. Assigning application ownership to `appuser` with `chown -R appuser /app` ensures only the application user has access to the application directory, while the rest of the system remains secure.

### 3. Virtual Environment for Dependency Isolation

**Virtual Environment**: `/opt/venv`

To further secure the application, dependencies are installed within a virtual environment located at `/opt/venv`. This isolates application dependencies from the system libraries, reducing potential conflicts and maintaining a clear boundary between system files and application dependencies. 

### 4. No Cache in Pip Install

**No Cache**: `pip install --no-cache-dir`

Adding `--no-cache-dir` to the `pip install` command prevents caching, keeping the final image smaller by excluding unnecessary cache files. This practice is particularly useful when using lightweight images to minimize storage and ensure efficiency.

### 5. Environment Configuration for Production

**Environment Variables**: `PYTHONUNBUFFERED=1`, `FLASK_ENV=production`, and `FLASK_APP=app.py`

- `PYTHONUNBUFFERED=1` prevents Python from buffering output, which improves logging and debugging visibility.
- `FLASK_ENV=production` configures Flask for production, disabling development features that aren’t secure or efficient for live applications.
- `FLASK_APP=app.py` sets the entry point file, ensuring the Flask application runs correctly on startup.