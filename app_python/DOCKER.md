# Docker Best Practices

[![Python CI](https://github.com/zeyadAjamy/S24-core-course-labs/actions/workflows/python-ci.yaml/badge.svg?branch=lab3)](https://github.com/zeyadAjamy/S24-core-course-labs/actions/workflows/python-ci.yaml)

1. **Use a specific Python version as the base image**: By specifying the exact Python version (`python:3.9.18-bullseye`), we ensure consistency and reproducibility in our environment. This helps avoid unexpected behavior due to version differences.

2. **Create a non-root user**: Creating a non-root user (`appuser`) enhances security by minimizing the potential impact of security vulnerabilities or malicious attacks. It follows the principle of least privilege, where the application runs with only the necessary permissions.

3. **Switch to the non-root user**: Switching to the `appuser` after creating it further restricts the privileges of the containerized application, reducing the risk of unauthorized access or malicious actions.

4. **Set the working directory and assign ownership to the non-root user**: Setting the working directory (`/app`) and assigning ownership to the `appuser` ensures that subsequent commands executed in the Dockerfile operate within the appropriate context and with the correct permissions.

5. **Copy only the requirements file to avoid unnecessary files in the build context**: Copying only the `requirements.txt` file reduces the size of the build context, improving build performance and reducing the risk of inadvertently including sensitive or unnecessary files in the Docker image.

6. **Install the required packages as the non-root user**: Installing required packages (`requirements.txt`) as the `appuser` prevents potential security risks associated with running package installation commands as the root user. Using `--mount=type=cache` for pip caching optimizes the build process by caching dependencies, improving build speed and efficiency.

7. **Copy the application files**: Copying the application files (`app.py`) into the Docker image ensures that the necessary code is available for execution within the container.

8. **Set a build argument for the port**: Setting a build argument (`PORT`) for the port number allows flexibility in specifying the port at build time. This enables customization without modifying the Dockerfile directly, enhancing portability and ease of deployment.

9. **Expose the port**: Exposing the port (`$PORT`) in the Dockerfile documents the port that the containerized application listens on. This information is useful for users when running the container and for orchestrating services that interact with the container.

10. **Specify the command to run the Flask application**: Specifying the command (`CMD`) to run the Flask application (`python app.py`) ensures that the container starts the application as the default behavior. This simplifies container execution and makes it easier for users to run the application without specifying additional parameters.
