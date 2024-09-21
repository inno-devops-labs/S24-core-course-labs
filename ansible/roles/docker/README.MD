# Ansible Role: Docker

This Ansible role installs Docker on various Linux distributions. It is based on the role provided by [geerlingguy/ansible-role-docker](https://github.com/geerlingguy/ansible-role-docker), which is widely used and maintained.

## Requirements

Before using this role, ensure that the following conditions are met:

- **Ansible version**: 2.8 or higher.
- **Supported Linux distributions**:
  - Ubuntu
  - Debian
  - CentOS
  - Red Hat
  - Fedora
  - Amazon Linux 2
  - Others (check the repository for full details)
  
- **Python**: Python should be installed on the target system for Ansible to function.
- **Root/Administrative privileges**: Ensure you have the necessary privileges (via `sudo` or `become`) to install packages and modify system configurations.

## Role Variables

This role comes with several variables that can be customized to suit your environment. The following are some of the main variables you may want to configure:

```yaml
docker_users:
  - user1
  - user2

docker_apt_release_channel: stable
docker_apt_arch: amd64
docker_version: "20.10"
```

This playbook will install Docker on all hosts defined in your inventory, and it will add `your_username` to the Docker group so that the user can manage Docker containers without needing `sudo`.

## Additional Information

For more detailed usage instructions, troubleshooting tips, and customization options, visit the official [GitHub repository](https://github.com/geerlingguy/ansible-role-docker).
