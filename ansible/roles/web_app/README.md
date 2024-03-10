# Python Web App role

This is an Ansible role to deploy the Python web application.

## Requirements for the hosts

- Ubuntu of any version;
- Python 3.

This role also depends on the Docker role to install Docker and Docker Compose.

## Usage

```yaml
- hosts: all
- roles:
    - role: web_app
```
