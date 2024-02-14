## Docker Best Practices
1. Non-Root User:  
   - Creating a non-root user in the Dockerfile limits security vulnerabilities by restricting process privileges.

2. Working Directory:  
   - Setting the working directory to /app organizes and isolates application files within the container.

3. Non-Privileged Port:  
   - Running the application on a non-privileged port (above 1024) avoids needing higher permissions.

4. Minimal Base Image:  
   - The image uses python:3.11.5-alpine3.18, a minimal base image suitable for Python applications.

5. Copying Application Files:  
   - Copying application files with COPY reduces attack surface by including only necessary files, keeping the image size minimal.
