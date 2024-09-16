## Best Docker Practices

1. **Use Official Base Images**: 
    - Always use official base images from trusted sources like Docker Hub. In this case, `python:3.11-slim` is used.

2. **Reduce Layers with &&**: 
    - Combine commands using `&&` to reduce the number of layers created in the Docker image. This helps in reducing the image size and improves build performance.

3. **Create a Non-Root User**: 
    - Create a non-root user to run the application. This enhances security by minimizing the impact of potential security vulnerabilities.

4. **Set Working Directory**: 
    - Set a working directory using `WORKDIR` instruction to ensure all subsequent commands are executed from this directory.

5. **Copy Specific Files Before Installing Dependencies**: 
    - Copy only necessary files into the image before installing dependencies. This helps utilize Docker's layer caching mechanism efficiently.

6. **Use ENV to Modify PATH**: 
    - Modify the `PATH` environment variable using `ENV` instruction to include user-specific binary directories.

7. **Use HEALTHCHECK Instruction**: 
    - Implement a health check to monitor the container's health status. In this case, a custom health check is performed to ensure the application is responsive on port 5000.

8. **Specify CMD Instruction**: 
    - Specify the default command to run when the container starts using the `CMD` instruction. This provides clarity on how to start the application within the container.

9. **Expose Required Ports**: 
    - Use the `EXPOSE` instruction to document which ports the container listens on. This does not actually publish the port, but serves as documentation for users of the image.

10. **Use .dockerignore**: 
    - Utilize a `.dockerignore` file to specify files and directories to be excluded from the build context. This ensures that only relevant files are sent to the Docker daemon, reducing build times and minimizing the size of the final image.
