# Docker role

The role contains several tasks:

- Setup repo
  - Install dependencies: `curl` and `ca-certificates`
  - Setup keyrings folder
  - Add Docker apt key
  - Add Docker repository
- Disable Unattended Upgrades (since it may fail the playbook)
- Install pip
- Install Docker
- Install Docker Compose with pip

It adds the docker repository for `ubuntu` using `apt` module.

## Usage

```yaml
---
- name: Install Docker
  hosts: all
  remote_user: user
  become: true

  roles:
    - <path-to-roles>/docker
```