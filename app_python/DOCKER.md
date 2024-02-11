## Docker Best Practises

1. No Root User:
   To enhance security, the Docker container runs with a non-root user instead of the root user.

2. Layer Optimization:
   Multiple commands are combined into a single `RUN` instruction to minimize the number of layers in the Docker image.
   This optimizes the build process and reduces the overall image size.

3. Use of .dockerignore:
   A `.dockerignore` file is utilized to exclude unnecessary files and directories from being copied into the Docker
   image. This ensures that only essential files required for running the application are included, reducing the image
   size and build time.

4. Container Cleanup:
   Unnecessary dependencies and files are removed within the container to minimize its size and reduce the attack
   surface. This includes removing temporary files generated during the build process and any unused dependencies.

5. Image Tagging:
   Docker images are tagged with meaningful version numbers or labels to ensure traceability and facilitate easy
   rollback in case of issues. Tags provide a way to identify specific versions of the application and maintain
   consistency across different environments.