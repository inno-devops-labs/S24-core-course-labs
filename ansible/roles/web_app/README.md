# Web app role

This role deploys a python web application using Docker.

## Description

This `web_app` role specifies the directory where web application files will be located. It utilizes the Docker image to
be deployed. Also, it defines the name of the Docker container that will be created from the specified Docker image. And
it uses variable `web_app_full_wipe` to include full wipe of the web application directory.

## Dependencies

* `docker` role

## Usage

```yaml
- hosts: all
  roles:
    - ../../roles/web_app
```

```bash
ansible-playbook playbooks/dev/main.yml
```
