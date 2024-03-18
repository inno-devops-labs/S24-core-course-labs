# web_app
## Overview
This position plays a key role in the deployment process of a web application. Its main responsibilities involve setting up essential components such as pip, Docker, and Docker Compose, as well as initiating a web server using docker-compose. Moreover, it provides support for a 'wipe' feature, allowing the removal of all existing containers if requested. The dependencies required for this role are outlined in the 'meta/main.yaml' file.

## Usage
To utilize this role, follow these steps:

1. Add the role to your playbook:
```yaml
- name: Deploy Docker
  hosts: all
  roles:
    - ../../roles/web_app
```
2. Run the playbook:
``` bash
ansible-playbook playbooks/dev/main.yaml --diff
``` 
You can access the web application at localhost:5000 with current time GMT+3.

## Requirements
- A VM with a public IP address.
- Ubuntu OS.
- Python on the machine.
- Availability of a Docker image from DockerHub. 