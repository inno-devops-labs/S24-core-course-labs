# Web App role

This is an Ansible role to deploy a web application using Docker Compose.

## Requirements for the hosts

- Ubuntu of any version;
- Python 3.

This role also depends on the Docker role to install Docker and Docker Compose.

## Usage

```yaml
- hosts: all
- roles:
    - role: web_app
      vars:
        app_directory: app_dada
        app_image: snejugal/devops-dada
        app_port: 8080
```
