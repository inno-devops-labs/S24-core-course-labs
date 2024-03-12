# Ansible Role: Web App

An Ansible Role that runs [this](https://hub.docker.com/layers/dianatomiya/devops/p_v1.0/images/sha256-05e831502c38c755d6ebb0b6b3a72423a37ea80223648b2fe4528eda48027c2d?context=repo) app in docker.

## Requirements

Docker role

## Role Variables

Available variables are listed below, along with default values (see `defaults/main.yml`):

```yaml
app_name: app
image_name: dianatomiya/devops:p_v1.0
web_app_full_wipe: false
```

`app_name` is a name of a container.
`image_name` is a name of a docker image.
`web_app_full_wipe` is a boolean value that if true removes app container and image.

## Example Playbook

```yaml
- hosts: all
  roles:
    - web_app
```
