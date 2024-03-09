# Web App Deployment Ansible Role
This role deploys a web app using Docker.

## Requirements
- Ubuntu 18.04 or later VM.
- `docker` role

## Role Variables
- `web_app_app_dir`: The directory where the web app is located.
- `web_app_image`: The name of the Docker image to use.
- `web_app_ports`: The port to expose the web app on.
- `web_app_full_wipe`: Whether to remove the app directory and docker-compose file before deploying.
- `web_app_docker_ansible_user`: The user to run the docker commands as.

## Dependencies
- `docker` role

## Example Playbook
```yaml
- name: Deploy Python App
  hosts: vms
  become: true
  roles:
    - role: web_app
      vars:
        web_app_app_dir: /opt/app_python
        web_app_image: slry/python_moscow_time:latest
        web_app_ports: 8081:8080
        web_app_full_wipe: true
        web_app_docker_ansible_user: slry
```
