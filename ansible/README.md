# Web App Ansible Role

This Ansible role is responsible for deploying a Dockerized web application.

## Requirements

- Ansible 2.0 or later
- Docker installed on the target host(s)

## Role Variables

- `image_name`: Name of the Docker image to deploy
- `image_tag`: Tag of the Docker image
- `ports`: List of ports to publish for the Docker container

## Dependencies

None

## Usage

To use this role, include it in your Ansible playbook like so:

```yaml
- name: Deploy Web App
  hosts: your_target_hosts
  become: yes
  roles:
    - web_app
```

##Tasks

This role consists of the following tasks:

Render docker-compose template: Renders the docker-compose.yml.j2 template to generate the Docker Compose file.
Start Docker: Ensures that the Docker service is started on the target host(s).
Start app service: Uses the community.docker.docker_compose_v2 module to start the Docker container for the web application.
Wipe Docker container: Imports the wipe tasks from tasks/0-wipe.yml to remove the Docker container and all related files if web_app_full_wipe variable is set to true.

##License

This role is licensed under the MIT License. See the LICENSE file for details.
