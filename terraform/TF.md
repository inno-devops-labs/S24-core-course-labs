# Terraform Lab

## Overview

1. I have Terraform already installed on my machine, because I used it in Summer DevOps elective. File and the guide can be found [here](https://github.com/Ozurexus/DevOps-Labs-Summer/blob/lab5/lab5).

### terraform state list

```bash
docker_container.app_python
docker_image.app_python
```

### terraform state show docker_container.app_python

```bash
docker_container.app_python:

resource "docker_container" "app_python" {
attach = false
command = [
"python",
"-m",
"flask",
"run",
"--host",
"0.0.0.0",
]
container_read_refresh_timeout_milliseconds = 15000
cpu_shares = 0
entrypoint = []
env = []
hostname = "e5cffcced854"
id = "e5cffcced854e1efd75f65804f92a539e73e36b34cfabec9baf33806ff3c19a7"
image = "sha256:63b40cb5d53bdb70db72d9b7722b5417d27b33ebb1e8379130b17da6838c6d7f"
init = false
ipc_mode = "private"
log_driver = "json-file"
logs = false
max_retry_count = 0
memory = 0
memory_swap = 0
must_run = true
name = "app_python"
network_data = [
{
gateway = "172.17.0.1"
global_ipv6_address = ""
global_ipv6_prefix_length = 0
ip_address = "172.17.0.2"
ip_prefix_length = 16
ipv6_gateway = ""
mac_address = "02:42:ac:11:00:02"
network_name = "bridge"
},
]
network_mode = "default"
privileged = false
publish_all_ports = false
read_only = false
remove_volumes = true
restart = "no"
rm = false
runtime = "runc"
security_opts = []
shm_size = 64
start = true
stdin_open = false
stop_timeout = 0
tty = false
user = "user"
wait = false
wait_timeout = 60
working_dir = "/app_python"

    ports {
        external = 5000
        internal = 5000
        ip       = "0.0.0.0"
        protocol = "tcp"
    }

}
```

### terraform show

```bash
docker_container.app_python:

resource "docker_container" "app_python" {
attach = false
command = [
"python",
"-m",
"flask",
"run",
"--host",
"0.0.0.0",
]
container_read_refresh_timeout_milliseconds = 15000
cpu_shares = 0
entrypoint = []
env = []
hostname = "e5cffcced854"
id = "e5cffcced854e1efd75f65804f92a539e73e36b34cfabec9baf33806ff3c19a7"
image = "sha256:63b40cb5d53bdb70db72d9b7722b5417d27b33ebb1e8379130b17da6838c6d7f"
init = false
ipc_mode = "private"
log_driver = "json-file"
logs = false
max_retry_count = 0
memory = 0
memory_swap = 0
must_run = true
name = "app_python"
network_data = [
{
gateway = "172.17.0.1"
global_ipv6_address = ""
global_ipv6_prefix_length = 0
ip_address = "172.17.0.2"
ip_prefix_length = 16
ipv6_gateway = ""
mac_address = "02:42:ac:11:00:02"
network_name = "bridge"
},
]
network_mode = "default"
privileged = false
publish_all_ports = false
read_only = false
remove_volumes = true
restart = "no"
rm = false
runtime = "runc"
security_opts = []
shm_size = 64
start = true
stdin_open = false
stop_timeout = 0
tty = false
user = "user"
wait = false
wait_timeout = 60
working_dir = "/app_python"

    ports {
        external = 5000
        internal = 5000
        ip       = "0.0.0.0"
        protocol = "tcp"
    }

}

docker_image.app_python:

resource "docker_image" "app_python" {
id = "sha256:63b40cb5d53bdb70db72d9b7722b5417d27b33ebb1e8379130b17da6838c6d7fozurexus/my-flask-app"
image_id = "sha256:63b40cb5d53bdb70db72d9b7722b5417d27b33ebb1e8379130b17da6838c6d7f"
keep_locally = false
name = "ozurexus/my-flask-app"
repo_digest = "ozurexus/my-flask-app@sha256:208e30808a8f648850c1bb64e2cf5816642aa4263866d640f8e5c04e19195d83"
}
```

Outputs:

```bash
container_id = "e5cffcced854e1efd75f65804f92a539e73e36b34cfabec9baf33806ff3c19a7"
image_id = "sha256:63b40cb5d53bdb70db72d9b7722b5417d27b33ebb1e8379130b17da6838c6d7fozurexus/my-flask-app"

C:\Users\hp\Desktop\Progs\S24-DevOps-labs\terraform>terraform output
container_id = "e5cffcced854e1efd75f65804f92a539e73e36b34cfabec9baf33806ff3c19a7"
image_id = "sha256:63b40cb5d53bdb70db72d9b7722b5417d27b33ebb1e8379130b17da6838c6d7fozurexus/my-flask-app"
```

2. Due to issues with Yandex cloud, I was unable to create a VM and run Terraform on it. I was able to only create a VM.

    ![alt text](https://i.ibb.co/wrjwWL3/Yandex-Cloud.png)

3. I created github folder for Terraform and added the file with the code. I also applied **the best practices** for Terraform code.

## Best practices

1. The repository requires a merge request to merge the code into the main branch, therefore there is a **branch protection rule**.
2. **Personal access tokens** are used to authenticate with the GitHub API and are hidden from the code.
3. The code is stored in a **version control system** - GitHub.
4. Code has premade **gitingore** template.
