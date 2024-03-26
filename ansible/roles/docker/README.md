# Usage

The Docker role is responsible for installing Docker and Docker Compose.

# Requirements

* Python3 
* Pip3
* Ubuntu
* Ansible


```bash
ansible-playbook playbooks/dev/main.yml --diff
```

## Example Playbook

```yaml
- name: Install Docker
  hosts: all
  roles:
    - role: <path-to-custom-role>
      become: true
```