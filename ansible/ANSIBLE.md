# Ansible

Originally, I used the `geerlingguy.docker` role. Then I created the custom
Docker role, closely following the [official installation guide for
Docker][docker]. I implemented the following best practices:

- Use fully qualified collection names;
- Always mention the state;
- Always name tasks.

[docker]: https://docs.docker.com/engine/install/ubuntu/

## Deployment output

Please note that I deployed the existing role before this one.

```
$ ansible-playbook playbooks/dev/main.yml -i inventory

PLAY [all] *****************************************************************************************

TASK [Gathering Facts] *****************************************************************************
ok: [158.160.124.228]

TASK [../../roles/docker : Install `pip`] **********************************************************
ok: [158.160.124.228]

TASK [../../roles/docker : Install required system packages] ***************************************
ok: [158.160.124.228]

TASK [../../roles/docker : Add Docker's GPG key] ***************************************************
ok: [158.160.124.228]

TASK [../../roles/docker : Add Docker Repository] **************************************************
ok: [158.160.124.228]

TASK [../../roles/docker : Install Docker] *********************************************************
ok: [158.160.124.228]

TASK [../../roles/docker : Install Docker Compose] *************************************************
changed: [158.160.124.228]

PLAY RECAP *****************************************************************************************
158.160.124.228            : ok=7    changed=1    unreachable=0    failed=0    skipped=0    rescued=
0    ignored=0
```

## Inventory Details

```
$ ansible-inventory -i inventory --list
{
    "_meta": {
        "hostvars": {
            "158.160.124.228": {
                "ansible_user": "ubuntu"
            }
        }
    },
    "all": {
        "children": [
            "ungrouped",
            "yandex_cloud"
        ]
    },
    "yandex_cloud": {
        "hosts": [
            "158.160.124.228"
        ]
    }
}
```

## Python application deployment

```
$ ansible-playbook -i inventory playbooks/dev/main.yml

PLAY [all] *********************************************************************

TASK [Gathering Facts] *********************************************************
ok: [devops-lab-4-cloud]

TASK [../../roles/docker : Install `pip`] **************************************
ok: [devops-lab-4-cloud]

TASK [../../roles/docker : Install required system packages] *******************
ok: [devops-lab-4-cloud]

TASK [../../roles/docker : Add Docker's GPG key] *******************************
ok: [devops-lab-4-cloud]

TASK [../../roles/docker : Add Docker Repository] ******************************
ok: [devops-lab-4-cloud]

TASK [../../roles/docker : Install Docker] *************************************
ok: [devops-lab-4-cloud]

TASK [../../roles/docker : Install Docker Compose] *****************************
ok: [devops-lab-4-cloud]

TASK [../../roles/web_app : Pull the app image] ********************************
changed: [devops-lab-4-cloud]

TASK [../../roles/web_app : Start the app] *************************************
changed: [devops-lab-4-cloud]

PLAY RECAP *********************************************************************
devops-lab-4-cloud         : ok=9    changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```
