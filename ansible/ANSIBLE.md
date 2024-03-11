# Best practice

1. Named tasks properly

# Output
## Command 1
``` bash
sudo ansible-playbook -i ansible/inventory/default_aws_ec2.yml ansible/playbooks/dev/main.yaml --diff
```
```
PLAY [all] *********************************************************************

TASK [Gathering Facts] *********************************************************
ok: [cloud_host]

TASK [/Users/renathajrullin/DevOps/S24-core-course-labs/ansible/roles/docker : Install pip] ***
ok: [cloud_host]

TASK [/Users/renathajrullin/DevOps/S24-core-course-labs/ansible/roles/docker : Update repositories] ***
ok: [cloud_host]

TASK [/Users/renathajrullin/DevOps/S24-core-course-labs/ansible/roles/docker : Install required packages] ***
ok: [cloud_host]

TASK [/Users/renathajrullin/DevOps/S24-core-course-labs/ansible/roles/docker : Add GPG key] ***
ok: [cloud_host]

TASK [/Users/renathajrullin/DevOps/S24-core-course-labs/ansible/roles/docker : Add repository] ***
ok: [cloud_host]

TASK [/Users/renathajrullin/DevOps/S24-core-course-labs/ansible/roles/docker : Install Docker] ***
ok: [cloud_host]

TASK [/Users/renathajrullin/DevOps/S24-core-course-labs/ansible/roles/docker : Install Docker-Compose] ***
ok: [cloud_host]

TASK [Install python3-pip package] *********************************************
ok: [cloud_host]

PLAY RECAP *********************************************************************
cloud_host                 : ok=9    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```
## Command 2
``` bash
ansible-inventory -i ansible/inventory/default_aws_ec2.yml --list
```
```
{
    "_meta": {
        "hostvars": {
            "cloud_host": {
                "ansible_host": "158.160.149.60",
                "ansible_user": "snapman"
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
            "cloud_host"
        ]
    }
}
```

# New role web_app
## Command
``` bash
sudo ansible-playbook -i ansible/inventory/default_aws_ec2.yml ansible/playbooks/dev/main.yaml --diff
```

```
PLAY [all] ************************************************************************************************************************************************************

TASK [Gathering Facts] ************************************************************************************************************************************************
ok: [cloud_host]

TASK [docker : Install pip] *******************************************************************************************************************************************
ok: [cloud_host]

TASK [docker : Update repositories] ***********************************************************************************************************************************
ok: [cloud_host]

TASK [docker : Install required packages] *****************************************************************************************************************************
ok: [cloud_host]

TASK [docker : Add GPG key] *******************************************************************************************************************************************
ok: [cloud_host]

TASK [docker : Add repository] ****************************************************************************************************************************************
ok: [cloud_host]

TASK [docker : Install Docker] ****************************************************************************************************************************************
ok: [cloud_host]

TASK [docker : Install Docker-Compose] ********************************************************************************************************************************
ok: [cloud_host]

TASK [../../roles/web_app : Create app directory] *********************************************************************************************************************
ok: [cloud_host]

TASK [../../roles/web_app : Render compose template] ******************************************************************************************************************
--- before
+++ after: /Users/renathajrullin/.ansible/tmp/ansible-local-61455afhe95mh/tmp8th5h8ve/docker-compose.yml.j2
@@ -0,0 +1,5 @@
+services:
+  web_app:
+    image: snapman/time_web.py:latest
+    ports:
+      - 5000:5000
\ No newline at end of file

changed: [cloud_host]

TASK [../../roles/web_app : Ensure docker is running] *****************************************************************************************************************
ok: [cloud_host]

TASK [../../roles/web_app : Create and start the services] ************************************************************************************************************
[WARNING]: Cannot parse event from line: "web_app The requested image's platform (linux/arm64/v8) does not match the detected host platform (linux/amd64/v4) and no
specific platform was requested". Please report this at https://github.com/ansible-
collections/community.docker/issues/new?assignees=&labels=&projects=&template=bug_report.md
changed: [cloud_host]

TASK [../../roles/web_app : Wipe out web application] *****************************************************************************************************************
skipping: [cloud_host]

TASK [Install python3-pip package] ************************************************************************************************************************************
ok: [cloud_host]

PLAY RECAP ************************************************************************************************************************************************************
cloud_host                 : ok=13   changed=2    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0   
```