
# Webapp role

## Description

Installs conternized docker web app on provided ansible managed hosts.

## Requirements

- Ansible version minimum 2.9
- Ansible managed host is debian based, checked on Ubuntu 18.04 LTS

## Example palybook

```yaml
---
- name: Install and run go web app using existing role
  hosts: all
  become: true

  roles:
    - web_app
  vars:
    docker_image: "image_name"
    tag: "latest"
    container_name: "app"
    app_directory: "app"
    exposed_ports: ["8080:8080", "8081:8081"]
```
