# Docker Description

## Dockerfile

This Dockerfile is crafted using `python:3.9.18-alpine3.18` as its base image to ensure a lightweight and secure deployment environment. The application resides within the `/app/app_python` directory, leveraging `uvicorn` for the Web Server Gateway Interface (WSGI) service.

## .dockerignore

To prevent the inclusion of the virtual environment into the Docker image, a `.dockerignore` file is utilized.

## Basic Best Practices followed

- A specific version of the base image is specified to maintain build consistency.
- Security measures were implemented to minimize potential vulnerabilities.
- Efforts were made to minimize the image size by opting for an Alpine-based image.
- The Dockerfile includes metadata and was checked with a linter for adherence to best practices.

### Security Measures
- Execution is performed under a non-root user account.
- The designated user (`myuser`) possesses restricted access, limited to the `/app/app_python` directory and its home directory.
- Official `python:3.9.18-alpine3.18` image was used as the base image
- Python executables are installed in the user's local bin directory, which is included in the `PATH`.
- The `latest` tag is used when publishing the image to prevent the accidental deployment of outdated versions.
- No credentials were included in the application and Dockerfile
- No ports were exposed in the Dockerfile

### Image Size
- `--no-cache-dir` flag was used to avoid caching the downloaded packages for `pip`
- The image is kept small by using the `alpine` version
- Multiple `RUN` commands were combined to reduce the number of layers
- Only important files were COPIED to the working directory


### Other Best Practices

- `LABEL` was used to add metadata to the image
- Less used commands were used earlier in the Dockerfile to take advantage of Docker's layer caching.
  In example, `requirements.txt` was copied first and installed before copying the other files.