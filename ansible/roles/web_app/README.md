# Web Application Deployment role

## Description and requirements

### Dependencies
- `docker` role

### Description
This role is responsible for Continuous Deployment of docker containers with `docker-compose` on a target machine. 

The role supports deployment, wiping and both deployment and wiping in the order of first wipe, and then deploy.
Lets you easily manage docker containers on your machines.

## Usage
- Utilize this role by installing the dependencies and adding it into your playbook.

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
