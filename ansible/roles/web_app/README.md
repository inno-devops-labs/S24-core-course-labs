# Web App Ansible Role

This Ansible role (`web_app`) is designed to facilitate the deployment of a Dockerized web application. It includes tasks for deploying the Docker image of the application, organizing related tasks using Ansible blocks, setting role dependencies, implementing tags for logical grouping, and providing wipe logic for cleaning up the deployment environment.

## Requirements

- Ansible installed on the control node.
- Docker installed on the target server.
- Access to the Docker registry/repository containing the web application image.
- Target server(s) configured with SSH access.

## Role Structure

````
.
├── defaults
│ └── main.yml
├── meta
│ └── main.yml
├── tasks
│ ├── main.yml
│ └── 0-wipe.yml
└── templates
└── docker-compose.yml.j2
````

- `defaults/main.yml`: Contains default variables for the role.
- `meta/main.yml`: Specifies dependencies for the role.
- `tasks/main.yml`: Main tasks file for deploying the Docker image and managing related tasks.
- `tasks/0-wipe.yml`: Tasks file for wipe logic, including removing Docker containers and related files.
- `templates/docker-compose.yml.j2`: Jinja2 template for the `docker-compose.yml` file.

## Usage

1. Ensure your playbook includes the `web_app` role:

    ```yaml
    - hosts: servers
      roles:
        - web_app