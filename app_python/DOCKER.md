# Dockerfile Best Practices

### 1. Specify a Working Directory

WORKDIR /app is used to set the working directory within the container. This ensures that subsequent commands are executed relative to this directory. It's a good practice for organization and clarity.

### 2. Create and Use a Non-Root User

Creating a non-root user with limited permissions is a security best practice. This reduces the potential impact of security vulnerabilities within the container. `RUN adduser -D testUser && chown -R testUser /app` creates a user named `testUser` and assigns ownership of the working directory to this user.

### 3. Use COPY Instead of ADD

Copying files into the container is done using COPY rather than ADD. While both commands serve a similar purpose, COPY is preferred as it's more explicit and less prone to unexpected behavior.

### 4. Install Dependencies Before Copying Application Code

By copying and installing dependencies (requirements.txt) separately, Docker can cache the dependency installation step. This allows for faster builds when the application code hasn't changed, as Docker can reuse the cached layers.

### 5. Expose Required Ports

`EXPOSE 5000` documents that the container will listen on port 5000 at runtime. This doesn't actually publish the port, but it's a good practice to declare the ports your container listens on for better clarity.

### 6. Use CMD for Defining Default Command

`CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=5000"]` specifies the default command to run when the container starts. This launches the Flask application with the specified host and port. Using CMD instead of ENTRYPOINT allows users to override the command easily if needed.