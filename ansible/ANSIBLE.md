# Ansible

## Best practices

- Assign unambiguous files.
- Comply with the lab's recommended file structure.
- Set up global preferences in ```ansible.cfg```.
- Use fully qualified collection names to avoid ambiguity.
## Outputs


```json
$ ansible-playbook playbooks/dev/main.yaml --diff
{
    "_meta": {
        "hostvars": {
            "ec2-3-124-209-126.eu-central-1.compute.amazonaws.com": {
                "ansible_connection": "ssh",
                "ansible_ssh_private_key_file": "~/.ssh/devops_new.pem",
                "ansible_user": "ubuntu"
            }
        }
    },
    "all": {
        "children": [
            "ungrouped"
        ]
    },
    "ungrouped": {
        "hosts": [
            "ec2-3-124-209-126.eu-central-1.compute.amazonaws.com"
        ]
    }
}
```
```ansible
$ ansible-playbook playbooks/dev/main.yaml --diff

PLAY [Install Docker] *********************************************************************************************************************
TASK [Gathering Facts] ***************************************************************************************************************************************
ok: [ec2-3-124-209-126.eu-central-1.compute.amazonaws.com]
TASK [../../roles/docker : Install pip] ********************************************************************************************************************
ok: [ec2-3-124-209-126.eu-central-1.compute.amazonaws.com]
TASK [../../roles/docker : Add user to docker group] *************************************************************************************************************
ok: [ec2-3-124-209-126.eu-central-1.compute.amazonaws.com]
TASK [../../roles/docker : Update packages] *********************************************************************************************************
ok: [ec2-3-124-209-126.eu-central-1.compute.amazonaws.com]
TASK [../../roles/docker : Install Docker] *******************************************************************************************************************
ok: [ec2-3-124-209-126.eu-central-1.compute.amazonaws.com]
TASK [../../roles/docker : Install Docker Compose] ***********************************************************************************************************
ok: [ec2-3-124-209-126.eu-central-1.compute.amazonaws.com]
PLAY RECAP ***************************************************************************************************************************************************
ec2-3-124-209-126.eu-central-1.compute.amazonaws.com : ok=6    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0  
ansible-inventory -i ./ansible/inventory/default_aws_ec2.yml --list
```

## Application Deployment

### Python App

```ansible
$ ansible-playbook playbooks/dev/app_python/main.yaml --diff

PLAY [Deploy Python App] ****************************************************************************************************************************************************************************

TASK [Gathering Facts] ******************************************************************************************************************************************************************************
ok: [ec2-3-124-209-126.eu-central-1.compute.amazonaws.com]
TASK [../../roles/docker : Install PIP] *************************************************************************************************************************************************************************
ok: [ec2-3-124-209-126.eu-central-1.compute.amazonaws.com]
TASK [../../roles/docker : Update apt] **************************************************************************************************************************************************************************
changed: [ec2-3-124-209-126.eu-central-1.compute.amazonaws.com]
TASK [../../roles/docker : Install Python] **********************************************************************************************************************************************************************
ok: [ec2-3-124-209-126.eu-central-1.compute.amazonaws.com]
TASK [../../roles/docker : Install PIP] *************************************************************************************************************************************************************************
ok: [ec2-3-124-209-126.eu-central-1.compute.amazonaws.com]
TASK [../../roles/docker : Install Docker] **********************************************************************************************************************************************************************
ok: [ec2-3-124-209-126.eu-central-1.compute.amazonaws.com]
TASK [../../roles/docker : Update apt] **************************************************************************************************************************************************************************
changed: [ec2-3-124-209-126.eu-central-1.compute.amazonaws.com]
TASK [../../roles/docker : Add Docker's GPG key] ****************************************************************************************************************************************************************
ok: [ec2-3-124-209-126.eu-central-1.compute.amazonaws.com]
TASK [../../roles/docker : Add Docker Repo] ***************************************************************************************************************************************************************
ok: [ec2-3-124-209-126.eu-central-1.compute.amazonaws.com]
TASK [../../roles/docker : Install Docker] **********************************************************************************************************************************************************************
ok: [ec2-3-124-209-126.eu-central-1.compute.amazonaws.com]
TASK [../../roles/docker : Install Docker Compose] **************************************************************************************************************************************************************
ok: [ec2-3-124-209-126.eu-central-1.compute.amazonaws.com]
TASK [../../roles/docker : Install Docker Compose] **************************************************************************************************************************************************************
ok: [ec2-3-124-209-126.eu-central-1.compute.amazonaws.com]
TASK [../../roles/web_app : Remove app container] ***********************************************************************************************************************************************************
changed: [ec2-3-124-209-126.eu-central-1.compute.amazonaws.com]
TASK [../../roles/web_app : Remove directory] ***************************************************************************************************************************************************************
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
changed: [ec2-3-124-209-126.eu-central-1.compute.amazonaws.com]
TASK [../../roles/web_app : Create app directory] *******************************************************************************************************************************************************
--- before
+++ after
@@ -1,4 +1,4 @@
 {
     "path": "/app_python",
-    "state": "absent"
+    "state": "directory"
 }
changed: [ec2-3-124-209-126.eu-central-1.compute.amazonaws.com]
TASK [ec2-3-124-209-126.eu-central-1.compute.amazonaws.com : Generate Docker Compose] ************************************************************************************************************************************************************
--- before
+++ after: /home/Laith/.ansible/tmp/ansible-local-12587a0d8luwj/tmps76ywa_m/docker-compose.yml.j2
@@ -0,0 +1,5 @@
+services:
+  web_app:
+    image: "LaithAlebrahim/app-python:latest"
+    ports:
+      - "8000:8000"
\ No newline at end of file
changed: [ec2-3-124-209-126.eu-central-1.compute.amazonaws.com]
TASK [../../roles/web_app : Start the app] **********************************************************************************************************************************************************************
changed: [ec2-3-124-209-126.eu-central-1.compute.amazonaws.com]
PLAY RECAP ******************************************************************************************************************************************************************************************
ec2-3-124-209-126.eu-central-1.compute.amazonaws.com : ok=10   changed=7    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0    
```


