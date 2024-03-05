Docker Role
=========

Installing docker (using apt) and using docker-compose (using pip) on host machine.

Requirements
------------

- Ubuntu
- Python ^3.6
- pip3

Prerequisites
--------------
If ```docker.io``` is installed it may cause conflicts.


Role Variables
--------------

```docker_user```: Name of the user that should have the docker permissions.

Example Playbook
----------------

I have used ```docker_user``` variable for the role.


```
- hosts: my_host
  roles:
    - geerlingguy.docker
```

License
-------

MIT
