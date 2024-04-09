# Install Docker on Ubuntu
Ansible role for installing the docker on ubuntu

# Requirements
1. Ubuntu
2. Python 3

# How to use

In your playbook directory create yaml file and write this code
```
- hosts: all

  roles:
    - docker

  become: yes
```