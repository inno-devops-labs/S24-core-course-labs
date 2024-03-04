# Web App Role

## Description
This Ansible role installs Docker and Docker-Compose on host virtual machine by using `docker` Ansible role and runs Docker image via Docker-Compose with simple web application which shows current Moscow time.

## Requirements
Requirements for the role:
* all requirements for `docker` role;
* `docker` role.

## Variables
In this role several variables are used:
* docker_app_base_dir: path of files directory;
* docker_image: name of used image;
* docker_container_name: name of docker container;
* ports: ports external and internal, which are used in image running; 
* web_app_full_wipe: variable which show if container should be stopped and related files removed.

## Dependencies:
Only one dependency: my own `docker` role.

## Usage
For proper usage define "hosts" and "role" in file `ansible/playbooks/dev/main.yaml` as following:
```commandline
- hosts: <YOUR_HOST_NAME>
  roles:
    - role: <YOUR_ROLE_NAME>
      become: true
```

In case of using this role, specify only <YOUR_ROLE_NAME>, role will be `web_app`:
```commandline
- hosts: <YOUR_HOST_NAME>
  roles:
    - role: web_app
      become: true
```

`become: true ` means that role is executing with "root" rights, use it in case of installing packages with root permission.

To execute the role, run the following command from `ansible` folder:
```commandline
ansible-playbook playbooks/dev/main.yaml 
```
It is possible to specify your own playbook path.