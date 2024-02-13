# Docker Best Practices

- Use a specific Python version: The base image is python:3.9, which specifies the Python version explicitly. It's a good practice to use a specific version rather than a generic version like python:latest to ensure consistent behavior across different environments.

- Create a non-root user: The useradd command creates a non-root user named app. Running the container with a non-root user helps improve security by reducing the potential impact of vulnerabilities.

- Set the user's PATH: The `ENV PATH /home/app/.local/bin:${PATH}` statement adds the user's local bin directory to the `PATH` environment variable. This allows the user to easily run any installed executables.

- Set the working directory: The `WORKDIR /app` statement sets the working directory inside the container to /app. This is where subsequent commands will be executed, unless specified otherwise.

- Copy the application code: Although `ADD` and `COPY` are functionally similar, generally speaking, `COPY` is preferred.`
