# Web App Role

Requirements:

- `docker` role to ensure that docker is installed

The role contains several tasks:

- Get image nad run container (tag `run`)
  - Get image (defined by variables `username`/`image_name`:`tag`)
  - Run container (defined by variables `username`/`image_name`:`tag` and `name` for container)
- Deliver Docker Compose (tag `compose`)
  - Create directory (`/tmp/compose/`)
  - Deliver compose (from `templates/docker-compose.yml.j2` to `/tmp/compose/{{ name }}.docker-compose.yml`)
- Wipe image and container (tag `wipe`)
  - Remove container (the same variables as for `Run container`)
  - Remove image (the same variables a for `Get image`)

## Usage

```yaml
---
- name: Deploy Docker
  hosts: yacloud
  remote_user: user
  become: true

  roles:
    - role: <path-to-roles>/web_app
      vars:
        name: "app_python"
        username: "tufra"
        image_name: "moscow-time-app-python"
        tag: "0.0.1"
        ports: "80:8080"
        web_app_full_wipe: true
```