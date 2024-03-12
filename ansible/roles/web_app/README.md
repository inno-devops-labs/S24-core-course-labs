# Web App Role

This Ansible role is designed to deploy a Dockerized Python web application.

## Requirements

- Ansible
- Docker
- Docker Compose

## Usage

1. Ensure Ansible, Docker, and Docker Compose are installed on the target system.
2. Create a playbook including this role and configure necessary variables in `defaults/main.yml`.
3. Execute the playbook to deploy the web application.
4. To wipe the application, set the variable `web_app_full_wipe` to `true` and run the playbook with the appropriate tag.

## Variables

- `base_path`: The base directory for the application.
- `web_app_service`: The name of the Docker service for the application.
- `ports`: Ports mapping for the application.
- `docker_image`: Details of the Docker image for the application.
- `web_app_full_wipe`: (Optional) A boolean variable to enable full wipe of the application.

## Tags

- `web_app`: Main tasks for deploying the web application.
- `wipe`: Tasks for wiping the application.
