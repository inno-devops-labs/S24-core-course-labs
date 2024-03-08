## Web App Deploy app role

The role to deploy and a docker container to the target vm 

## Prerequisite 

To run the role you need an Ubuntu vm

## Requirements 

The role requires a `docker` role that deploys docker service on the ubuntu vm. 

## How to run 

To run the role you need to need to include it to your playbook by its name: `web_app`

Example: 
```
- name: Deploy Web App
  hosts: aws
  become: true
  vars: 
    web_app_full_wipe: false
  roles:  
    - role: web_app
```

After that you can run the playbook with `ansible-playbook <playbook-name>.yaml`. 

## Tags 

You can also tune the role depending on your needs with the tags below: 
* `deliver-docker-compose` if you want to create a generic docker-container.yml file on `/home/ubuntu` path file to run the app
* `deploy-python-app` if you want to deploy moscow-time docker container 
* `docker-compose-install` if you want to install docker-compose on your system 
* `docker-install` if you want to install docker on your system 
* `wipe-app-python` if you want to wipe the python_app docker container together with its volumes

You also need to override a boolean variable `web_app_full_wipe` (default: false) if you want to delete the docker container of the app together with its volumes. 