#### Ansible Role: Docker

This Ansible Role is used to install Docker on Linux systems.

## Role Variables

- **docker_edition**: Specifies the edition of Docker to install. Use 'ce' for Community Edition or 'ee' for Enterprise Edition.
- **docker_service_manage, docker_service_state, docker_service_enabled, docker_restart_handler_state**: Specify various service options for Docker.
- **docker_install_compose_plugin, docker_compose_package, docker-compose-plugin, docker_compose_package_state**: Define options for the Docker Compose Plugin.
- **docker_install_compose, docker_compose_version, docker_compose_arch, docker_compose_url, docker_compose_path**: Specify options for Docker Compose.

## Example Playbook

```
---
- name: setup Docker
  hosts: all
  become: true
  roles:
    - docker
```