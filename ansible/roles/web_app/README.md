## Web App Ansible Role

This Ansible role is designed to deploy a web application using Docker.

### Requirements

- Docker
- Ubuntu

### Role Variables

- `app_dir`: The directory where the web application files will be located.
- `web_image`: The Docker image containing the web application code.
- `web_port`: The port on which the web application will listen.

### Usage

```commandline
- hosts: web_server
  roles:
    - role: ./roles/docker
      become: true
```