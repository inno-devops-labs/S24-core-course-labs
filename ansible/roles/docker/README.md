# Docker Role

## Description
This role installs Docker and Docker Compose on target machines.

## Requirements
- Ansible 2.9+
- Target system running Ubuntu/Linux

## Role Variables
- `docker_compose_version` (default: `1.29.2`)

## Usage
To use this role, add it to your playbook as follows:

```yaml
- hosts: all
  roles:
    - docker
