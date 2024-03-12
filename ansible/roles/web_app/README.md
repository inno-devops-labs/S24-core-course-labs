## Web App role

This folder contains Ansible role that can be used to deploy web application using docker-compose

### Requirements

- Python 3
- Ubuntu

## Example of usage

```yaml
- name: Deploy python web application
  hosts: all
  become: true

  roles:
    - web_app
  vars:
    docker_image: "nad777/anton_nekhaev_flask"
    docker_tag: "latest"
    container_name: "web_app"
    app_directory: "app"
    exposed_port: "5001"
```
