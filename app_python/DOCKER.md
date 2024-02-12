In this Docker image, we've implemented several Docker security best practices to ensure a secure and reliable containerized environment:

1. **Non-Root User**: The Docker image runs the application using a non-root user to minimize the risk of privilege escalation attacks.

2. **Minimal Base Image**: We've used an official Python slim image as the base image to keep the image size minimal and reduce the attack surface.

3. **Limited Permissions**: File permissions within the Docker image are set to restrict access to sensitive files and directories, further enhancing security.

4. **Content Trust Enabled**: Docker Content Trust is enabled to ensure that only signed images are pulled and executed on the Docker host, preventing unauthorized or tampered images from being used.

##### Build Docker Image

To build the Docker image locally, follow these steps:

```bash
cd app_python
docker build -t dzendos/app_python .
```

##### Pull Docker Image

If you prefer to pull the Docker image from Docker Hub, you can use the following command:

```bash
docker pull dzendos/app_python
```

##### Run Docker Container

To run the Docker container, use the following command:

```bash
docker run -p 5000:5000 dzendos/app_python
```

After running the container, you can access the application by navigating to `http://localhost:5000` in your web browser.
