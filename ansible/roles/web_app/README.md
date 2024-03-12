# web_app Ansible Role

This role deploys a web application using Docker containers. 

## Requirements

- The target host should have Docker installed.
- Expose `5000` and `5001` ports on the target host to access the web application. using AWS security group.

## Role Variables

- `docker_services`: (Required) Specifies the Docker services to be deployed. It should be a list of service names defined in the `docker-compose.yml` file.

## Dependencies

- Install the `geerlingguy.docker` role to install Docker on the target host.
- Run the `geerlingguy.pip` role to install the `docker` Python package on the target host.


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

1. Define your web application services in the `docker-compose.yml.j2` file.
2. Include the `web_app` role in your playbook and specify the `docker_services` variable.
3. Run the playbook to deploy the web application.