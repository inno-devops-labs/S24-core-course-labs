# Ansible Documentation

## Prerequisites
Ansible should be installed.

## Creating a custom docker role
For creating a custom docker role, I used `ansible-galaxy init ansible/roles/docker`
Then I wrote tasks for the role: installing pip, docker, docker-compose


## Running a Playbook
Execute the playbook:

```bash
ansible-playbook ansible/playbooks/dev/main.yaml
```

## Output of --diff

```[WARNING]: No inventory was parsed, only implicit localhost is available
[WARNING]: provided hosts list is empty, only localhost is available. Note that the implicit localhost does not match 'all'

PLAY [localhost] ********************************************************************************************************************

TASK [Gathering Facts] **************************************************************************************************************
ok: [localhost]

TASK [../../roles/docker : Install pip] *********************************************************************************************
ok: [localhost]

TASK [../../roles/docker : include_tasks] *******************************************************************************************
included: /mnt/c/Users/almet/S24-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for localhost

TASK [../../roles/docker : Install Docker packages] *********************************************************************************
ok: [localhost] => (item=docker-ce)
ok: [localhost] => (item=docker-ce-cli)
ok: [localhost] => (item=docker-ce-rootless-extras)

TASK [../../roles/docker : include_tasks] *******************************************************************************************
included: /mnt/c/Users/almet/S24-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for localhost

TASK [../../roles/docker : Install Docker Compose using pip] ************************************************************************
ok: [localhost]

TASK [Pull default Docker image] ****************************************************************************************************
changed: [localhost]

TASK [Run docker container] *********************************************************************************************************
changed: [localhost]

PLAY RECAP **************************************************************************************************************************
localhost                  : ok=8    changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

## Output of ansible-inventory
I used localhost

```
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

