# Web Application Role
## Overview
This role facilitates the deployment of a web application.
Its primary tasks include installing pip, Docker, Docker Compose, and launching a web server using docker-compose. 
Additionally, it supports a 'wipe' feature, which clears all previous containers if specified. 
Dependencies for this role are defined in the 'meta/main.yaml' file.

## Requirements
- A VM with a public IP address.
- Ubuntu OS.
- Python pre-installed on the target machine.
- Availability of a Docker image from DockerHub. 
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
Ensure that you have correctly configured the IP address and SSH connection. Upon successful execution, you can access the web application at xxx.xxx.xxx.xxx:5000, displaying the current time in Moscow.