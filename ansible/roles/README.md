# Web App Ansible Role

This Ansible role is designed for deploying a web application using Docker.

## Requirements

This role requires the `docker` role as a dependency.

## Usage

1. Include this role in your Ansible playbook.
2. Set appropriate variables such as `docker_image`, `docker_container_name`, etc.
3. Run the playbook.

## Variables

- `web_app_full_wipe`: A boolean variable to control whether to perform a full wipe of the application or not. Default is `false`.
- Other variables such as `docker_image`, `docker_container_name`, etc. should be defined according to your application requirements.
