# `web_app` role

This role is used to deploy a web application on a server. It uses docker-compose to run the containerized application and nginx to serve it.

## Requirements

- Ubuntu 18.04 or later
- Python 3.6 or later
- `pip3` installed
- Docker and docker-compose installed

## Role Variables

There are several variables associated with this role. None of them have default values, so they must be set in the playbook.

- `app_name`: Name of the docker image. `pptx704/<app_name>:latest` will be fetched in the `docker-compose.yml` file.
- `app_port`: Port where the application is getting served. Docker compose will use `app_port:app_port` that will be mapped to port 80 by nginx.
- `app_dir`: The directory where `docker-compose.yml` file should be placed. If the directory does not exist, it will be created.
- `host_name`: The domain name or the IP address of the application. This will be used in the nginx configuration file.
- `web_app_full_wipe`: If set to `true`, the role will remove everything related to the application from the server. This includes the docker container, the docker image, the docker network, the nginx configuration file. However, the `app_dir` will not be removed.

## Dependencies

The following roles are required to be run before this role:

- `docker`

Although, `docker` is set as a meta dependency, it will not run automatically. It should be run manually before running this role.

## Example Playbook

```yaml
- name: Install docker
  hosts: app_server_python
  roles:
    - role: docker
      become: true

- name: Deploy web app
  hosts: app_server_python
  roles: 
  - role: web_app
    become: true
    vars:
      app_name: "app_python"
      app_port: 5000
      app_dir: "/home/{{ ansible_user }}/{{ app_name }}"
      host_name: "{{ ansible_host }}"
      web_app_full_wipe: true
```

Tags that can be used with this role:

- `setup`: Related to the setup and deployment of the web app
- `wipe`: Related to the removal of the web app

## License

MIT
