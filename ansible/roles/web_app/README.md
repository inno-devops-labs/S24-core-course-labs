# Role

This Ansible role facilitates the deployment of a web application through Docker Compose.

## Requirements

This role relies on Ubuntu of any version and Python 3. Additionally, it requires the geerlingguy.docker role to be installed for Docker and Docker Compose setup

## How to use

```yaml
- hosts: all
- roles:
    - role: ../../../roles/web_app
      become: yes
      vars:
        app_dir: app_python
        web_image: bavpnet/app_python
        web_port: 8080
```
