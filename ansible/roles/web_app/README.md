# Ansible Role: web_app

An Ansible role for deploying a web application using Docker and Docker Compose.

## Requirements

This role requires the following dependencies:

- Ansible 2.9 or later
- Docker
- Docker Compose

## Role Dependencies

This role is dependent on the following roles:

- docker

## Role Variables

The following variables can be customized to configure your web application deployment:

- web_app_full_wipe: A boolean variable that determines whether to wipe all related files when running the playbook. Default is true.

## Tags

This role includes the following tags:

- web_app: Includes all tasks related to deploying the web application.
- web_app_wipe: Includes all tasks related to wiping the web application.

## Usage

To use this role, include it in your playbook and customize the necessary variables:

yaml

- hosts: localhost
  roles:
  - role: web_app
    vars:
    web_app_full_wipe: true

You can also run specific tasks using tags:

bash
ansible-playbook playbook.yml --tags "web_app_wipe"

## Credits

This role was created by Wesam Naseer .
