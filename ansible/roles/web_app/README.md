# Web App Ansible Role

This Ansible role is used for deploying and managing a Dockerized web application.

## Requirements

- Ansible 2.0+
- Docker

## Role Variables

- `web_app_full_wipe` is used to control wipe of docker image

## Dependencies

This role has a dependency on the `docker` role.

## Usage

Include this role in your playbook and ensure that the `docker` role is executed before the `web_app` role.

Example playbook:

```yaml
- name: Deploy Web App
  hosts: all
  become: true
  roles:
    - docker
    - web_app
```

## Tasks

- `0-wipe.yml`: Wipes the Docker container if `web_app_full_wipe` variable is set to true.
- `main.yml`: Includes the wipe task and other tasks for pulling the latest Docker image, running the Docker container, and delivering the `docker-compose.yml` template.

## Tags

- `wipe`: Tag for wiping the Docker container.
- `image-pull`: Tag for pulling the latest Docker image.
- `docker-run`: Tag for running the Docker container.
- `template-delivery`: Tag for delivering the docker-compose.yml template.

## Template Delivery

The docker-compose.yml file template is delivered to the target server using the template module.
