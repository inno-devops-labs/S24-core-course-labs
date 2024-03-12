# Ansible

## Lab 6
- Deployment output

```bash
PLAY [webservers] **************************************************************

TASK [Gathering Facts] *********************************************************
ok: [80.76.60.143]

TASK [docker : Install pip] ****************************************************
ok: [80.76.60.143]

TASK [docker : Install Docker] *************************************************
ok: [80.76.60.143]

TASK [docker : Install Docker Compose] *****************************************
ok: [80.76.60.143]

TASK [web_app : Stop, remove a container moscow_time] **************************
skipping: [80.76.60.143]

TASK [web_app : Deliver docker compose] ****************************************
ok: [80.76.60.143]

TASK [web_app : Pull the image from Dockerhub] *********************************
ok: [80.76.60.143]

TASK [web_app : Run a container] ***********************************************
ok: [80.76.60.143]

PLAY RECAP *********************************************************************
80.76.60.143               : ok=7    changed=0    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0 
```

## Lab 5
- Deployment output

```bash
PLAY [webservers] **************************************************************

TASK [Gathering Facts] *********************************************************
ok: [51.250.10.101]

TASK [docker : Install pip] ****************************************************
ok: [51.250.10.101]

TASK [docker : Install Docker] *************************************************
ok: [51.250.10.101]

TASK [docker : Install Docker Compose] *****************************************
ok: [51.250.10.101]

PLAY RECAP *********************************************************************
51.250.10.101              : ok=4    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```

- There is one group name (webservers). It consists of one server with a custom variable server_name.
Inventory details are the following:

```bash
{
    "_meta": {
        "hostvars": {
            "51.250.10.101": {
                "server_name": "yandexcloud"
            }
        }
    },
    "all": {
        "children": [
            "ungrouped",
            "webservers"
        ]
    },
    "webservers": {
        "hosts": [
            "51.250.10.101"
        ]
    }
}
```
