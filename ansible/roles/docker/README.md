# Docker Role

This Ansible role is responsible for installing Docker and Docker Compose on a target machine.

## Requirements

This role requires Ansible 2.9 or higher.

## Role Variables

There are no specific variables for this role.

## Dependencies

There are no dependencies for this role.

## Tasks

This role includes two main tasks:

1. Install Docker: This task imports tasks from `install_docker.yml` to install Docker on the target machine.
2. Install Docker Compose: This task imports tasks from `install_compose.yml` to install Docker Compose on the target machine.

Both tasks are tagged with `docker`, which allows you to run just these tasks using the `--tags docker` option with the `ansible-playbook` command.
