# Docker Role

## Description

Installs docker on provided ansible managed hosts.

## Requirements

- Ansible version minimum 2.9
- Ansible managed host is debian based, checked on Ubuntu 18.04 LTS

## Example palybook

```yaml
---
- name: Install Docker
  hosts: all
  become: true
  roles:
    - docker
```
