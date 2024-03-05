# Docker role

## Description

This is a custom Ansible role for Docker for:
- pip installation
- Docker installation using apt 
- Docker Compose installation using pip

## Requirements 

The host machine running Ubuntu

## Usage

Add role to roles in ```playbooks/dev/main.yaml```

```sh
---
- name: Install Docker
  hosts: all
  become: true
  roles:
    - docker
```