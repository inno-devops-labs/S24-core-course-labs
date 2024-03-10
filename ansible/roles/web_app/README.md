# Web Application Deployment Role

## Overview
- Introduced two distinct tasks: deployment and cleanup, each encapsulated within its own executable segment.
- Dependencies are outlined within the meta directory, specifically pointing to the Docker role as a prerequisite.
- Incorporated two tags for operational ease: 'deploy' and 'wipe'.
- Implemented a cleanup procedure that halts the process if the container is active, ensuring data is thoroughly purged.
- Crafted a Docker Compose template for the configuration file, which is subsequently distributed to the target hosts.

## Requirements
Relies on the Docker role and employs the `community.docker.docker_compose` module, which is bundled within the default Ansible collection.

## Default Settings
```shell
image: "ananastya10/devops:lab2"
container_name: "web_app"
ports: "5000:5000"

deployment_method: "docker_compose"

complete_cleanup: true
```
These parameters offer flexibility in the application deployment configuration.

## Implementation
Incorporate this role into your playbook as demonstrated below.

```shell
- name: Deploy Web Application
  hosts: all
  become: true
  roles:
    - web_app

```