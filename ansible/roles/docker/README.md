# Docker Role

This Ansible role automates the installation of Docker and Docker Compose on target hosts.

## Requirements

- Ansible installed on the control node.
- Target hosts accessible via SSH.
- Internet access on the target hosts for package installation.

## Role Variables

The role utilizes the following variables:

- `docker_gpg_key`: URL to the GPG key for Docker repository.

## Dependencies

This role has no external dependencies.

## Installation

No specific installation steps are required for this role. Simply include it in your playbook's roles section.

## Usage

1. Include the Docker role in your playbook's roles section:

    ```yaml
    - name: Docker role
        hosts: all
        become: true

        roles:
            - ../../roles/docker 
    ```
2. Set up inventory file

```yaml
my_hosts:
  hosts:
    host_01:
      ansible_host: 158.160.116.148
      ansible_user: ubuntu
```



3. Run your playbook:

    ```bash
    ansible-playbook ./playbooks/dev/main.yml --diff -i ./inventory/default_aws_ec2.yml
    ```