## Output of deploying
```
TASK [../../roles/web_app : Create Docker container] ********************************************************************************
task path: /mnt/c/Users/almet/S24-core-course-labs/ansible/roles/web_app/tasks/main.yml:6
redirecting (type: modules) ansible.builtin.docker_container to community.docker.docker_container
<127.0.0.1> ESTABLISH LOCAL CONNECTION FOR USER: kamil
<127.0.0.1> EXEC /bin/sh -c 'echo ~kamil && sleep 0'
<127.0.0.1> EXEC /bin/sh -c '( umask 77 && mkdir -p "` echo /home/kamil/.ansible/tmp `"&& mkdir "` echo /home/kamil/.ansible/tmp/ansible-tmp-1710318592.8065596-17714-264406928006880 `" && echo ansible-tmp-1710318592.8065596-17714-264406928006880="` echo /home/kamil/.ansible/tmp/ansible-tmp-1710318592.8065596-17714-264406928006880 `" ) && sleep 0'
redirecting (type: modules) ansible.builtin.docker_container to community.docker.docker_container
Using module file /home/kamil/.local/share/pipx/venvs/ansible/lib/python3.10/site-packages/ansible_collections/community/docker/plugins/modules/docker_container.py
<127.0.0.1> PUT /home/kamil/.ansible/tmp/ansible-local-17343rmlqo2bq/tmp2f3ygjvd TO /home/kamil/.ansible/tmp/ansible-tmp-1710318592.8065596-17714-264406928006880/AnsiballZ_docker_container.py
<127.0.0.1> EXEC /bin/sh -c 'chmod u+x /home/kamil/.ansible/tmp/ansible-tmp-1710318592.8065596-17714-264406928006880/ /home/kamil/.ansible/tmp/ansible-tmp-1710318592.8065596-17714-264406928006880/AnsiballZ_docker_container.py && sleep 0'
<127.0.0.1> EXEC /bin/sh -c 'sudo -H -S -n  -u root /bin/sh -c '"'"'echo BECOME-SUCCESS-spknfftxqlgekwggeupobkknapbpuwxc ; /home/kamil/.local/share/pipx/venvs/ansible/bin/python /home/kamil/.ansible/tmp/ansible-tmp-1710318592.8065596-17714-264406928006880/AnsiballZ_docker_container.py'"'"' && sleep 0'
<127.0.0.1> EXEC /bin/sh -c 'rm -f -r /home/kamil/.ansible/tmp/ansible-tmp-1710318592.8065596-17714-264406928006880/ > /dev/null 2>&1 && sleep 0'
ok: [localhost] => {
    "changed": false,
    "container": {
        "AppArmorProfile": "",
        "Args": [
            "app.py"
        ],
        "Config": {
            "AttachStderr": true,
            "AttachStdin": false,
            "AttachStdout": true,
            "Cmd": null,
            "Domainname": "",
            "Entrypoint": [
                "python3",
                "app.py"
            ],
            "Env": [
                "PATH=/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
                "LANG=C.UTF-8",
                "GPG_KEY=7169605F62C751356D054A26A821E680E5FA6305",
                "PYTHON_VERSION=3.12.2",
                "PYTHON_PIP_VERSION=24.0",
                "PYTHON_GET_PIP_URL=https://github.com/pypa/get-pip/raw/dbf0c85f76fb6e1ab42aa672ffca6f0a675d9ee4/public/get-pip.py", 
                "PYTHON_GET_PIP_SHA256=dfe9fd5c28dc98b5ac17979a953ea550cec37ae1b47a5116007395bfacff2ab9"
            ],
            "ExposedPorts": {
                "5000/tcp": {}
            },
            "Hostname": "cee977b9691b",
            "Image": "almetovkamil/app_python:v2",
            "Labels": {
                "desktop.docker.io/wsl-distro": "Ubuntu",
                "maintainer": "almetov.kamil@gmail.com"
            },
            "OnBuild": null,
            "OpenStdin": false,
            "StdinOnce": false,
            "Tty": false,
            "User": "nobody",
            "Volumes": null,
            "WorkingDir": "/app_python"
        },
        "Created": "2024-03-13T08:22:42.804390986Z",
        "Driver": "overlay2",
        "ExecIDs": null,
        "GraphDriver": {
            "Data": {
                "LowerDir": "/var/lib/docker/overlay2/a9be63b5f2d7c156120fa0a7661444f23818de26cd859a390f95230d631867dc-init/diff:/var/lib/docker/overlay2/5ou3x38k3gsk7i5n1vd89qnvm/diff:/var/lib/docker/overlay2/q0wi07ic73ikxhpyttney921i/diff:/var/lib/docker/overlay2/gpypx3isosaph1apuwbxnf9eq/diff:/var/lib/docker/overlay2/0njtfryacen3q8o1apg0etl7r/diff:/var/lib/docker/overlay2/sudxv27rhawjy0g3e41n257cz/diff:/var/lib/docker/overlay2/5e000530e4c5f53b6446d3b04b63111725f083a3e3567beceb267a94c36e7a4f/diff:/var/lib/docker/overlay2/32c4c250726737f7ad3b21b1b88de3d71fc17cc61729cddb67781e9db528da19/diff:/var/lib/docker/overlay2/e344964b824a03251dfea5d8f06029e8fc945002f62dd0482313a4dc0c511ada/diff:/var/lib/docker/overlay2/984babfb9d7fc7264ad8b252328bd7443a07bed3bd05176323b35aa05801927e/diff:/var/lib/docker/overlay2/22262044f7138e5d3e162630a9509d30e1cab0b07a695b21ba1da77eb88d9fab/diff",
                "MergedDir": "/var/lib/docker/overlay2/a9be63b5f2d7c156120fa0a7661444f23818de26cd859a390f95230d631867dc/merged",     
                "UpperDir": "/var/lib/docker/overlay2/a9be63b5f2d7c156120fa0a7661444f23818de26cd859a390f95230d631867dc/diff",        
                "WorkDir": "/var/lib/docker/overlay2/a9be63b5f2d7c156120fa0a7661444f23818de26cd859a390f95230d631867dc/work"
            },
            "Name": "overlay2"
        },
        "HostConfig": {
            "AutoRemove": false,
            "Binds": null,
            "BlkioDeviceReadBps": null,
            "BlkioDeviceReadIOps": null,
            "BlkioDeviceWriteBps": null,
            "BlkioDeviceWriteIOps": null,
            "BlkioWeight": 0,
            "BlkioWeightDevice": null,
            "CapAdd": null,
            "CapDrop": null,
            "Cgroup": "",
            "CgroupParent": "",
            "CgroupnsMode": "host",
            "ConsoleSize": [
                0,
                0
            ],
            "ContainerIDFile": "",
            "CpuCount": 0,
            "CpuPercent": 0,
            "CpuPeriod": 0,
            "CpuQuota": 0,
            "CpuRealtimePeriod": 0,
            "CpuRealtimeRuntime": 0,
            "CpuShares": 0,
            "CpusetCpus": "",
            "CpusetMems": "",
            "DeviceCgroupRules": null,
            "DeviceRequests": null,
            "Devices": null,
            "Dns": null,
            "DnsOptions": null,
            "DnsSearch": null,
            "ExtraHosts": null,
            "GroupAdd": null,
            "IOMaximumBandwidth": 0,
            "IOMaximumIOps": 0,
            "IpcMode": "private",
            "Isolation": "",
            "Links": null,
            "LogConfig": {
                "Config": {},
                "Type": "json-file"
            },
            "MaskedPaths": [
                "/proc/asound",
                "/proc/acpi",
                "/proc/kcore",
                "/proc/keys",
                "/proc/latency_stats",
                "/proc/timer_list",
                "/proc/timer_stats",
                "/proc/sched_debug",
                "/proc/scsi",
                "/sys/firmware",
                "/sys/devices/virtual/powercap"
            ],
            "Memory": 0,
            "MemoryReservation": 0,
            "MemorySwap": 0,
            "MemorySwappiness": null,
            "NanoCpus": 0,
            "NetworkMode": "default",
            "OomKillDisable": false,
            "OomScoreAdj": 0,
            "PidMode": "",
            "PidsLimit": null,
            "PortBindings": {
                "5000/tcp": [
                    {
                        "HostIp": "0.0.0.0",
                        "HostPort": "5000"
                    }
                ]
            },
            "Privileged": false,
            "PublishAllPorts": false,
            "ReadonlyPaths": [
                "/proc/bus",
                "/proc/fs",
                "/proc/irq",
                "/proc/sys",
                "/proc/sysrq-trigger"
            ],
            "ReadonlyRootfs": false,
            "RestartPolicy": {
                "MaximumRetryCount": 0,
                "Name": "no"
            },
            "Runtime": "runc",
            "SecurityOpt": null,
            "ShmSize": 67108864,
            "UTSMode": "",
            "Ulimits": null,
            "UsernsMode": "",
            "VolumeDriver": "",
            "VolumesFrom": null
        },
        "HostnamePath": "/var/lib/docker/containers/cee977b9691bc75db4865d1fadca1a917a24636ae83a1706641a635fb7732eba/hostname",      
        "HostsPath": "/var/lib/docker/containers/cee977b9691bc75db4865d1fadca1a917a24636ae83a1706641a635fb7732eba/hosts",
        "Id": "cee977b9691bc75db4865d1fadca1a917a24636ae83a1706641a635fb7732eba",
        "Image": "sha256:6079a54b6ea85a1c1d5faa92453d2e5ab0fd1e7361c4a52b9238fc1c5f1f132e",
        "LogPath": "/var/lib/docker/containers/cee977b9691bc75db4865d1fadca1a917a24636ae83a1706641a635fb7732eba/cee977b9691bc75db4865d1fadca1a917a24636ae83a1706641a635fb7732eba-json.log",
        "MountLabel": "",
        "Mounts": [],
        "Name": "/app_python",
        "NetworkSettings": {
            "Bridge": "",
            "EndpointID": "818facd03b139c69e6efcc64050bc9a3c8592f4c7f5373f067ed2276b2ee27b1",
            "Gateway": "172.17.0.1",
            "GlobalIPv6Address": "",
            "GlobalIPv6PrefixLen": 0,
            "HairpinMode": false,
            "IPAddress": "172.17.0.2",
            "IPPrefixLen": 16,
            "IPv6Gateway": "",
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "MacAddress": "02:42:ac:11:00:02",
            "Networks": {
                "bridge": {
                    "Aliases": null,
                    "DNSNames": null,
                    "DriverOpts": null,
                    "EndpointID": "818facd03b139c69e6efcc64050bc9a3c8592f4c7f5373f067ed2276b2ee27b1",
                    "Gateway": "172.17.0.1",
                    "GlobalIPv6Address": "",
                    "GlobalIPv6PrefixLen": 0,
                    "IPAMConfig": null,
                    "IPAddress": "172.17.0.2",
                    "IPPrefixLen": 16,
                    "IPv6Gateway": "",
                    "Links": null,
                    "MacAddress": "02:42:ac:11:00:02",
                    "NetworkID": "a3a04a09b5dbfe1429c5e8ba735f14259cdd8ad3cf6b44ccb0538ac697dbd009"
                }
            },
            "Ports": {
                "5000/tcp": [
                    {
                        "HostIp": "0.0.0.0",
                        "HostPort": "5000"
                    }
                ]
            },
            "SandboxID": "a114317938965233dc72311e6d9cab2b695a25a7dee5aeb886137ebce15404a6",
            "SandboxKey": "/var/run/docker/netns/a11431793896",
            "SecondaryIPAddresses": null,
            "SecondaryIPv6Addresses": null
        },
        "Path": "python3",
        "Platform": "linux",
        "ProcessLabel": "",
        "ResolvConfPath": "/var/lib/docker/containers/cee977b9691bc75db4865d1fadca1a917a24636ae83a1706641a635fb7732eba/resolv.conf", 
        "RestartCount": 0,
        "State": {
            "Dead": false,
            "Error": "",
            "ExitCode": 0,
            "FinishedAt": "0001-01-01T00:00:00Z",
            "OOMKilled": false,
            "Paused": false,
            "Pid": 1553,
            "Restarting": false,
            "Running": true,
            "StartedAt": "2024-03-13T08:22:43.370238097Z",
            "Status": "running"
        }
    },
    "invocation": {
        "module_args": {
            "api_version": "auto",
            "auto_remove": null,
            "blkio_weight": null,
            "ca_path": null,
            "cap_drop": null,
            "capabilities": null,
            "cgroup_parent": null,
            "cgroupns_mode": null,
            "cleanup": false,
            "client_cert": null,
            "client_key": null,
            "command": null,
            "command_handling": "correct",
            "comparisons": null,
            "container_default_behavior": "no_defaults",
            "cpu_period": null,
            "cpu_quota": null,
            "cpu_shares": null,
            "cpus": null,
            "cpuset_cpus": null,
            "cpuset_mems": null,
            "debug": false,
            "default_host_ip": null,
            "detach": null,
            "device_read_bps": null,
            "device_read_iops": null,
            "device_requests": null,
            "device_write_bps": null,
            "device_write_iops": null,
            "devices": null,
            "dns_opts": null,
            "dns_search_domains": null,
            "dns_servers": null,
            "docker_host": "unix:///var/run/docker.sock",
            "domainname": null,
            "entrypoint": null,
            "env": null,
            "env_file": null,
            "etc_hosts": null,
            "exposed_ports": null,
            "force_kill": false,
            "groups": null,
            "healthcheck": null,
            "hostname": null,
            "ignore_image": false,
            "image": "almetovkamil/app_python:v2",
            "image_comparison": "desired-image",
            "image_label_mismatch": "ignore",
            "image_name_mismatch": null,
            "init": null,
            "interactive": null,
            "ipc_mode": null,
            "keep_volumes": true,
            "kernel_memory": null,
            "kill_signal": null,
            "labels": null,
            "links": null,
            "log_driver": null,
            "log_options": null,
            "mac_address": null,
            "memory": null,
            "memory_reservation": null,
            "memory_swap": null,
            "memory_swappiness": null,
            "mounts": null,
            "name": "app_python",
            "network_mode": null,
            "networks": null,
            "networks_cli_compatible": true,
            "oom_killer": null,
            "oom_score_adj": null,
            "output_logs": false,
            "paused": null,
            "pid_mode": null,
            "pids_limit": null,
            "platform": null,
            "ports": [
                "5000:5000"
            ],
            "privileged": null,
            "publish_all_ports": null,
            "published_ports": [
                "5000:5000"
            ],
            "pull": "missing",
            "pull_check_mode_behavior": "image_not_present",
            "purge_networks": false,
            "read_only": null,
            "recreate": false,
            "removal_wait_timeout": null,
            "restart": false,
            "restart_policy": null,
            "restart_retries": null,
            "runtime": null,
            "security_opts": null,
            "shm_size": null,
            "ssl_version": null,
            "state": "started",
            "stop_signal": null,
            "stop_timeout": null,
            "storage_opts": null,
            "sysctls": null,
            "timeout": 60,
            "tls": false,
            "tls_hostname": null,
            "tmpfs": null,
            "tty": null,
            "ulimits": null,
            "use_ssh_client": false,
            "user": null,
            "userns_mode": null,
            "uts": null,
            "validate_certs": false,
            "volume_driver": null,
            "volumes": null,
            "volumes_from": null,
            "working_dir": null
        }
    }
}

TASK [../../roles/web_app : include_tasks] ******************************************************************************************
task path: /mnt/c/Users/almet/S24-core-course-labs/ansible/roles/web_app/tasks/main.yml:14
redirecting (type: modules) ansible.builtin.docker_container to community.docker.docker_container
redirecting (type: modules) ansible.builtin.docker_container to community.docker.docker_container
included: /mnt/c/Users/almet/S24-core-course-labs/ansible/roles/web_app/tasks/0-wipe.yml for localhost

TASK [../../roles/web_app : Stop Docker container] **********************************************************************************
task path: /mnt/c/Users/almet/S24-core-course-labs/ansible/roles/web_app/tasks/0-wipe.yml:4
skipping: [localhost] => {
    "changed": false,
    "false_condition": "web_app_full_wipe | default(false)",
    "skip_reason": "Conditional result was False"
}

TASK [../../roles/web_app : Remove Docker container] ********************************************************************************
task path: /mnt/c/Users/almet/S24-core-course-labs/ansible/roles/web_app/tasks/0-wipe.yml:9
skipping: [localhost] => {
    "changed": false,
    "false_condition": "web_app_full_wipe | default(false)",
    "skip_reason": "Conditional result was False"
}

TASK [../../roles/web_app : Delete related files (adjust paths as needed)] **********************************************************
task path: /mnt/c/Users/almet/S24-core-course-labs/ansible/roles/web_app/tasks/0-wipe.yml:14
skipping: [localhost] => {
    "changed": false,
    "false_condition": "web_app_full_wipe | default(false)",
    "skip_reason": "Conditional result was False"
}

PLAY RECAP **************************************************************************************************************************
localhost                  : ok=9    changed=1    unreachable=0    failed=0    skipped=3    rescued=0    ignored=0
```