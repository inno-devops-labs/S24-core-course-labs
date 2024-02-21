## Docker Best Practices:

### 1. Use Official Base Images:
- I've used the official Python image from Docker Hub (`python:3.9-slim`) as the base image for our application.

### 2. Minimize Image Layers:
- I've combined multiple operations into a single `RUN` instruction.

### 3. Explicitly Define Versions in Dependencies:
- I've pinned version numbers for Python dependencies in the `requirements.txt` file 

### 4. Use `.dockerignore` File:
- I've crafted `.dockerignore` file.

### 5. Set Working Directory:
- I've set the working directory to `/app_python` inside the container.

### 6. Expose Necessary Ports:
- I've specified port 5000.

### 7. Clean Up After Dependencies Installation:
- I've cleaned the installation cache by using the `--no-cache-dir` option in the `pip install` command.

### 8. Implement Security Measures:
- Non-root user.
