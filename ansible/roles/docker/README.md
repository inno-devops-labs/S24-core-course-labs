# Docker Ansible Role

This Ansible role facilitates the installation and configuration of Docker and Docker Compose on target machines. It ensures the Docker environment is set up according to specified configurations.

## Requirements

- Ansible 2.12 or later
- Target machines running Linux distributions (Debian or Ubuntu)

## Usage

1. Clone the repository containing the Ansible playbook

2. Navigate to the directory containing the playbook:
```
cd <repository_directory>
```
3. Execute the playbook using the following command:
```
ansible-playbook <path_to your_playbook>
```

## Role Variables
The role defines several variables in the defaults/main.yml file:

- docker_edition: Specifies the Docker edition (ce for Community Edition or ee for Enterprise Edition).
- docker_packages: Lists the Docker packages to install.
- docker_service_manage: Indicates whether to manage the Docker service.
- docker_service_state: Defines the desired state of the Docker service.
- docker_service_enabled: Specifies whether the Docker service should be enabled at boot.
- docker_restart_handler_state: Defines the state for the Docker service restart handler.
- docker_install_compose_plugin: Specifies whether to install the Docker Compose plugin.
- docker_compose_version: Defines the version of Docker Compose to install.
- docker_compose_arch: Specifies the architecture for Docker Compose.
- docker_compose_url: Specifies the URL for downloading Docker Compose.
- docker_compose_path: Defines the installation path for Docker Compose.
- docker_add_repo: Specifies whether to add the Docker repository.
- docker_repo_url: Specifies the URL of the Docker repository.
- docker_apt_release_channel: Defines the release channel for Debian/Ubuntu systems.
- docker_apt_arch: Specifies the architecture for Docker on Debian/Ubuntu.
- docker_apt_repository: Defines the Docker apt repository configuration.
- docker_apt_ignore_key_error: Specifies whether to ignore GPG key errors during apt setup.
- docker_apt_gpg_key: Specifies the GPG key URL for Docker apt repository.

## Handlers
- restart docker: Restarts the Docker service.
## Tasks
The tasks are organized into several YAML files:

- install_compose.yml: Installs Docker Compose.
- install_docker.yml: Installs Docker packages.
- setup-Debian.yml: Sets up dependencies and repository for Debian-based systems.
- docker-users.yml: Manages users added to the Docker group.
## Additional Information
- The role ensures that old versions of Docker are not installed and installs necessary dependencies.
- It adds the Docker repository and GPG key to the apt configuration.
- The playbook ensures that the Docker service is started and enabled at boot.