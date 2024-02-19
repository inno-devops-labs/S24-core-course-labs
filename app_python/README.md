## Docker

This application can be containerized using Docker. Follow the instructions below to build, pull, and run the Docker image.

### Requirements

- Rootless container environment
- Docker installed

### Build

To build the Docker image, navigate to the project directory and run the following command:
```docker build -t darverda/app . ```

### Pull
If you prefer to pull the pre-built Docker image from a registry, you can use the following command:
```docker pull darverda/app:latest ```

### Run
To run the Docker container, use the following command:
```docker run -p 5000:5000 --name app darverda/app:latest```