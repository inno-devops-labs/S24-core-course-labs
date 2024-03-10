# Ansible Docker role for deploying Python Web App

## Description

This role installs pip, Docker and Docker Compose on the target hosts (dependencies from **docker** role).
Then it renders docker-compose file and runs compose. If `wipe` flag is provided - stops the containers + removes the
image from machine.

## Requirements

1. Ubuntu OS
2. Python 3.x
3. Docker role

## Usage

Add the role to the `playbooks/dev/main.yml` file:

```yaml
- hosts: all
- roles:
    - role: web_app
```

You can also add the following parameters:

```yaml
- roles:
    - role: web_app
      image_name: "My Image name"
      image_tag: "tag"
      publish_ports:
        - 5000:5000
      wipe: false
```