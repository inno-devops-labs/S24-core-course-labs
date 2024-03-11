# Ansible Web App role

## Description

This is an Ansible role for docker compose app deployment on target computers. The optional application wipe logic used by this role is playbook-enabled.

## Requirements

* Python3 
* Pip3
* Ubuntu
* Ansible
* Docker

## Usage

Add role to your playbook

Example:

```sh
- name: Deploy JS app
  hosts: all
  become: true
  become_method: 'sudo'
  roles:
    - name: web_app_js
      tags: [web_app_js]
      vars:
        web_app_name: app_js
        web_app_path: /app_js
        internal_port: 80
        external_port: 8080
        docker_image_name: 'LaithAlebrahim/js'
        docker_image_version: 'latest'
        web_app_full_wipe: false
```
