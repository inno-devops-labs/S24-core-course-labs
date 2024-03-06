# New Docker role 

## Description
It's an ansible role which installs Docker on Ubuntu.

## Requirements
1. Ubuntu
2. Python v. 3

## Usage (Running playbooks\dev\main.yaml)
```
- name: run Docker role
  hosts: all

  become: true
  roles:
    - docker
```