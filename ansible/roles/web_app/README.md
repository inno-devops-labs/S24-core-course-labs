Web app
=========

This role is used to deploy web app with docker

Requirements
------------

- Python 3
- Ubuntu

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

```yaml
- name: Install web app
  hosts: all
  become: true

  roles:
    - web_app
  vars:
    docker_image: "vladdan16/app_python:latest"
    container_name: "web_app"
    exposed_port: "8000"
    app_dir: "app"
    wipe: false
```
