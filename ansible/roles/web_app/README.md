Web App role
=========

This role handles the installation of pip, Docker, and Docker Compose on designated hosts, utilizing dependencies from the docker role. Subsequently, it processes and deploys a docker-compose file, executing the composed services. Additionally, if a wipe flag is activated, it halts any running containers and purges the corresponding images from the host machine.

Requirements
------------
1. Ubuntu OS
2. Python 3.x
3. Docker role

Basic Playbook
----------------

    - hosts: all
      roles:
         - role: web_app

Extended Playbook
----------------

    - hosts: host1 // you can specify which hosts
      roles:
        - name: "Role custom name"
          role: web_app
          image_name: "My Image name"
          image_tag: "tag"
          publish_ports:
            - 5000:5000
          wipe: false