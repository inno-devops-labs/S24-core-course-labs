# Ansible Role: Web App

An Ansible role for deploying a web application Docker image. This role is responsible for managing the setup of pip, Docker, and Docker Compose on specified hosts. It relies on dependencies from the docker role to ensure proper installation. It proceeds to deploy a docker-compose file, executing the services defined within it. In case the wipe flag is enabled, the role stops any running containers and removes associated images from the host machine.

## Requirements

- Docker
- Python 3.x
- Ansible
- Ubuntu OS

## Example Playbook

```yaml
- hosts: all
  roles:
    - role: web_app
