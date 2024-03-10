# Web Application Deployment role

## Description and requirements

### Deps
- `docker` role

### Description
Role stands for Continuous Deployment of docker containers with `docker-compose` on a target machines. 

Role supports deploy, wiping and both options in order wipe -> deploy.
Easy tool for management of docker containers on your machines.

## Usage
- Utilize this role by installing deps and adding it into your playbook, nothing in addition required

- Example of a playbook usage:
    ```yml
    - name: Test Playbook
    hosts: all
    become: yes
    tags: [web_app]
    roles:
        - name: web_app
        tags: [web_app]
        vars:
            app_image: docker.io/user/image
            app_name: app
            internal_port: 8000
            external_port: 8000
            web_app_full_wipe: true  # fully wipe without followed creation
    ```