# Docker Role

## Description
This is ansible role that installs Docker and Docker-Compose on target hosts

## Requirements
- Ansible >= 2.10
- Target hosts are running Ubuntu 22.04

## Dependencies

- `apt`
- `python3`

## How to Use

Example of playbook:

```yaml
- name: Install Docker on cloud
  hosts: all
  become: true
  roles:
    - docker
```

### YML Files in Docker Folder

- defaults/main.yaml
- handlers/main.yaml
- tasks/install_pip.yaml
- tasks/install_docker.yaml
- tasks/install_compose.yaml
- tasks/main.yaml