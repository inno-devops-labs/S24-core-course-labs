# New Web_App Role

## Description
It's a new ansible role which deploys a web app.
Includes installing pip, Docker, Docker Compose
Supports a 'wipe', it clears all previous specified containers. 
Dependencies: 'meta/main.yaml' file.

## Requirements
- Ubuntu (OS)
- A VM with a public IP address.
- Python on machine
- Docker image (available on DockerHub).

## Usage

1. Add the web_app role to playbook:

```yaml
- name: Deploy Docker
  hosts: all
  roles:
    - ../../roles/web_app
```
2. Run it using command:
``` bash
ansible-playbook playbooks/dev/main.yaml --diff
``` 
It is necessary to check the correctness of the configuration of the IP address and SSH connection. 
So, you may access the web app at xxx.xxx.xxx.xxx:5000, it will display the current Moscow time.