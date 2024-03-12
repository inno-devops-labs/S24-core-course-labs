# Ansible Role: web_app

An Ansible role to deploy a web application using Docker containers.

## Requirements

- Docker installed on the target host.
- Access to Docker Hub or a private Docker registry to pull Docker images.
- Expose `5000` and `5001` ports on the target host to access the web application. using AWS security group.

## Role Variables

- `docker_services`: (Required) Specifies the Docker services to be deployed. It should be a list of service names defined in the `docker-compose.yml` file.

## Dependencies

- You may need to install the `geerlingguy.docker` role to install Docker on the target host.
- Also You have to run the `geerlingguy.pip` role to install the `docker` Python package.

## Example Playbook

```yaml
- hosts: all
  roles:
    - role: web_app
      vars:
        docker_services:
          - app_javascript
          - app_python
```

## Usage

1. Define your web application services in the `docker-compose.yml.j2` template file.

2. Include this role in your Ansible playbook, specifying the `docker_services` variable with a list of services to deploy.

3. Run the playbook to deploy your web application using Docker containers.
