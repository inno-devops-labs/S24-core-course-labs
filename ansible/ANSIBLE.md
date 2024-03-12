### Deployment command
```ansible-playbook playbooks/dev/main.yaml --diff```
```
(myenv) nikitazorin@MacBook-Air-Nikita-2 ansible % ansible-playbook playbooks/dev/main.yaml --diff                                                                       

PLAY [Install Docker] ***************************************************************************************************************************************************

TASK [Gathering Facts] **************************************************************************************************************************************************
ok: [vm1]

TASK [docker : include_tasks] *******************************************************************************************************************************************
included: /Users/nikitazorin/Documents/DevOps/S24-core-course-labs/ansible/roles/docker/tasks/install_docker.yaml for vm1

TASK [docker : Installation of necessary system packages] ***************************************************************************************************************
ok: [vm1]

TASK [docker : Retrieve Docker GPG apt Key] *****************************************************************************************************************************
ok: [vm1]

TASK [docker : Delete conflicting Docker GPG apt Key] *******************************************************************************************************************
ok: [vm1]

TASK [docker : Add Docker Repository to apt sources] ********************************************************************************************************************
ok: [vm1]

TASK [docker : Update apt cache and install Docker Community Edition (docker-ce)] ***************************************************************************************
skipping: [vm1]

TASK [docker : include_tasks] *******************************************************************************************************************************************
included: /Users/nikitazorin/Documents/DevOps/S24-core-course-labs/ansible/roles/docker/tasks/install_compose.yaml for vm1

TASK [docker : Install pip] *********************************************************************************************************************************************
ok: [vm1]

TASK [docker : Set Docker Compose pip package name] *********************************************************************************************************************
ok: [vm1]

TASK [docker : Install Docker Compose] **********************************************************************************************************************************
changed: [vm1]

PLAY RECAP **************************************************************************************************************************************************************
vm1                        : ok=10   changed=1    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0   

```
### Inventory information
``` ansible-inventory -i inventory/cloud_yandex.yaml --list```

```
{
    "_meta": {
        "hostvars": {
            "vm1": {
                "ansible_host": "178.154.207.144",
                "ansible_user": "ubuntu"
            }
        }
    },
    "all": {
        "children": [
            "ungrouped",
            "myhosts"
        ]
    },
    "myhosts": {
        "hosts": [
            "vm1"
        ]
    }
}

```
### Deployment information
```
nikitazorin@MacBook-Air-Nikita-2 ansible % ansible-playbook playbooks/dev/main.yaml --tags "deploy,wipe" --diff

PLAY [Install Docker] ********************************************************************************************

TASK [Gathering Facts] *******************************************************************************************
Enter passphrase for key '/Users/nikitazorin/.ssh/ya_cloud_key': 
ok: [vm1]

PLAY [Deploy Web Application] ************************************************************************************

TASK [Gathering Facts] *******************************************************************************************
ok: [vm1]

TASK [web_app : Create folder] ***********************************************************************************
ok: [vm1]

TASK [web_app : Copy docker-compose file] ************************************************************************
--- before: /home/nikzor/compose.yaml
+++ after: /Users/nikitazorin/.ansible/tmp/ansible-local-75246w4_rkl7r/tmp9czw6x7g/docker-compose.yml.j2
@@ -1,6 +1,6 @@
 version: '3'
 services:
   web_app:
-    image: "nikzor/devops-lab-container"
+    image: "nikzor/my-flask-app"
     ports:
       - "80:5000"
\ No newline at end of file

changed: [vm1]

TASK [web_app : Start web app] ***********************************************************************************
changed: [vm1]

TASK [web_app : Stop and remove Docker container] ****************************************************************
skipping: [vm1]

PLAY RECAP *******************************************************************************************************
vm1                        : ok=5    changed=2    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0 
```