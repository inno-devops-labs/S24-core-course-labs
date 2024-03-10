# Web app role

## Description

Ansible role that deploys the web app on the target host

## Requirements

 - `Ansible` 2.16
 - `Ubuntu` and `python3` on the target host
 - `docker` role

## Example playbook

```yaml
---
- name: Deploy web app
  hosts: all
  become: true
  roles:
    - web_app

  vars:
    ansible_ssh_private_key_file: "~/.ssh/id_rsa"
    ansible_user: damir
    ansible_python_interpreter: /usr/bin/python3
    app_dir: app_python
    app_port: 8000
    app_image: damirafliatonov/moscow-time-app:latest
    web_app_full_wipe: true
    
```

In this playbook, you should specify the following variables:

 - `path_to_file` - path to the private ssh key on your machine.
 - `username` - name of the user on the host.
 - `python_interpreter_path` - path to the python interpreter on the host.
 - `app_dir` - directory, where the app will be launched
 - `app_port` - port of the app
 - `app_image` - docker image that will be deployed
 - `web_app_full_wipe` - true/false, whether the app should be wiped after running the image

In inventory file you should specify the hosts that will be used.
