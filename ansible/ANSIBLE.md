# Ansible

## Best practices

- Follow the structure of files that was recommended in the lab
- Assign a clear names for plays and tasks
- Configure global settings in ```ansible.cfg```
- Use fully qualified collection names to avoid ambiguity

## Outputs

### Deployment Output
 
```sh
$ ansible-playbook playbooks/dev/main.yaml --diff

BECOME password: 

PLAY [web_server] **************************************************************************************************

TASK [Gathering Facts] *********************************************************************************************
ok: [web_server]

TASK [docker : Install pip] ****************************************************************
included: /home/everyonehateme/programing/S24-core-course-labs/ansible/roles/docker/tasks/install_pip.yml for web_server

TASK [docker : Update apt] *****************************************************************************************
ok: [web_server]

TASK [docker : Install python] *************************************************************************************
ok: [web_server]

TASK [docker : Install pip] ****************************************************************************************
ok: [web_server]

TASK [docker : Install docker] *************************************************************************************
included: /home/everyonehateme/programing/S24-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for web_server

TASK [docker : Update apt] *****************************************************************************************
ok: [web_server]

TASK [docker : Install docker] *************************************************************************************
changed: [web_server]

TASK [docker : Install docker-compose] *****************************************************************************
included: /home/everyonehateme/programing/S24-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for web_server

TASK [docker : Install docker-compose] *****************************************************************************
changed: [web_server]

PLAY RECAP *********************************************************************************************************
web_server                 : ok=7    changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0  
```

### Inventory details

```sh
$ ansible-inventory -i inventory/default_local.yml --list
{
    "_meta": {
        "hostvars": {
            "web_server": {
                "ansible_host": "84.201.128.97",
                "ansible_user": "vm-admin"
            }
        }
    },
    "all": {
        "children": [
            "ungrouped",
            "virtual_machines"
        ]
    },
    "virtual_machines": {
        "hosts": [
            "web_server"
        ]
    }
}
```

## Application Deployment

### Python App

```sh
$ ansible-playbook playbooks/dev/app_python/main.yaml --diff

PLAY [Deploy python app] ****************************************************************************************************************************************************************************

TASK [Gathering Facts] ******************************************************************************************************************************************************************************
ok: [web_server]

TASK [docker : Install pip] *************************************************************************************************************************************************************************
included: /home/everyonehateme/programing/S24-core-course-labs/ansible/roles/docker/tasks/install_pip.yml for web_server

TASK [docker : Update apt] **************************************************************************************************************************************************************************
changed: [web_server]

TASK [docker : Install python] **********************************************************************************************************************************************************************
ok: [web_server]

TASK [docker : Install pip] *************************************************************************************************************************************************************************
ok: [web_server]

TASK [docker : Install docker] **********************************************************************************************************************************************************************
included: /home/everyonehateme/programing/S24-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for web_server

TASK [docker : Update apt] **************************************************************************************************************************************************************************
changed: [web_server]

TASK [docker : Add Docker's GPG key] ****************************************************************************************************************************************************************
ok: [web_server]

TASK [docker : Add Docker Repository] ***************************************************************************************************************************************************************
ok: [web_server]

TASK [docker : Install docker] **********************************************************************************************************************************************************************
ok: [web_server]

TASK [docker : Install docker-compose] **************************************************************************************************************************************************************
included: /home/everyonehateme/programing/S24-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for web_server

TASK [docker : Install docker-compose] **************************************************************************************************************************************************************
ok: [web_server]

TASK [web_app : Remove the app container] ***********************************************************************************************************************************************************
changed: [web_server]

TASK [web_app : Remove the directory] ***************************************************************************************************************************************************************
--- before
+++ after
@@ -1,10 +1,4 @@
 {
     "path": "/app_python",
-    "path_content": {
-        "directories": [],
-        "files": [
-            "/app_python/docker-compose.yaml"
-        ]
-    },
-    "state": "directory"
+    "state": "absent"
 }

changed: [web_server]

TASK [web_app : Create directory for the app] *******************************************************************************************************************************************************
--- before
+++ after
@@ -1,4 +1,4 @@
 {
     "path": "/app_python",
-    "state": "absent"
+    "state": "directory"
 }

changed: [web_server]

TASK [web_app : Generate docker-compose] ************************************************************************************************************************************************************
--- before
+++ after: /home/everyonehateme/.ansible/tmp/ansible-local-12587a0d8luwj/tmps76ywa_m/docker-compose.yml.j2
@@ -0,0 +1,5 @@
+services:
+  web_app:
+    image: "alyonaart/app-python:latest"
+    ports:
+      - "8000:8000"
\ No newline at end of file

changed: [web_server]

TASK [web_app : Start the app] **********************************************************************************************************************************************************************
changed: [web_server]

PLAY RECAP ******************************************************************************************************************************************************************************************
web_server                 : ok=17   changed=7    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0    

```

### Dart App

```sh
$ ansible-playbook playbooks/dev/app_dart/main.yaml --diff

PLAY [Deploy dart app] **********************************************************************************************************************************************

TASK [Gathering Facts] **********************************************************************************************************************************************
ok: [web_server]

TASK [docker : Install pip] *****************************************************************************************************************************************
included: /home/everyonehateme/programing/S24-core-course-labs/ansible/roles/docker/tasks/install_pip.yml for web_server

TASK [docker : Update apt] ******************************************************************************************************************************************
changed: [web_server]

TASK [docker : Install python] **************************************************************************************************************************************
ok: [web_server]

TASK [docker : Install pip] *****************************************************************************************************************************************
ok: [web_server]

TASK [docker : Install docker] **************************************************************************************************************************************
included: /home/everyonehateme/programing/S24-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for web_server

TASK [docker : Update apt] ******************************************************************************************************************************************
changed: [web_server]

TASK [docker : Add Docker's GPG key] ********************************************************************************************************************************
ok: [web_server]

TASK [docker : Add Docker Repository] *******************************************************************************************************************************
ok: [web_server]

TASK [docker : Install docker] **************************************************************************************************************************************
ok: [web_server]

TASK [docker : Install docker-compose] ******************************************************************************************************************************
included: /home/everyonehateme/programing/S24-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for web_server

TASK [docker : Install docker-compose] ******************************************************************************************************************************
ok: [web_server]

TASK [web_app : Remove the app container] ***************************************************************************************************************************
skipping: [web_server]

TASK [web_app : Remove the directory] *******************************************************************************************************************************
skipping: [web_server]

TASK [web_app : Create directory for the app] ***********************************************************************************************************************
--- before
+++ after
@@ -1,4 +1,4 @@
 {
     "path": "/app_dart",
-    "state": "absent"
+    "state": "directory"
 }

changed: [web_server]

TASK [web_app : Generate docker-compose] ****************************************************************************************************************************
--- before
+++ after: /home/everyonehateme/.ansible/tmp/ansible-local-132885ve9xqdo/tmp8ukznni9/docker-compose.yml.j2
@@ -0,0 +1,5 @@
+services:
+  web_app:
+    image: "alyonaart/app-dart:latest"
+    ports:
+      - "8080:80"
\ No newline at end of file

changed: [web_server]

TASK [web_app : Start the app] **************************************************************************************************************************************
changed: [web_server]

PLAY RECAP **********************************************************************************************************************************************************
web_server                 : ok=15   changed=5    unreachable=0    failed=0    skipped=2    rescued=0    ignored=0   
```