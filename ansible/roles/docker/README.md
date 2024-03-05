# Docker Role

## Description

This Ansible role installs and sets up hosts with docker and pip.

## Requirements

- Ansible >=2.9

## Host requirements

- Ubuntu 22.04
- python3 installed

## Usage

1. Create playbook:

   ```yaml
   - name: Install docker and pip
     become: true
     hosts: all
     roles:
       - ../../roles/docker 
   ```

2. Set inventory file

   ```yaml
   my_hosts:
     hosts:
       host_01:
         ansible_host: 51.250.95.217
         ansible_user: ubuntu
   ```

3. Run playbook

   ```bash
   ansible-playbook playbooks/dev/main.yml
   ```

