# Ansible Role: Web Application with Docker

This Ansible role is designed for setting up and managing a Dockerized web application. It includes tasks for preparing the application environment, managing Docker containers and networks, and ensuring the web application is running in a Docker container as expected.

## Requirements

- Ansible 2.9 or higher.
- Docker installed on the target host.
- Docker Compose installed on the target host.

This role also depends on the `docker` Ansible role for Docker installation and setup. Ensure this dependency is resolved by including the `docker` role in your playbook or by installing Docker on your target hosts beforehand.

## Role Variables

Below are the key variables used in this role:

- `app_dir`: The directory on the host where the application files and Docker compose file will be located.
- `app_name`: The name of the application, used for Docker image tagging.
- `app_port`: The port on which the application will be accessible.

The variables are defined in my playbooks

## Dependencies

This role depends on another role:

- `docker`: Required for Docker setup. Ensure this role is included in your roles path or playbook.

## Example Playbook

Below is an example playbook that uses the `web_app` role:

```yaml
- hosts: web_servers
  roles:
    - role: docker
    - role: web_app
      vars:
        app_dir: "/path/to/your/app"
        app_name: "your_app_name"
        app_port: "your_app_port"
```

## Usage
- Prepare your environment: Ensure Docker and Docker Compose are installed on your target hosts. The `docker` role can be used for Docker setup.
- Define your variables: Set app_dir, app_name, and app_port according to your application's needs.
- Run the playbook: Use the example playbook provided above, adjusting the path, name, and port as necessary.
## Role Tasks Overview
- Run wipe: Removes existing Docker environments and cleans up related files and networks.
- Docker Compose Environment Setup: Ensures the application directory exists, sets up the Docker compose file from a template, and manages the Docker containers as specified.
- Start docker container: Starts the application's Docker containers using Docker Compose.
  
For detailed information on each task, refer to the tasks/main.yml and tasks/wipe.yml files within the role directory.