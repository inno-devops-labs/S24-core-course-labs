In this Docker image, we've implemented several Docker security best practices to ensure a secure and reliable containerized environment:

1. **Non-Root User**: The Docker image runs the application using a non-root user to minimize the risk of privilege escalation attacks.

2. **Limited Permissions**: File permissions within the Docker image are set to restrict access to sensitive files and directories, further enhancing security.

3. **Content Trust Enabled**: Docker Content Trust is enabled to ensure that only signed images are pulled and executed on the Docker host, preventing unauthorized or tampered images from being used.

4. **Multi-Stage Builds:** Multi-stage builds are employed to separate the build environment from the runtime environment, resulting in smaller and more efficient Docker images.
The final Docker image contains only the necessary artifacts required to run the Go application.

##### Build Docker Image

To build the Docker image locally, follow these steps:

```bash
cd app_golang
docker build -t dzendos/app_golang .
```

##### Pull Docker Image

If you prefer to pull the Docker image from Docker Hub, you can use the following command:

```bash
docker pull dzendos/app_golang
```

##### Run Docker Container

To run the Docker container, use the following command:

```bash
docker run -p 8080:5000 dzendos/app_golang
```

After running the container, you can access the application curl `http://localhost:8080/msk_timezone`.
