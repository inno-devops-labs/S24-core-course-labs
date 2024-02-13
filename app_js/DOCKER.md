# Docker Best Practices for App_Python

This document elaborates on the Docker best practices employed in the Dockerfile for the NodeJs-based web application. These practices are aimed at optimizing the build process, ensuring security, and enhancing the overall efficiency of the container.

## Utilizing an Official, Lightweight Base Image

```bash
FROM node:14-alpine
```
**Practice** : Choosing an official NodeJs image ensures a reliable and secure foundation. The slim variant minimizes the footprint of the image, reducing potential attack surfaces and speeding up build and deployment times.

## Working Directory
```bash
WORKDIR /app_js
```
**Practice** : Setting a specific working directory (/app_python) within the container provides a clear, consistent location for the application code, simplifying navigation and command execution within the container.

## Copying Only Necessary Files
```bash
COPY package.json package-lock.json app.js ./
COPY views/ ./views/
```
**Practice** : By selectively copying only the files necessary for the application to run (requirements.txt, app.py, and the templates directory), we minimize the image size and reduce build time. This approach also limits the potential inclusion of sensitive files or unnecessary data in the image.

## Non-Root User
```bash
RUN adduser --disabled-password appuser && \
    chown -R appuser:appuser /app_js
USER appuser
```
**Practice** : Running the application as a non-root user (appuser) significantly enhances the security of the container by restricting the privileges of potential attackers, thus adhering to the principle of least privilege.

## Exposing Only Necessary Port
```bash
EXPOSE 3000
```
**Practice** :Exposing only the necessary port (3000) for the Flask application follows the security best practice of minimizing the container's attack surface. It also provides clear documentation about which port the container expects to communicate on.
## Clean, Specific Startup Command
```bash
CMD [ "node", "app.js" ]
```
**Practice** : A clear and specific command to start the NodeJs application ensures that the container runs predictably and is easily debuggable. Using the array syntax for CMD ensures that the command is executed without a shell, which is both more secure and allows signals like SIGTERM to be directly received by the process.
 
