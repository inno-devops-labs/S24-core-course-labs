# Ansible

## Table of Contents

- [Ansible](#ansible)
  - [Table of Contents](#table-of-contents)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Inventory](#inventory)
  - [Custom `web_app` Role](#custom-web_app-role)
    - [Usage](#usage)
    - [Output](#output)
    - [Demo](#demo)
  - [Best Practices](#best-practices)

## Prerequisites

For this assingment, I needed two AWS EC2 instances running that could be accessed using SSH. I also needed to have `ansible` installed on my local machine.

For quick setup, I modified my terraform script to create two `t2.micro` instances in the `eu-central-1` region. The servers are tagged as `server-python` and `server-bun` respectively. I also added the following security group rules to allow SSH access from my IP address and HTTP access from anywhere. The changes can be found [here](../terraform/aws.tf).

## Installation

I had to install `aws` collection from `ansible-galaxy` using the following commands:

```bash
ansible-galaxy collection install amazon.aws
```

Apart from that, I needed to install `boto3` and `botocore` using the following command as a dependency for the `amazon.aws` collection:

```bash
pip install boto3 botocore
```

For `ansible.cfg`, I used the following configuration:

```ini
inventory=./inventory
roles_path=./roles
host_key_checking=False
```

The first two were to specify the directory for the inventory and roles. The `host_key_checking` was set to `False` to avoid the prompt for adding the host to the `known_hosts` file.

## Inventory

I used dynamic inventory to fetch the EC2 instances from AWS. I created a file `default_aws_ec2.yml` in the `invetory` directory and looked for `server-python` and `server-bun` tags to fetch the instances. The `ansible-user` was set to `ubuntu` as a compose key-value. `compose` was also instructed to use the IP address of the instances.

I additionally used tag group to get the instances of different tags together. This gave me the flexibility to run the playbook on different groups of instances.

```json
"app_server_bun": {
        "hosts": [
            "ec2-3-79-184-244.eu-central-1.compute.amazonaws.com"
        ]
    },
    "app_server_python": {
        "hosts": [
            "ec2-18-193-109-68.eu-central-1.compute.amazonaws.com"
        ]
    },
```

## Custom `web_app` Role

I created a custom role `web_app` to deploy a web app on the EC2 instances. This role uses docker-compose to run the web app and nginx as a reverse proxy. The docker image is pulled from docker hub.

The playbook `main.yml` in the `playbooks/dev/app_python` directory to use the role looks like this:

```yaml
---
- name: Install docker
  hosts: app_server_python
  roles:
    - role: docker
      become: true

- name: Deploy web app
  hosts: app_server_python
  roles: 
  - role: web_app
    become: true
    vars:
      app_name: "app_python"
      app_port: 5000
      app_dir: "/home/{{ ansible_user }}/{{ app_name }}"
      host_name: "{{ ansible_host }}"
      web_app_full_wipe: true

```

### Usage

To deploy the web app-

```bash
ansible-playbook playbooks/dev/app_bun/main.yml
```

To wipe the web app-

```bash
ansible-playbook playbooks/dev/app_bun/main.yml --extra-vars "web_app_full_wipe=true" --tags "wipe"
```

To wipe the web app and deploy it again-

```bash
ansible-playbook playbooks/dev/app_bun/main.yml --extra-vars "web_app_full_wipe=true"
```

To deploy without installing docker-

```bash
ansible-playbook playbooks/dev/app_bun/main.yml --skip-tags "docker"
```

### Output

Running `ansible-playbook playbooks/dev/app_python/main.yml --diff` gives me the following output (last 50 lines):

```ansible
TASK [web_app : Copy nginx configuration file] *********************************
--- before
+++ after: /home/pptx704/.ansible/tmp/ansible-local-128348u88nvgab/tmprt4kht0v/nginx.conf.j2
@@ -0,0 +1,10 @@
+server {
+    listen 80;
+    listen [::]:80;
+
+    server_name 18.157.165.23;
+
+    location / {
+        proxy_pass http://localhost:3000/;
+    }
+}

changed: [ec2-18-157-165-23.eu-central-1.compute.amazonaws.com]

TASK [web_app : Create folder for web app if it does not exist] ****************
--- before
+++ after
@@ -1,4 +1,4 @@
 {
     "path": "/home/ubuntu/app_bun",
-    "state": "absent"
+    "state": "directory"
 }

changed: [ec2-18-157-165-23.eu-central-1.compute.amazonaws.com]

TASK [web_app : Copy template file] ********************************************
--- before
+++ after: /home/pptx704/.ansible/tmp/ansible-local-128348u88nvgab/tmpccdd0811/docker-compose.yml.j2
@@ -0,0 +1,7 @@
+version: "3"
+
+services:
+  web:
+    image: pptx704/app_bun:latest
+    ports:
+      - "3000:3000"

changed: [ec2-18-157-165-23.eu-central-1.compute.amazonaws.com]

TASK [web_app : Stop and remove Docker containers] *****************************
changed: [ec2-18-157-165-23.eu-central-1.compute.amazonaws.com]

TASK [web_app : Run docker-compose] ********************************************
changed: [ec2-18-157-165-23.eu-central-1.compute.amazonaws.com]

RUNNING HANDLER [web_app : Restart Nginx] **************************************
changed: [ec2-18-157-165-23.eu-central-1.compute.amazonaws.com]

PLAY RECAP *********************************************************************
ec2-18-157-165-23.eu-central-1.compute.amazonaws.com : ok=15   changed=7    unreachable=0    failed=0    skipped=7    rescued=0    ignored=0  
```

### Demo

Going to `http://IP_ADDRESS` of the EC2 instance in the browser gives me the following images-
![](https://i.postimg.cc/26hbxVpK/image.png)

![](https://i.postimg.cc/yYVgF1LL/image.png)


## Best Practices

- Related tasks were grouped together as blocks
- `web_app` role had `docker` role as a dependency in `meta/main.yml`. However, `docker` role was given a `never` tag to give the user the flexibility to skip the installation of docker.
- Tags were used to have more control over the execution of the playbook
- Wipe logic was added to the docker role with a control variable to decide whether to wipe the web app or not. Also, wipe was added as a tag to do selective runs.
- Templates were used to create the configuration files for nginx and docker-compose
