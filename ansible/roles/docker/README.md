# Docker role

This Ansible role installs Docker on Ubuntu remote server

## Requirements

- Ansible 2.16 or later
- Target hosts running Ubuntu

## Usage

Here is an example of playbook contents:

```yaml
- name: Install docker and docker-compose
  hosts: all
  become: true
  roles:
    - docker
```
