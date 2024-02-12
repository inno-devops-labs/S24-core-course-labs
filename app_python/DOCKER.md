## Best Practices for Dockerfile
### 1. Use a Precise Base Image
- Use a precise version of your base image and language, example `python:3-alpine3.15`.
- This ensures that your application is built on a stable and secure base image.
- It also helps to avoid any potential issues that may arise from using the latest version of the base image.
### 2. Use COPY, but Only Specific Files
- Use the `COPY` instruction to copy only the necessary files from your local machine to the Docker image.
- This helps to reduce the size of the Docker image and improve build times.
- It also ensures that only the required files are included in the image, reducing the risk of including sensitive information.
### 3. Use a Non-Root User
- Use a non-root user inside the Docker image to run your application.
- This helps to improve the security of the image by reducing the potential impact of any security vulnerabilities.
- It also follows best practices for running applications in containers.
### 4. Use a `.dockerignore` File
- Create a `.dockerignore` file to specify which files and directories should be excluded from the Docker image.
- This helps to reduce the size of the image and improve build times by excluding unnecessary files.
- It also helps to avoid including sensitive information in the image.
### 5. Exposure of Ports
- Use the `EXPOSE` instruction to specify which ports should be exposed by the Docker image.
- This helps to document which ports are used by the application and allows for easier configuration of port mappings when running the container.
### 6. CMD Instruction
- Use the `CMD` instruction to specify the default command to run when the container is started.
- This helps to ensure that the container starts with the correct command, making it easier to use and reducing the risk of misconfiguration.
- It also provides a clear indication of how the container should be used.
