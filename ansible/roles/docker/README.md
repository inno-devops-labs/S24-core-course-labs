# Docker Ansible Role
This role installs Docker and Docker Compose on a target machine.

## Requirements
Ubuntu 18.04 or later VM.

## Usage

1. Set the following variables in your playbook:
```yaml
vars:
    ansible_user: slry # ubuntu is default value
```

2. Include the role in your playbook:
```yaml
roles:
    - docker
```
