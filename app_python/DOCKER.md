# Best Practices in Dockerfile

1. **Slim Version of Base Image**
Utilizing a slim version of the base image (`python:3.11.1-slim`) ensures a smaller footprint, reducing the attack surface and minimizing the overall size of the Docker image.

2. **Rootless container**
Creating a non-root user within the Dockerfile enhances security. This follows the principle of least privilege, reducing the risks associated with running processes as the root user.

3. **Layer sanity**
By combining multiple commands, such as creating directories (mkdir), setting permissions (chown), and installing dependencies (pip install), into single RUN instructions, it optimizes Docker's layering system. This approach helps to minimize the number of intermediate layers, reducing the final image size and improving build efficiency.

4. **Layer ordering**
Ordering the Dockerfile commands with rarely changeable actions first promotes Docker build caching efficiency. This is more helpful in future builds as chaching system is working.

5. **COPY only specific files**
By explicitly specifying which files to copy into the container using the COPY instruction, unnecessary files and directories are excluded from the Docker build context. This practice helps to minimize the size of the build context and improves build performance.

6. **Use .dockerignore**
File exclusion with .dockerignore helps to avoid irrelevant or sensitive files from the Docker build context. It reduces the size, improving build performance and security by preventing the inclusion of unnecessary or sensitive files in the final image. 

7. **Remove temporary files**
The requirement.txt file is unnecessary after installation of all dependancies, therefore does not needed for further build or run. Removement of such files reduces potential size.
