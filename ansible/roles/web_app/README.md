# Ansible Role: WebApp

---

Using docker role to install docker

## Requirements

---

- Python 3.8+
- Ansible

(For docker role)

## Usage

---

- Import role
- Specify vars:
    - inner_port (port to use inside docker container)
    - app_port (to expose)
    - repo_name (repository name for docker hub)
    - version (version of repository to pull correct image)
    - web_app_full_wipe
    (if you want to wipe previously deployed image with the same name)

## Example Playbook

```yaml
- hosts: all
  roles:
    - role: <path_to_role>
      vars:
        inner_port: 5000
        app_port: 5000
        repo_name: <repo_name>
        web_app_full_wipe: false
        version: latest
```