### JS App
```ansible
$ ansible-playbook playbooks/dev/app_js/main.yaml --diff
PLAY [Deploy JS app] **********************************************************************************************************************************************
TASK [Gathering Facts] **********************************************************************************************************************************************
ok: [ec2-3-124-209-126.eu-central-1.compute.amazonaws.com]
TASK [../../roles/docker : Install pip] *****************************************************************************************************************************************
ok: [ec2-3-124-209-126.eu-central-1.compute.amazonaws.com]
TASK [../../roles/docker : Update apt] ******************************************************************************************************************************************
changed: [ec2-3-124-209-126.eu-central-1.compute.amazonaws.com]
TASK [../../roles/docker : Install python] **************************************************************************************************************************************
ok: [ec2-3-124-209-126.eu-central-1.compute.amazonaws.com]
TASK [../../roles/docker : Install PIP] *****************************************************************************************************************************************
ok: [ec2-3-124-209-126.eu-central-1.compute.amazonaws.com]
TASK [../../roles/docker : Install Docker] **************************************************************************************************************************************
ok: [ec2-3-124-209-126.eu-central-1.compute.amazonaws.com]
TASK [docker : Update apt] ******************************************************************************************************************************************
changed: [ec2-3-124-209-126.eu-central-1.compute.amazonaws.com]
TASK [../../roles/docker : Add Docker's GPG key] ********************************************************************************************************************************
ok: [ec2-3-124-209-126.eu-central-1.compute.amazonaws.com]
TASK [../../roles/docker : Add Docker Repo] *******************************************************************************************************************************
ok: [ec2-3-124-209-126.eu-central-1.compute.amazonaws.com]
TASK [../../roles/docker : Install Docker] **************************************************************************************************************************************
ok: [ec2-3-124-209-126.eu-central-1.compute.amazonaws.com]
TASK [../../roles/docker : Install Docker Compose] ******************************************************************************************************************************
ok: [ec2-3-124-209-126.eu-central-1.compute.amazonaws.com]
TASK [../../roles/docker : Install Docker Compose] ******************************************************************************************************************************
ok: [ec2-3-124-209-126.eu-central-1.compute.amazonaws.com]
TASK [../../roles/web_app : Remove app container] ***************************************************************************************************************************
skipping: [ec2-3-124-209-126.eu-central-1.compute.amazonaws.com]
TASK [../../roles/web_app : Remove directory] *******************************************************************************************************************************
skipping: [ec2-3-124-209-126.eu-central-1.compute.amazonaws.com]
TASK [../../roles/web_app : Create app directory] ***********************************************************************************************************************
--- before
+++ after
@@ -1,4 +1,4 @@
 {
     "path": "/app_js",
-    "state": "absent"
+    "state": "directory"
 }
changed: [ec2-3-124-209-126.eu-central-1.compute.amazonaws.com]
TASK [../../roles/web_app : Generate docker-compose] ****************************************************************************************************************************
--- before
+++ after: /home/Laith/.ansible/tmp/ansible-local-132885ve9xqdo/tmp8ukznni9/docker-compose.yml.j2
@@ -0,0 +1,5 @@
+services:
+  web_app:
+    image: "LaithAlebrahim/app-js:latest"
+    ports:
+      - "8080:80"
\ No newline at end of file
changed: [ec2-3-124-209-126.eu-central-1.compute.amazonaws.com]
TASK [../../roles/web_app : Start the app] **************************************************************************************************************************************
changed: [ec2-3-124-209-126.eu-central-1.compute.amazonaws.com]
PLAY RECAP **********************************************************************************************************************************************************
ec2-3-124-209-126.eu-central-1.compute.amazonaws.com : ok=10   changed=5    unreachable=0    failed=0    skipped=2    rescued=0    ignored=0   

```