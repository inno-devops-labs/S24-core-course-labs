## Dockerfile Best Practices

### 1. Specific Base Image Usage
- The Dockerfile utilizes a specific version of the Python Alpine image (`python:alpine3.19@sha256:849ed6079c9f797ca9c1b7d6aea1c00aea3ac35110cbd0d6003f15950017ea8d`). This ensures consistency and reliability in the build process, avoiding potential issues stemming from updates to the base image.

### 2. Setting Working Directory
- By employing the `WORKDIR` instruction, the Dockerfile establishes the working directory within the container as `/app`. This enhances file organization and simplifies subsequent commands.

### 3. Non-root User Creation
- The Dockerfile creates a non-root user named `myuser` using the `adduser` command. This practice enhances security by minimizing the potential impact of security vulnerabilities. Additionally, ownership of the `/app/app_python` directory is assigned to `myuser` using `chown`.

### 4. Managing Dependencies
- The Dockerfile copies the `requirements.txt` file into the container's `/app/app_python` directory to better manage dependencies. This approach facilitates efficient caching and dependency resolution. Dependencies are installed using `pip install -r ./app_python/requirements.txt --no-cache-dir --user` with options to prevent caching of downloaded packages and to install them in the user's local directory.

### 5. Application File Copying
- Only relevant application files are copied into the container. This includes the Flask application code, ensuring that all necessary components are present within the container.

### 6. Port Exposure
- The Dockerfile exposes port 5000, the standard port for Flask applications to serve HTTP requests. This allows external access to the application running within the container.

### 7. Labeling for Metadata
- Labels are added to the Docker image to provide metadata. This includes the maintainer's email address (`maintainer="c.ogbonna@innopolis.university"`) and a brief description of the image's purpose (`description="Docker image for Flask app."`).

### 8. Default Command Definition
- The `CMD` instruction specifies the default command to execute when the container starts. In this case, it runs the Flask application by executing `python3 app/routes.py`.

### 9. .dockerignore
- The project uses a `.dockerignore` file to exclude certain files and directories from being copied into the Docker image.