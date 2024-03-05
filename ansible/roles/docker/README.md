# Docker Role

## Overview

The Docker role automates the installation and configuration of Docker and Docker Compose on Ubuntu systems. It consists of tasks organized into separate files for clarity and modularity.

## Requirements

- **Ansible**: Ensure Ansible is installed on the control node where you will run the playbook.
- **Ubuntu**: This role is specifically designed for Ubuntu systems.

## Role Structure

```
-- roles
   |-- docker
   |   |-- defaults
   |   |   `-- main.yml
   |   |-- handlers
   |   |   `-- main.yml
   |   |-- tasks
   |   |   |-- install_compose.yml
   |   |   |-- install_docker.yml
   |   |   `-- main.ym
```


- `defaults/main.yml`: Default variables for the role.
- `handlers/main.yml`: Handlers triggered by tasks in the role.
- `tasks/install_compose.yml`: Task file to install Docker Compose.
- `tasks/install_docker.yml`: Task file to install Docker and its dependencies.
- `tasks/main.yml`: Main task file to include other task files.
### Tasks
#### install_compose.yml

This task file is responsible for installing Docker Compose on the target system.

- **Install Docker Compose**: Uses the `apt` module to install Docker Compose from the system's package manager (`apt`) repository.

#### install_docker.yml

This task file is responsible for setting up Docker on the target system.

- **Add Docker APT Repository**: Adds Docker's APT repository to the system's repository list. This ensures that the system can fetch Docker packages from the official Docker repository.

- **Add Docker's Official GPG Key**: Adds Docker's official GPG key to the system's keyring. This is necessary for verifying the authenticity of Docker packages downloaded from the APT repository.

- **Install Docker Dependencies**: Installs dependencies required for Docker installation, including `apt-transport-https`, `ca-certificates`, `curl`, `gnupg`, and `lsb-release`.

- **Install Docker**: Installs Docker CE (Community Edition) using the `apt` module. This ensures that Docker is installed and available on the target system.

### main.yml

This main task file includes the tasks from `install_docker.yml` and `install_compose.yml`.

- **Include Tasks from `install_docker.yml`**: Includes tasks from the `install_docker.yml` file, ensuring that Docker setup tasks are executed.

- **Include Tasks from `install_compose.yml`**: Includes tasks from the `install_compose.yml` file, ensuring that Docker Compose setup tasks are executed.

These tasks collectively ensure that Docker and Docker Compose are installed and configured properly on the target system, enabling you to manage Docker containers and services efficiently.

## Usage

1. **Clone the Repository**: Clone the Ansible playbook repository containing the Docker role.

    ```bash
    git clone https://github.com/glebuben/S24-core-course-labs.git
    ```

2. **Set up the config file**: set up config file as environmental variable.

    ```bash
    export ANSIBLE_CONFIG=./ansible/ansible.cfg
    ```

3. **Run the Playbook**: Run your playbook to apply the Docker role.

    ```bash
    ansible-playbook ./ansible/playbooks/dev/main.yaml
    ```

4. **Customize Variables**: Optionally, customize variables in `defaults/main.yml` to suit your environment.

## Variables

- `docker_compose_version`: Version of Docker Compose to install.
- `docker_apt_repo`: Docker APT repository URL.
- `docker_apt_key_url`: URL of Docker's official GPG key.
- `docker_dependencies`: List of dependencies required for Docker installation.

## Dependencies

- None

