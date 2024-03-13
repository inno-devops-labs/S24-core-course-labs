# Web app role

The purpose of this role is to run web app via Docker

## Description

The place where web application files will be kept is specified by this `web_app` role. It makes use of the deployed
Docker image. It also specifies the name of the Docker container that is going to be constructed using the given Docker
image. Additionally, it incorporates a full wipe of the web application directory using the variable
{web_app_wipe}.

## Dependencies

* `docker` role

## Usage

`playbook/dev/main.yml`

```bash
- name: Add new role
  hosts: all
  become: true

  roles:
    - web_app
    - docker
```

```bash
ansible-playbook ansible/playbooks/dev/main.yml
```
