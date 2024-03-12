# Dockerized Web Application Deployment

This project facilitates the deployment of a basic web application using Docker.

## Role Parameters

1. `web_app_dir` (default: `/opt/web_app`) - Specifies the directory where web application files will be stored.
1. `web_app_docker_image` (default: `nabuki/moscowtime-web:latest`) - Refers to the Docker image for the application. If this references a docker registry, ensure that the image is publicly accessible on Docker Hub.
1. `web_app_full_wipe` (default: false) - If set to `true`, the role will delete the Docker container and all related files.

## Dependencies

- This role relies on the local `docker` role.

## Example Usage

```yaml
- hosts: all
  roles:
    - role: web_app
```