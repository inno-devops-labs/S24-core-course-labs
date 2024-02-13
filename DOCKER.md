## Dockerfile best practices used

1. **Used a minimal base image:** The Dockerfile starts with the `python:3.9-slim` base image, which is a slim version of Python 3.9. This helps keep the final image size small, reducing security risks and improving performance.

2. **Defined a working directory**: The `WORKDIR` instruction sets the working directory to `/app_python`. This ensures that all subsequent commands are executed from this directory, making it easier to manage and reference files within the image.

3. **Copied only necessary files**: The `COPY` instructions are used to copy the `requirements.txt` file and `app_python.py` to the working directory. This approach avoids copying unnecessary files, reducing the build time and image size.

4. **Exposed necessary ports**: The `EXPOSE` instruction exposes port 8000, indicating that the container will listen on this port. This is useful for documenting the intended network connections of the image.

5. **Created non-root user**: Instead of running the container as the root user, the `adduser` command is used to create a user named `foo`. This practice improves security by minimizing the potential impact of any container vulnerabilities.

6. **Used cache for pip installation**: The `pip install --no-cache-dir -r requirements.txt` command installs the Python dependencies listed in `requirements.txt`. By using the `--no-cache-dir` flag, it avoids caching the installed dependencies, leading to a smaller image size.

7. **Set appropriate user permissions**: The `USER foo` instruction sets the user to `foo` before the container starts. This is important for running the container with reduced privileges, enhancing the security and isolating potential container processes.

8. **Defined the default command**: The `CMD` instruction sets the default command to execute when the container starts. In this case, it runs the Python script `app_python.py` with the `runserver` argument, specifying the host as `0.0.0.0`.