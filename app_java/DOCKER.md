## Best practices used
1. **Multi-stage build**:
   - The Dockerfile is divided into multiple stages (`FROM` statements), which is a best practice to optimize image size and reduce security risks by separating build-time dependencies from runtime dependencies.
   - Stage 1 (`build` stage) uses the Maven Docker image as a base to build the application. This stage is responsible for compiling and packaging the application code.
   - Stage 2 (`openjdk` stage) uses the OpenJDK Docker image as a base to create the final image. This stage copies only the necessary artifacts from the previous stage (`build`) and sets up the runtime environment.

2. **Optimized layers**:
   - The `COPY . .` command in the first stage copies the entire context to the Docker build directory (`/app`). This ensures that only necessary files are copied, avoiding unnecessary layers in the image.

3. **Use of specific base images**:
   - Specific versions of base images (`maven:3.8.4` and `openjdk:17-jdk-slim`) are used instead of generic ones. This ensures reproducibility and consistency across builds.

4. **Minimal base image**:
   - The `openjdk:17-jdk-slim` image is chosen as the base image for the final stage. This image provides a minimal runtime environment, reducing the size of the final Docker image.

5. **Non-privileged user**:
   - A non-privileged user `springuser` is created in the final stage (`openjdk` stage) using the `adduser` command. This follows the principle of least privilege, enhancing security by running the application as a non-root user.

6. **Exposing ports**:
   - The `EXPOSE` instruction exposes port 8080, indicating that the container will listen on this port at runtime.

7. **Setting ownership**:
    - Before switching to the non-privileged user (`springuser`), ownership of the `/app` directory is changed to `springuser:springuser`, ensuring that the user has appropriate permissions to access application files.
