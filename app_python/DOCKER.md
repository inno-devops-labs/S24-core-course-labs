# Dockerfile Best Practices Employed in the Project

### 1. Using an Official and Slim Base Image

I selected `python:3.12.2-slim-bookworm` as a base image. The `slim` variant minimizes the image size without sacrificing essential functionality, enhancing deployment speed and security.

### 2. Non-Root User and Explicit User Switching

To enhance security, A non-root user for running the application was created. It diminishes the potential impact of exploits that might target the containerized application.

### 3. Minimizing Layers with RUN Instructions

The `RUN` instructions are combined into a single layer using `&&` to concatenate commands. This approach reduces the image layers, following the best practice of minimizing layers to optimize build performance and image size.

### 4. Leveraging Build Cache with COPY Instructions

I placed `COPY` instructions for requirements.txt before copying the application code. This takes advantage of Docker's build cache: if the requirements.txt file hasn't changed, Docker will reuse the cached layer for the pip install step, speeding up rebuilds of the Docker image.


### 5. Exposing Necessary Ports

The port 5000 was exposed using `EXPOSE`, which is standard for Flask applications. This instruction documents the port on which the application listens, although it doesn't actually publish the port. It is a form of documentation and can be used by runtime for automatic port mapping.

### 6. Specifying a Precise Command

The `CMD` instruction clearly defines the default command to run the Flask application, ensuring the container starts the application correctly upon instantiation. This explicit definition contributes to the maintainability and ease of use of the Docker image.

