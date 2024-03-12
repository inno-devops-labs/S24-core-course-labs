# Ansible Role: Dockerized Flask App Deployment

This Ansible role automates the deployment of a Flask application inside a Docker container. It performs tasks such as creating directories, rendering Docker Compose configurations, starting Docker services, and managing the application lifecycle.

## Requirements

- Ansible installed on the control node.
- Docker installed on the target host(s).
- Python and Flask installed inside the Docker container.

## Role Variables

The role expects the following variables to be defined:

- `app_image_dir`: The directory where Docker images and configurations will be stored.
- `app_image_name`: The name of the Docker image for the Flask application.
- `app_image_tag`: The version/tag of the Docker image.
- `app_full_wipe`: Boolean flag indicating whether to perform a full wipe of the application before deployment.

## Dependencies

This role depends on the following Ansible collection:

- `community.docker`

Ensure that this dependency is installed before using the role.

## Example Playbook

```yaml
- name: ansible-lab-05
  hosts: all
  become: true
  roles:
    - web_app
```
For checking result:
<ip_address>:5000


## Best Practices
- Modularization: Break down the deployment process into smaller tasks and roles, such as creating directories, rendering templates, and starting services. This improves maintainability and reusability.
- Idempotency: Ensure that the playbook tasks are idempotent, meaning they can be run multiple times without changing the outcome. This prevents unintended changes to the system.
- Error Handling: Implement error handling mechanisms, such as conditionals (when statements) and error checks, to gracefully handle failures during deployment.