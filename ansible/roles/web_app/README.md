# Web App

Deploys simple dockerized web application.

## Requirements

- `docker` role

## Role Variables

1. `web_app_dir` - The directory to put web application files to.
1. `web_app_docker_image` - The docker image reference. If it refers to the
   docker registry, the image should be **publicly** available.
1. `web_app_docker_image_tag` - The tag of the docker image.
1. `web_app_target_port` - The port on which the web application will be
   listening inside the container.
1. `web_app_published_port` - The port on which the web application will be
   published on the host.
1. `web_app_full_wipe` - If set to `true`, the role will remove the Docker
   container and all related files.

For default values, please refer to `defaults/main.yml`.

## Dependencies

- My local `docker` role.

## Example Playbook

```yaml
---
- hosts: all
  roles:
    - role: web_app
      vars:
        web_app_docker_image: "nginx"
        web_app_docker_image_tag: "latest"
        web_app_target_port: 80
        web_app_published_port: 8080
```
