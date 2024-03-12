# Ansible Role: web_app

## Description

This Ansible role, `web_app`, is designed for deploying and managing a Dockerized web application. It includes tasks for pulling Docker images, creating containers, and managing related configurations.

## Requirements

- Ansible installed on the control machine.
- Docker installed on the target hosts.

## Role Structure

The role directory structure is as follows:

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


- `defaults/main.yml`: Default variables for the role.
- `handlers/main.yml`: Handlers triggered by tasks.
- `meta/main.yml`: Metadata and dependencies.
- `tasks/main.yml`: Main tasks for deploying Docker containers.
- `templates/docker-compose.yml.j2`: Jinja2 template for Docker Compose file.

## Role Usage

1. **Clone the repository:**

2. **Integrate the role into your playbook:**

    Update your playbook (`playbook.yml`):

    ```yaml
    ---
    - name: Deploy Web Application
      hosts: your_target_hosts
      become: yes
      roles:
        - web_app
    ```

3. **Execute the playbook:**

    ```bash
    ansible-playbook -i inventory playbook.yml
    ```

## Example Playbook

```yaml
---
- name: Deploy app_python
  hosts: all
  become: true
  roles:
    - web_app
  vars:
    web_app_name: app_python
    web_app_internal_port: 8080
    web_app_external_port: 8080
    web_app_full_wipe: true

```
