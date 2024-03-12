# Web App Ansible Role

This Ansible role, `web_app`, is designed to manage a web application deployed using Docker containers. It handles tasks such as container management, image handling, and deployment of the application.

## Role Structure

The role directory structure is organized as follows:

```
web_app
├── defaults
│ └── main.yml
├── meta
│ └── main.yml
├── tasks
│ ├── 0-wipe.yml
│ └── main.yml
└── templates
└── docker-compose.yml.j2
```

- `defaults/main.yml`: Defines default variables used by the role.
- `meta/main.yml`: Specifies dependencies required by the role.
- `tasks/0-wipe.yml`: Handles wiping of Docker containers and images.
- `tasks/main.yml`: Contains tasks for pulling and running Docker containers, wiping Docker, and copying template files.
- `templates/docker-compose.yml.j2`: Jinja2 template for the Docker Compose file used to deploy the web application.

## Role Dependencies

This role depends on the Docker role to ensure Docker and Docker Compose are installed on the target hosts. 
## Role Variables

The role defines the following variables in `defaults/main.yml`:

- `web_app_full_wipe`: A boolean flag indicating whether to perform a full wipe of containers and images.
- `web_image`: The Docker image to use for the web application.
- `container_name`: The name of the Docker container.
- `web_port`: The port on which the web application will be accessible.

## Tasks Overview

- **Container Handling**: Task for stopping and removing Docker containers.
- **Image Handling**: Task for removing Docker images.
- **Pull and Run Docker Container**: Task for pulling the Docker image and running the container.
- **Wipe Docker**: Task for wiping containers and images, executed conditionally based on `web_app_full_wipe`.
- **Copy Template File**: Task for copying the Docker Compose template file.

## Tags

This role uses the following tags to organize its tasks:

- **remove-container**: Tags related to stopping and removing Docker containers.
- **remove-image**: Tags related to removing Docker images.
- **docker-pull**: Tags related to pulling Docker images.
- **docker-run**: Tags related to running Docker containers.
- **wipe**: Tags related to wiping Docker containers and images.
- **deploy**: Tags related to deploying the web application.

## Usage

To use this role, include it in your Ansible playbook along with the Docker role and provide necessary variables. For example:

```yaml
- name: Deploy Web App
  hosts: web_servers
  roles:
    - role: docker
    - role: web_app
      vars:
        web_app_full_wipe: true
        web_image: "your_custom_image:tag"
        container_name: "your_container_name"
        web_port: 8000
```