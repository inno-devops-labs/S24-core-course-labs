# Docker best practices & instructions

## Best practices applied

- Entrypoint is not ran as root
- Code is owned by root and not writable by ```app``` user
- Base image is official alpine-based python: reduces attack surface
- ```COPY``` only used on specific files, not directories
- Dockerfile linter is installed in pre-commit scripts
- Includes a healthcheck

## Building and running
1. Acquire the image
    1. Pull the image from docker hub:
    ```bash
    docker pull n0m1nd/moscow_time_python:0.1.2
    ```

    2. Alternatively: Clone this repository to your machine and build the image
    ```bash
    git clone https://github.com/geffk2/S24-core-course-labs.git -b lab1
    cd S24-core-course-labs
    docker build -t n0m1nd/moscow_time_python app_python
    ```

3. Run the container:
```bash
docker run -d -p 8080:8080 n0m1nd/moscow_time_python
```

4. Ensure the container is healty:
```console
foo@bar ~$ docker ps
. . .
yyyy...    xxx       "python3 -m server"   n minutes ago   Up n minutes (healthy)   0.0.0.0:8080->8080/tcp   . . .
```
