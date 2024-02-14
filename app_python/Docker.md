# Docker Best Practices

1. Targeted File Transfers
The `COPY` instruction is utilized to transfer the `requirements.txt` file into the Docker container prior to executing the dependency installation. This approach guarantees that the dependencies are installed in accordance with the versions listed in the `requirements.txt` file.

2. User Privileges
For increased security, a non-root `appuser` is established and assigned to execute the application. This strategy reduces the risk of security breaches linked to the use of the root user within the container environment.

3. Exact Base Image Version
The Dockerfile specifies a fixed version of the Python alpine image `python:3-alpine3.15`, ensuring consistent deployments and reducing the chance of unexpected changes in behavior due to updates in the base image.

4. Port Accessibility
The application's port is declared open using the `EXPOSE` command, signaling Docker that the container is intended to accept connections on the specified port during runtime.

5. Application Initialization
The `CMD` instruction is leveraged to initiate the Flask application. By defining the startup command in this format, the application will automatically begin upon the container's execution.

6. Docker Ignore
Ignores the irrelevant files