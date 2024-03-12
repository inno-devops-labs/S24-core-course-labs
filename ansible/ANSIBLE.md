# Ansible configuration results
- Yandex cloud server
- Config in the inventory 
- Configuring of `ansible.cfg`

## Deployment Output
```bash
PLAY [Install docker] **************************************************************************************************
TASK [Gathering Facts] *************************************************************************************************
ok: [devops]
TASK [/Users/i-pechersky/DevOps/S24-core-course-labs/ansible/roles/docker : install `pip`] ***
ok: [devops]
TASK [/Users/i-pechersky/DevOps/S24-core-course-labs/ansible/roles/docker : refresh apt packages] ***
ok: [devops]
TASK [/Users/i-pechersky/DevOps/S24-core-course-labs/ansible/roles/docker : update docker.io] ***
ok: [devops]
TASK [/Users/i-pechersky/DevOps/S24-core-course-labs/ansible/roles/docker : install docker] ***
ok: [devops]
TASK [/Users/i-pechersky/DevOps/S24-core-course-labs/ansible/roles/docker : install docker-compose] ***
ok: [devops]
PLAY RECAP ***
devops                     : ok=6    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

## Details
```bash
{
    "_meta": {
        "hostvars": {
            "devops": {
                "ansible_connection": "ssh",
                "ansible_host": "158.160.60.140",
                "ansible_ssh_private_key_file": "~/.ssh/id_ed25519",
                "ansible_user": "pechersky"
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
            "devops"
        ]
    }
}
```

## Best practices:
- Using ansible.cfg configuration
- Proper structure


## Ansible role web_app output
```bash
sudo ansible-playbook -i ansible/inventory/default_aws_ec2.yml ansible/playbooks/dev/main.yaml --diff
PLAY [Install docker] **************************************************************************************************
TASK [Gathering Facts] *************************************************************************************************
ok: [devops]
TASK [/Users/i-pechersky/DevOps/S24-core-course-labs/ansible/roles/docker : install `pip`] ***
ok: [devops]
TASK [/Users/i-pechersky/DevOps/S24-core-course-labs/ansible/roles/docker : refresh apt packages] ***
ok: [devops]
TASK [/Users/i-pechersky/DevOps/S24-core-course-labs/ansible/roles/docker : update docker.io] ***
ok: [devops]
TASK [/Users/i-pechersky/DevOps/S24-core-course-labs/ansible/roles/docker : install docker] ***
ok: [devops]
TASK [/Users/i-pechersky/DevOps/S24-core-course-labs/ansible/roles/docker : install docker-compose] ***
ok: [devops]
PLAY RECAP ***
devops                     : ok=6    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
--- before
+++ after: /Users/i-pechersky/.ansible/tmp/ansible-local-65365bgkf98wg/tmp9tj3a7ee/docker-compose.yml.j2
@@ -0,0 +1,5 @@
+services:
+  web_app:
+    image: app_python/app.py:latest
+    ports:
+      - 5000:5000
\ No newline at end of file
changed: [cloud_host]
TASK [../../roles/web_app : start docker] *****************************************************************************************************************
ok: [cloud_host]
TASK [../../roles/web_app : start services] ************************************************************************************************************
[WARNING]: Cannot parse event from line: "web_app The requested image's platform (linux/arm64/v8) does not match the detected host platform (linux/amd64/v4) and no
specific platform was requested". Please report this at https://github.com/ansible-
collections/community.docker/issues/new?assignees=&labels=&projects=&template=bug_report.md
changed: [cloud_host]
TASK [../../roles/web_app : shutdown web app] *****************************************************************************************************************
skipping: [cloud_host]
TASK [Install python3-pip package] ************************************************************************************************************************************
ok: [cloud_host]
PLAY RECAP ************************************************************************************************************************************************************
cloud_host                 : ok=13   changed=2    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0   
```
