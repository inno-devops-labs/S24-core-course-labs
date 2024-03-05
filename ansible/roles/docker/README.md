# Ansible Docker role

## Description

This role installs pip, Docker and Docker Compose on the target hosts.

## Requirements

1. Ubuntu OS
2. Python 3.x

## Usage

Add the role to the `playbooks/dev/main.yml` file:

```yaml
- hosts: all
- roles:
    - role: docker
```