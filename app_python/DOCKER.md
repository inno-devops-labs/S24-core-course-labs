# Best Practices in Dockerfile

1. **Use of Specific Base Image Version**:
   - The Dockerfile specifies `python:3.9-alpine3.18` as the base image, which provides a specific version of Python (3.9) and Alpine Linux (3.18). Using specific versions helps ensure consistency and predictability across builds.

2. **Setting Environment Variables**:
   - `PYTHONDONTWRITEBYTECODE` and `PYTHONUNBUFFERED` environment variables are set to 1, which disables bytecode generation and enables unbuffered output for Python. This is recommended to optimize Python applications in containerized environments.

3. **Creating Non-Root User**:
   - The Dockerfile creates a non-root user `nonroot` and switches to that user. Running containers as a non-root user enhances security by reducing the potential impact of security vulnerabilities.

4. **Working Directory**:
   - The working directory `/app` is set using the `WORKDIR` instruction. This ensures that subsequent commands are executed in the specified directory, improving readability and maintainability.

5. **Changing Ownership of Working Directory**:
   - The ownership of the working directory is changed to the non-root user `nonroot`. This ensures that the user has appropriate permissions to write to the directory, maintaining security and avoiding permission issues.

6. **Copying Specific Files**:
   - Only the necessary files (`requirements.txt` and `app.py`) are copied into the container. This minimizes the size of the Docker image and improves build performance by reducing unnecessary file copying.

7. **Installing Dependencies**:
   - Dependencies specified in `requirements.txt` are installed using `pip install`. Using `--no-cache-dir` ensures that no cache is used during the installation process, reducing the size of the Docker image and avoiding potential caching issues.

8. **Exposing Ports**:
   - Port 5000 is exposed using the `EXPOSE` instruction. Although this is not strictly necessary for container communication, it documents the intended port usage and provides clarity for users.

9. **Defining Command to Run Application**:
   - The `CMD` instruction specifies the command (`python app.py`) to run the application when the container starts. This defines the default behavior of the container and ensures that the application is executed automatically.
