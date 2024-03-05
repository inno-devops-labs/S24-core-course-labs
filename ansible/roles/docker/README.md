# Docker Role

## Description

Target hosts have Docker installed using this Ansible role. It also handles settings related to Docker and installs Docker Compose.

## Requirements

- Ansible installed
- Target should be Debian-based host

## Usage

1. Define your playbook as it shown in the file;
2. Define `inventory/hosts.yml` as the inventory file;
3. Launch the playbook from the `ansible-playbook playbooks/dev/main.yml` ansible folder.
