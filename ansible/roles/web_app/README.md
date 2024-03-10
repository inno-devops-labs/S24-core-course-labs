# Web App

This role is created to facilitate with deploying Docker application to AWS.

## Usage

```
- name: Setup docker
  hosts: all
  become: yes
  roles:
    - ../../roles/docker
```

## Requirements

- Ubuntu ASW machine 