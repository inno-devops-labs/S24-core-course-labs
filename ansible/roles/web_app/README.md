# Web app role

## Description

This is the role created to deploy an application using docker-compose and template for it. This role depends on docker
role and has all the rights of the parent role. This role provides the wipe logic before the start if the parameter is
set. 

## Requirements

- Ansible
- Ubuntu

## Usage

1. Change config files for your purposes
    - Configure `Deploy application` in `/ansible/playbooks/dev/main.yml`
    - Configure inventory in `/ansible/inventory/default_aws_ec2.inl` file
2. Run ansible (with web_app_full_wipe=true if wipe needed) using
    ```bash
    ansible-playbook --diff playbooks/dev/main.yml
    ```