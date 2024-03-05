# Ansible Role: Docker

---

Simple docker role. It installs `pip` and `docker`
using `ansible.builtin.apt` and `docker-compose`
using installed `pip` in previous step

## Requirements

---

- Python 3.8+
- Ansible

## Usage

---

- Import role
- Execute command with `docker` or `docker-compose`

## Example Playbook

```yaml
- hosts: all
  roles:
    - { role: <path_to_role> }
  tasks:
    - name: Use docker
      command: docker pull <url>
```