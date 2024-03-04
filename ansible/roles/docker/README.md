## Roles
### docker
The docker role installs Docker and Docker Compose on target hosts.

### Requirements:

 - Ubuntu 20.04 or later
 - Ansible 2.10 or later

### Tasks:

 1. Install pip.
 2. Install Docker dependencies using apt.
 3. Add Docker GPG key.
 4. Add Docker repository.
 5. Install Docker using apt.
 6. Install Docker Compose using pip.

### Usage:

Add the docker role to your playbook as follows:
```
roles:
  - docker
```
See README.md in the roles/docker folder for more details on the docker role.
bash

**README.md in ansible/roles/docker folder:**

## Docker Role
This Ansible role installs Docker and Docker Compose on target hosts.

### Requirements
 - Ubuntu 20.04 or later
 - Ansible 2.10 or later
