# Description

Ansible role that installs Docker on Ubuntu

## Requirements

1. Python 3
2. Ubuntu

## How to use

```
- name: run docker role
  hosts: all
  become: true
  roles:
    - docker
```