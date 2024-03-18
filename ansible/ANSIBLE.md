# ANSIBLE

## Best practices
* ansible lint

## Outputs

```
ansible-playbook playbooks/dev/main.yaml -i inventory/default_aws_ec2.yaml --diff
```

```
PLAY [Run Docker role] ***********************************************************************************************

TASK [Gathering Facts] ***********************************************************************************************
ok: [51.15.48.52]

TASK [docker : Install pip] ******************************************************************************************
ok: [51.15.48.52]

TASK [docker : Update repositories] **********************************************************************************
ok: [51.15.48.52]

TASK [docker : Install required packages] ****************************************************************************
ok: [51.15.48.52]

TASK [docker : Add GPG key] ******************************************************************************************
ok: [51.15.48.52]

TASK [docker : Add repository] ***************************************************************************************
ok: [51.15.48.52]

TASK [docker : Install Docker] ***************************************************************************************
ok: [51.15.48.52]

TASK [docker : Install Docker-Compose] *******************************************************************************
ok: [51.15.48.52]

PLAY RECAP ***********************************************************************************************************
51.15.48.52             : ok=8    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```

```
ansible-inventory -i inventory/default_aws_ec2.yaml --list
```

```
{
    "_meta": {
        "hostvars": {
            "51.15.48.52": {
                "ansible_user": "grisharybolovlev"
            }
        }
    },
    "all": {
        "children": [
            "ungrouped",
            "myhost"
        ]
    },
    "myhost": {
        "hosts": [
            "51.15.48.52"
        ]
    }
}
```

## web_app role

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
+++ after: /Users/grisharybolovlev/.ansible/tmp/ansible-local-53782aqwod73mh/tmpddf4h9hg/docker-compose.yml.j2
@@ -0,0 +1,5 @@
+services:
+  web_app:
+    image: grisharybolovlev/devops.py:latest
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