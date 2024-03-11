# Web app role

## Role

This role has the following tasks: install pip, Docker, Docker Compose and run web server using docker-compose.
It supports `wipe` if `wipe` is true it wipes all previous containers. In `meta` directory defined dependencies(`docker`
role)

## Requirements

1. VM with public ip
2. Ubuntu O
3. Python pre-installed on target machine
4. Available docker image from dockerHub

## Usage

First, add role into playbook:

```
- name: Deploy Docker
  hosts: all
  roles:
    - ../../roles/web_app
```

Then, you should run
`ansible-playbook playbooks/dev/main.yaml --diff --become --become-user=root`
Assuming that you configured ip and ssh connection correctly, on address xxx.xxx.xxx.xxx:5000 you will see current time
in Moscow

