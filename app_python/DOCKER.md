# Docker

Best practices:

1. Using multi-stage builds: The Dockerfile utilizes a multi-stage build by specifying a base image with the desired Python version and slim variant. This helps reduce the final image size by discarding unnecessary build dependencies.

2. Setting environment variables: The Dockerfile sets environment variables `PYTHONDONTWRITEBYTECODE` and `PYTHONUNBUFFERED` to optimize Python's behavior within the container by preventing writing .pyc files and buffering stdout/stderr.

3. Creating a non-privileged user: The Dockerfile creates a non-privileged user appuser with a specific UID to enhance security and avoid running the application as root, following best practices for container security.

4. Dependency caching: Dependencies are downloaded in a separate step to take advantage of Docker's layer caching mechanism. By using cache mounts for pip cache and bind mounts for requirements.txt, subsequent builds can be faster as long as the dependencies have not changed.
