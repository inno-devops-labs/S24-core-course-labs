# Docker Best Practices Report

I implemented several best practices when using Docker for containerization. Below are the practices that I followed:

1. Make executables owned by root and not writable: I made sure that the executables within the containers were owned by the root user and were not writable by other users. This helps to enhance security and prevent unauthorized modifications to the executables.

2. Don’t bind to a specific UID: I avoided binding containers to specific user IDs (UIDs) to avoid potential conflicts and security vulnerabilities. By allowing Docker to assign user IDs dynamically, I ensured better isolation and security within the containers.

3. Rootless containers: I utilized rootless containers to further enhance security and limit the privileges of the containerized applications. Rootless containers provide a more secure environment by running containers with reduced permissions.

4. Use trusted base images: I used trusted base images from official repositories (openjdk:17-jdk-slim) to ensure the reliability and security of the containerized applications. By using well-maintained and updated base images, I reduced the risk of vulnerabilities and security threats in the containers.

5. Distroless, from scratch: I leveraged distroless base images (openjdk:17-jdk-slim). Distroless images contain only the necessary dependencies for the application, making them more lightweight and secure.

6. Exposed ports: I exposed only the necessary ports (only 8080) in the containers to limit potential entry points for attackers. By explicitly specifying the ports that need to be exposed, I minimized the risk of unauthorized access to the containerized applications.

7. By using multi-stage builds in my homework project, I was able to improve the efficiency of the Docker build process and reduce the size of the final Docker image. This practice is highly recommended for anyone looking to optimize their Docker workflow and improve the performance of their containers.