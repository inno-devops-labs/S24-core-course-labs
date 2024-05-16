# Ansible Role: web_app

An Ansible role to deploy a web application using Docker containers.

## Requirements

---

- Python 3.8+
- Ansible

## Usage

---
- Specify vars:
    - web app name
    - web app port
    - web application directory
    - host name 
    - web_app_full_wipe

```sh
---
- name: Deploy Python Application
  hosts: all
  roles: 
  - role:  ../../../roles/web_app
    become: true
    vars:
      web_app_name: "my-python-app"
      web_app_port: 5000
      web_app_dir: "/home/{{ ansible_user }}/{{ web_app_name }}"
      host_name: "{{ ansible_host }}"
      web_app_full_wipe: true
```