# Best Practices in Dockerfile

1. **Slim version of python image**
I used `python:3.11.1-slim`

2. **Rootless container**
More secured and stable image.

3. **Layer sanity**
I've tried to merge different commands as much as possible.

4. **Layer ordering**
Rarely changable things should go first.

5. **COPY only specific files**

6. **Use .dockerignore**

