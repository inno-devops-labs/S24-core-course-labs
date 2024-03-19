# web_app ansible role

An ansible role is needed to, using Docker containers, deploy a web application.

## Requirements

- Python 3.8+
- Ansible

## How to use

- Specify variables:
  1. `web_app_name`
  2. `web_app_port`
  3. `web_app_dir`
  4. `host_name`
  5. `web_app_full_wipe`

```sh
---
- name: Deploy Python Application
  hosts: all
  roles:
  - role:  ../../../roles/web_app
    become: true
    vars:
      web_app_name: "app_python"
      web_app_port: 5000
      web_app_dir: "/home/{{ ansible_user }}/{{ web_app_name }}"
      host_name: "{{ ansible_host }}"
      web_app_full_wipe: true
```
