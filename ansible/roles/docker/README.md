# Ansible Role: Docker

An Ansible Role that installs Docker on Linux.

## Role Variables:
 
- Specifies the Docker edition to install ('ce' for Community Edition or 'ee' for Enterprise Edition): **docker_edition**
- Specifies service options: **docker_service_manage, docker_service_state, docker_service_enabled, docker_restart_handler_state**
- Specifies Docker Compose Plugin options: **docker_install_compose_plugin, docker_compose_package, docker-compose-plugin, docker_compose_package_state**
- Specifies Docker Compose options: **docker_install_compose, docker_compose_version, docker_compose_arch, docker_compose_url, docker_compose_path**

## Example Playbook

```yaml
- hosts: all
  roles:
    - docker
```

