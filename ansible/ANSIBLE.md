# Ansible

---

## Docker Role

- To install `docker` I used `ansible.builtin.apt`
- To install `pip` I used `command` to execute `ansible.builtin.apt`
- To install `docker-compose` I imported `pip` and `docker` installation roles
- In `main.yaml` of my custom docker role I just imported all installation roles

## Playbook

- Importing role by passing relative path of the role
(with respect to `main.yml` of playbook)
- I used localhost as a host to test ansible locally
- Tasks for playbook are just pulling docker image and starting docker container

## Inventory

I didn't do anything with `ansible-inventory`

## Ansible Playbook Output (Deployment Output)

```
[WARNING]: No inventory was parsed, only implicit localhost is available
[WARNING]: provided hosts list is empty, only localhost is available. Note that the implicit localhost does not match 'all'
TASK [Gathering Facts] *******************************************************************************************************************************************************************
ok: [localhost]

TASK [../../roles/docker : Install pip] **************************************************************************************************************************************************
ok: [localhost]

TASK [../../roles/docker : Install docker] ***********************************************************************************************************************************************
ok: [localhost]

TASK [../../roles/docker : Install pip] **************************************************************************************************************************************************
ok: [localhost]

TASK [../../roles/docker : Install docker] ***********************************************************************************************************************************************
ok: [localhost]

TASK [../../roles/docker : command] ******************************************************************************************************************************************************
changed: [localhost]

TASK [Pull docker image] *****************************************************************************************************************************************************************
changed: [localhost]

TASK [Execute docker image] **************************************************************************************************************************************************************
```

## Inventory Details

```yaml
{
    "_meta": {
        "hostvars": {}
    },
    "all": {
        "children": [
            "ungrouped"
        ]
    }
}
```

I didn't do anything with inventory.
It should be default inventory