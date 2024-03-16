# Web App Role

This Ansible role is designed for deploying and managing a web application using Docker.

## Requirements

- Ansible version 2.9 or higher
- Target hosts must be operating Ubuntu 20.04 or Debian 10
- Python 3.8 or later with installed `pip3`
- Docker and docker-compose installed on target host

## Role Variables

- `docker_image`: Name of the Docker image
- `docker_image_tag`: Tag of the Docker image
- `docker_container_name`: Name of the Docker container
- `docker_container_port`: Port within the Docker container where the web application is listening
- `docker_host_port`: Port on the host to which the Docker container's port is mapped

## Dependencies

- `docker` role.


## Usage

1. Define the playbook (example: `playbooks/dev/main.yaml`)
2. Define the inventory file (example: `inventory/yandex_cloud.yml`):
3. Run the playbook inside ansible folder: `ansible-playbook playbooks/dev/main.yaml`