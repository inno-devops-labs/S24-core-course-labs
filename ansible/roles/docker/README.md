Docker
=========

Install docker on an Ubuntu machine (>22.04)

Role Variables
--------------

| Variable               | Required | Default | Choices                            | Comments                                 |
|------------------------|----------|---------|------------------------------------|------------------------------------------|
| docker_edition         | yes      | ce      | docker editions                    | docker edition (ce for community edition)|
| docker_service_manage  | yes      | true    | true/false                         | whether to manage the service            |
| docker_service_state   | yes      | started | started/stopped/restarted/reloaded | service state                            |
| docker_service_enabled | yes      | true    | true/false                         | whether service is enabled or not        |

Example Playbook
----------------
```
    - hosts: all
      roles:
         - docker
```
