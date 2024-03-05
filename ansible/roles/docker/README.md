## Docker Installation with Ansible Role

This guide explains how to use an Ansible role to set up Docker on specific operating systems.

**Requirements:**

* Ansible version 2.9 or newer
* Target machines running Ubuntu 20.04 or Debian 10

**Customization:**

You can customize the installation process using variables defined in your playbook:

* `docker_gpg_apt_key_url`: URL for the Docker GPG key used by APT
* `docker_apt_repository`: URL for the Docker APT repository
* `docker_pip_compose_version`: Version of Docker Compose to install with pip

**Dependencies:**

* `apt`: package manager for Ubuntu/Debian
* `python3`: required for installing Docker Compose with pip

**Example Playbook:**

The following code snippet shows how to install Docker using this role:

```yaml
- name: Install Docker
  hosts: all
  become: true
  roles:
    - docker
```