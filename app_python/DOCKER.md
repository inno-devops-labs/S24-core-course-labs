# Docker Best Practices Documentation

## Dockerfile Explanation

### 1. **Use a Minimal Base Image**

   - We based our Docker image on `python:3.9.18-slim-bullseye` to keep the image size minimal.
   - A smaller image reduces the attack surface and improves deployment speed.

### 2. **Avoid Running as Root**

   - Created a non-root user (`myuser`) to run the application.
   - Reducing privileges enhances security by adhering to the principle of least privilege.

### 3. **Copy Application Files**

   - Copied only necessary files into the image, optimizing the build process.
   - Utilized `COPY` instead of `ADD` for explicitness and predictability.

### 4. **Expose Required Port**

   - Explicitly exposed the required port (`5000`) to document the port the application listens on.

### 5. **Define Entry Point**

   - Set the entry point to run the Python application (`app.py`) when the container starts.
   - Clearly defined the default behavior of the container.

### 6. Build Context and Dockerignore

   - Carefully managed the build context and use a .dockerignore file to exclude unnecessary files.

### 7. Metadata Labels

   - Metadata labels are included for image management, providing information like application version and maintainer contact.