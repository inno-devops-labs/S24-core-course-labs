# Description
This is the Ansible role that installs Docker on Ubuntu

# Requirements
1. Ubuntu
2. Python 3

# How to use
```
- name: Run Docker role
  hosts: all
  become: true
  roles:
    - docker
```