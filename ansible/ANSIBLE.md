## lab 5 output 
### ansible-playbook playbooks/dev/main.yml

```
PLAY [all] **********************************************************************************************

TASK [Gathering Facts] **********************************************************************************
ok: [host_01]

TASK [docker : Install `pip`] ***************************************************************************
ok: [host_01]

TASK [docker : Install Docker] **************************************************************************
changed: [host_01]

TASK [docker : Install Docker Compose] ******************************************************************
changed: [host_01]

PLAY RECAP **********************************************************************************************
host_01                    : ok=4    changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```

### ansible-inventory -i inventory/default_yc_ec2.yml --list

```
{
    "_meta": {
        "hostvars": {
            "host_01": {
                "ansible_connection": "ssh",
                "ansible_host": "62.84.117.83",
                "ansible_ssh_private_key_file": "~/.ssh/id_rsa",
                "ansible_user": "maintheme"
            }
        }
    },
    "all": {
        "children": [
            "ungrouped",
            "selfhosts"
        ]
    },
    "selfhosts": {
        "hosts": [
            "host_01"
        ]
    }
}
```
The connection to host 62.84.117.83 is done via ssh and get the key from .ssh/id_rsa file. The host belongs to selfhosts group.

## lab 6 output
### ansible-playbook playbooks/dev/main.yml --diff
```
requirements

PLAY [all] **********************************************************************************************

TASK [Gathering Facts] **********************************************************************************
ok: [host_01]

TASK [docker : Update apt package cache] ****************************************************************
changed: [host_01]

TASK [docker : Install dependencies] ********************************************************************
ok: [host_01]

TASK [docker : Add Docker GPG key] **********************************************************************
ok: [host_01]

TASK [docker : Add Docker APT repository] ***************************************************************
ok: [host_01]

TASK [docker : Update apt package cache (again)] ********************************************************
changed: [host_01]

TASK [docker : Install Docker] **************************************************************************
ok: [host_01]

TASK [docker : Install Docker Compose] ******************************************************************
ok: [host_01]

TASK [docker : Add user to the docker group] ************************************************************
ok: [host_01]

TASK [docker : Enable and start Docker services] ********************************************************
ok: [host_01] => (item=docker.service)
ok: [host_01] => (item=containerd.service)

TASK [docker : Ensure docker deamon is running] *********************************************************
ok: [host_01]

TASK [web_app : Stop and remove flask-msktime-app] ******************************************************
skipping: [host_01]

TASK [web_app : get docker-compose file] ****************************************************************
ok: [host_01]

TASK [web_app : pull image] *****************************************************************************
ok: [host_01]

TASK [web_app : start container] ************************************************************************
--- before
+++ after
@@ -1,4 +1,4 @@
 {
-    "exists": false,
-    "running": false
+    "exists": true,
+    "running": true
 }

changed: [host_01]

PLAY RECAP **********************************************************************************************
host_01                    : ok=14   changed=3    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0  
```

### docker ps inside VM:
```
CONTAINER ID   IMAGE                            COMMAND                  CREATED         STATUS         PORTS     NAMES
eb33caf3a472   maintheme/flask-msktime-app:v1   "python -m flask run…"   3 minutes ago   Up 3 minutes             flask-msktime-app
```

### ansible-playbook --extra-vars '{"web_app_full_wipe": true}' --tag wipe-app-python playbooks/dev/main.yml
```
PLAY [all] *****************************************************************************************************************************

TASK [Gathering Facts] *****************************************************************************************************************
ok: [host_01]

TASK [web_app : Stop and remove flask-msktime-app] *************************************************************************************
changed: [host_01]

PLAY RECAP *****************************************************************************************************************************
host_01                    : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0  
```

### docker ps inside VM:
```
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
```