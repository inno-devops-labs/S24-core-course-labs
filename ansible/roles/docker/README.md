# Docker Role 

## Description
This Ansible role installs Docker and Docker-Compose oh host virtual machine. Docker installs with `apt`, however Docker-Compose installs by using `pip`. 

## Requirements
For this role exists only two requirements:
* host has to have Ubuntu;
* `apt` has to be installed.

Role installs `python3` and `python3-pip`, so there is not need to pre-install them.

## Usage
For proper usage define "hosts" and "role" in file `ansible/playbooks/dev/main.yaml` as following:
```commandline
- hosts: <YOUR_HOST_NAME>
  roles:
    - role: <YOUR_ROLE_NAME>
      become: true
```

In case of using this role, specify only <YOUR_HOST_NAME>, role will be `docker`:
```commandline
- hosts: <YOUR_HOST_NAME>
  roles:
    - role: docker
      become: true
```

`become: true ` means that role is executing with "root" rights, use it in case of installing packages with root permission.

To execute the role, run the following command from `ansible` folder:
```commandline
ansible-playbook playbooks/dev/main.yaml 
```
It is possible to specify your own playbook path.
