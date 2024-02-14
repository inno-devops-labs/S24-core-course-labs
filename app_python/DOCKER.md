# Best Practices Employed in Dockerfile:

1. **Specific Version Tag for Python Image**:
   - Used a specific version tag (`3.12.2-alpine3.19`) for the Python base image to ensure consistency and reproducibility across builds. This helps avoid unexpected changes due to updates in newer versions.

2. **Minimize Image Layers**:
   - Combined multiple `RUN` commands into a single one to minimize the number of layers created in the final image. This practice helps reduce the image size and improves build performance by reducing the overhead of managing multiple layers.

3. **Specific File Copying**:
   - Utilized specific file copying instead of copying the entire directory (`COPY requirements.txt .`) to reduce the build context and minimize the chances of including unnecessary files in the final image. This helps keep the image size small and ensures that only essential files are included.

4. **Cleanup after Dependency Installation**:
- Removed unnecessary files and cache after installing dependencies (`pip install`) to reduce the final image size. This cleanup step helps eliminate unused files and cache, resulting in a more streamlined and efficient image.

5. **Rootless Containers**
- ***Used non-root users***: Whenever possible, run your containers with non-root users. This reduces the potential attack surface and limits the damage that can be done if a security vulnerability is exploited.

6. **Use COPY, but only specific files**
- ***Used COPY instead of ADD***: COPY is preferred over ADD as it is more transparent and has fewer capabilities, reducing the risk of inadvertently introducing security vulnerabilities.
- ***Copy only necessary files***: Only copy the files that are required for the application to run. Avoid copying unnecessary files, especially sensitive ones, to minimize the risk of exposing sensitive information.

7. **Layer Sanity**
- ***Minimized layers***: Reduce the number of layers in your Docker image to minimize the attack surface and simplify image management.
- ***Combined RUN commands***: Combine multiple RUN commands into a single command to minimize the number of layers created during the image build process.
