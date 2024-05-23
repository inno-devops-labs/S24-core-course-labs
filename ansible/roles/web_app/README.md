Docker
=========

Install docker on an Ubuntu machine (>22.04)

Dependencies
------------
docker role

Role Variables
--------------
container_image: container name, required
docker_image: docker image, required
host_port: port number, required
docker_port: port number, required
web_app_full_wire: (true|false), required

Example Playbook
----------------
```
    - hosts: all
      roles:
         - web_app
```
