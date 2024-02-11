## Which best practices were applied?
    
1. Using a minimal base image: The Dockerfile uses the Alpine version of the Python 3.9 image, which is a lightweight base image compared to other distributions. This helps reduce the overall image size and improve security.

2. Setting a working directory: The WORKDIR instruction sets the working directory to /app_python, which helps organize the files within the container and makes it easier to manage and run commands.

3. Creating a non-root user: The Dockerfile creates a new_user with limited privileges using the adduser command. Running the container as a non-root user enhances security by reducing the impact of potential security vulnerabilities.

4. Copying only necessary files: The COPY instruction copies only the requirements.txt and app.py files into the container. This approach optimizes the build process by minimizing the number of files copied and improves caching efficiency.

5. Exposing ports explicitly: The EXPOSE instruction exposes port 5000, which documents the ports that the container uses. This helps users understand which ports need to be mapped when running the container.

6. Using pip with –no-cache-dir: The pip install command uses the –no-cache-dir flag to avoid caching downloaded packages in the Docker image. This reduces the image size and ensures that dependencies are always installed from scratch.

7. Defining a default command: The CMD instruction specifies the default command to run when the container starts. In this case, it runs the Flask application with specific host and port settings. This provides a clear entry point for running the application within the container.

Overall, these practices help create a secure, efficient, and maintainable Docker image for running a Python Flask application.

Additionally, an online Docker linter was utilized to validate the Dockerfile against best practices and potential issues. This tool helps ensure that the Dockerfile follows recommended conventions, adheres to security guidelines, and maintains consistency in the Docker image creation process. By using an online Docker linter, potential errors and inefficiencies in the Dockerfile can be identified and corrected early in the development process, leading to a more robust and optimized Docker image.