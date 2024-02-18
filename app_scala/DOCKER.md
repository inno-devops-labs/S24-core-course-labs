
# Docker Best Practices for `app_python`

This document outlines the Docker best practices we have employed in developing the Docker environment for our Scala application. Our Docker setup is split into two stages: a build stage and a final image stage, optimizing for efficiency, security, and performance.

## Multi-Stage Build

We use a multi-stage build process to keep our final image size as small as possible. The build stage uses `sbtscala/scala-sbt:eclipse-temurin-jammy-21.0.2_13_1.9.8_2.13.12` to compile and stage the application, which includes all necessary build tools and dependencies. By separating the build environment from the runtime environment, we reduce the final image size, limiting potential attack vectors and minimizing the footprint.

### Build Stage

- **Non-Root User**: We create a non-root user `user` with `--disabled-login` to enhance security. Running as a non-root user limits potential system compromises.
- **Permissions**: Directories `target/` and `project/target` are created with write permissions to allow the `user` to compile and stage the application without root privileges.

### Final Image

- **Base Image**: The final image is based on `openjdk:22-slim-bullseye`, a slim version of the OpenJDK image, to minimize the attack surface and reduce the size.
- **Non-Root User**: Similar to the build stage, we use a non-root user for running the application, enhancing the security posture of our runtime environment.
- **Minimal Runtime Environment**: Only the necessary files from the build stage are copied into the final image. This step ensures that the runtime environment contains only what is required to run the application, reducing the potential for vulnerabilities.
- **Exposing Ports**: We expose port `9000`, which is standard for web applications, indicating clear documentation and understanding of the application's networking requirements.
- **Runtime Directory**: A directory `/app/run` is created with write permissions for the application to generate a PID file, adhering to best practices for file permissions and application requirements.

## Configuration and Secrets

- **External Configuration**: Application secrets and configurations, such as the Play framework secret key, are passed as envinronment variables

Essential to mention that I didn't used CMD JSON notation intentionally. I failed to substitute secret in JSON notation, so used command notation
