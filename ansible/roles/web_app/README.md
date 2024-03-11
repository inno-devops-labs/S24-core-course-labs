# Ansible Web App role

## Description

This is an Ansible role to deploy app using docker compose on a target machines. This role implements optional application wipe logic, that can be enabled in playbook.

## Requirements

- Ubuntu
- This role also requires a `docker` role to install Docker and Docker Compose

## Usage

Add role and all needed variables to your playbook

Example:

```sh
- name: Deploy python app
  hosts: all
  become: true
  become_method: 'sudo'
  roles:
    - name: web_app
      tags: [web_app]
      vars:
        web_app_name: app_python
        web_app_path: /app_python
        internal_port: 8000
        external_port: 8000
        docker_image_name: 'alyonaart/app-python'
        docker_image_version: 'latest'
        web_app_full_wipe: true
```

