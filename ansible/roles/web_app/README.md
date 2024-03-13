# Ansible Docker role for deploying Python Web App

## Description

Pip, Docker, and Docker Compose are installed on the target hosts by this role (dependencies from **docker** role).
Next, it launches compose after rendering the docker-compose file. If the `wipe} flag is used, the containers 
are stopped and the picture is deleted from the computer.


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

We can also add the following parameters:

```yaml
- roles:
    - role: web_app
      image_name: "My Image name"
      image_tag: "tag"
      publish_ports:
        - 5000:5000
      wipe: false
```