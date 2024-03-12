# Ansible-related work 

## Best practices

1. Testing with Ansible linting: validating Ansible code using linting tools like ansible-lint. Linting helps identify potential issues, enforces best practices, and improves the overall quality of  automation code.
2. Using FQCN
3. Modular playbook structure: organizing playbook into logical module.

## Outputs of following commands:

`ansible-playbook playbooks/dev/playbook.yaml -i inventory/inventory.yaml --diff`

```
PLAY [Run Docker role] ***********************************************************************************************

TASK [Gathering Facts] ***********************************************************************************************
ok: [84.201.135.38]

TASK [docker : Install pip] ******************************************************************************************
ok: [84.201.135.38]

TASK [docker : Update repositories] **********************************************************************************
ok: [84.201.135.38]

TASK [docker : Install required packages] ****************************************************************************
ok: [84.201.135.38]

TASK [docker : Add GPG key] ******************************************************************************************
ok: [84.201.135.38]

TASK [docker : Add repository] ***************************************************************************************
ok: [84.201.135.38]

TASK [docker : Install Docker] ***************************************************************************************
ok: [84.201.135.38]

TASK [docker : Install Docker-Compose] *******************************************************************************
ok: [84.201.135.38]

PLAY RECAP ***********************************************************************************************************
84.201.135.38             : ok=8    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```

`ansible-inventory -i inventory/inventory.yaml --list`

```
{
    "_meta": {
        "hostvars": {
            "84.201.135.38": {
                "ansible_user": "hugowea"
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
            "84.201.135.38"
        ]
    }
}
```

## Development of new role called web_app

### Using command

``` bash
sudo ansible-playbook -i ansible/inventory/default_aws_ec2.yml ansible/playbooks/dev/main.yaml --diff
```

### Outputs:

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
+++ after: /Users/79393/.ansible/tmp/ansible-local-62375flsdk84mh/tmp8gr7h7ty/docker-compose.yml.j2
@@ -0,0 +1,5 @@
+services:
+  web_app:
+    image: hugowea123/devops-labs-py.py:latest
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