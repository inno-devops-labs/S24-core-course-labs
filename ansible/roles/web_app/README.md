# Web app Ansible role

This role will install a web application Docker image on the host

## Requirements
- Docker ansible role

## Usage
```
- name: Example web app installation
  hosts: all
  become: true
  roles:
    - role: web_app
      image: ubuntu:latest
      ports:
        - 8080:8888
```