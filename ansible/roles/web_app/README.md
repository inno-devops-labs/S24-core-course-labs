# Ansible Role: Web Application

Deploys web application as Docker container to a remote host.

Can also be used to wipe created containers.

## Requirements

None.

## Role Variables

Available variables are listed below, along with default values (see `defaults/main.yml`):

```yaml
web_app_full_wipe: false
```

Specifies whether to perform full wipe right after execution.

```yaml
container_name: "app_python"

image_repo: "mrfired/devops-course"
```

`container_name` and `image_repo` specify container name and repository for image respectively.

```yaml
host_interface: "0.0.0.0"
host_port: "5000"
container_port: "5000"
```

`host_interface` specifies bind address, `host_port` and `container_port` specify host and container ports respectively.

## Dependencies

`docker` role
