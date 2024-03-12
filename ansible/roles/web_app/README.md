# Web app role

## Overview

The `web_app_deployment` Ansible role facilitates the deployment and management of Dockerized web applications. It streamlines tasks such as pulling Docker images, creating containers, and configuring related settings.

## Prerequisites

- Ansible must be installed on the control machine.
- Docker should be installed on the target hosts.

## Directory Structure

The directory structure of this role is organized as follows:

```
.
|-- defaults
|   `-- main.yml
|-- meta
|   `-- main.yml
|-- tasks
|   |-- 0-wipe.yml
|   `-- main.yml
`-- templates
   `-- docker-compose.yml.j2
```

- `docker-compose.yml.j2` contains docker compose schema that describes build, ports and
- `main.yml` in `defaults` contains avialable repositories
- `main.yml` in `meta` contains dependencies.
- `main.yml` in `tasks` contains number of steps for service deployment
- `0-wipe.yml` in `tasks` describes a way to remove all project files from sever

## How to Run

For python application:

```bash
ansible-playbook playbooks/dev/app_python/main.yaml --diff -i inventory/default_aws_ec2.yml --private-key ~/.ssh/yandex_cloud
```

For scala application:

```bash
ansible-playbook playbooks/dev/app_scala/main.yaml --diff -i inventory/default_aws_ec2.yml --private-key ~/.ssh/yandex_cloud
```
