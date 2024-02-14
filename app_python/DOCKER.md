### Best Practices Employed in Dockerfile:

1. **Specific Version Tag for Python Image**:
   - Used a specific version tag (`3.12.2-alpine3.19`) for the Python base image to ensure consistency and reproducibility across builds. This helps avoid unexpected changes due to updates in newer versions.

2. **Multi-Stage Builds**:
   - Employed multi-stage builds to reduce the final image size and improve build efficiency. This involves using separate build stages to compile dependencies and then copying only necessary artifacts into the final image, resulting in a smaller and more optimized production image.

3. **Minimize Image Layers**:
   - Combined multiple `RUN` commands into a single one to minimize the number of layers created in the final image. This practice helps reduce the image size and improves build performance by reducing the overhead of managing multiple layers.

4. **Specific File Copying**:
   - Utilized specific file copying instead of copying the entire directory (`COPY requirements.txt .`) to reduce the build context and minimize the chances of including unnecessary files in the final image. This helps keep the image size small and ensures that only essential files are included.

5. **Cleanup after Dependency Installation**:
   - Removed unnecessary files and cache after installing dependencies (`pip install`) to reduce the final image size. This cleanup step helps eliminate unused files and cache, resulting in a more streamlined and efficient image.

6. **Set Non-Root User**:
   - Created and set a non-root user (`myuser`) within the container for improved security. Running the container as a non-root user helps mitigate potential security risks by minimizing the privileges available to potential attackers, thereby enhancing the overall security posture of the containerized application.
