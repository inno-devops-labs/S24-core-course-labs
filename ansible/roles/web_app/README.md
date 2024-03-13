# Ansible Role: web_app

This Ansible role is designed for deploying a web application using Docker containers.

## Requirements

- Python 3.8 or newer
- Ansible

## Usage

- Configuration:
    - Specify the following variables:
        - Name of the web application
        - Port for the web application
        - Directory of the web application
        - Hostname
        - Option for a full wipe of the web application (web_app_full_wipe)


```sh
---
- name: Deploy Python Application
  hosts: all
  roles: 
  - role:  ../../../roles/web_app
    become: true
    vars:
      web_app_name: "python-app"
      web_app_port: 8000
      web_app_dir: "/home/{{ ansible_user }}/{{ web_app_name }}"
      host_name: "{{ ansible_host }}"
      web_app_full_wipe: true
```