# Web App role

Role for deploying `web_app` using docker compose 

## Requirements:

- Ubuntu 
- Python
- Installed docker compose v2 on machine

## Usage
```
- name: Deploy Web Application
  hosts: all
  become: true
  roles:
    - web_app
```