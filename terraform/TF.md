# Terraform

## Docker

### Output of `terraform state show`

```markdown
# docker_container.nginx:

resource "docker_container" "nginx" {
attach = false
command = [
"nginx",
"-g",
"daemon off;",
]
container_read_refresh_timeout_milliseconds = 15000
cpu_shares = 0
entrypoint = [
"/docker-entrypoint.sh",
]
env = []
hostname = "8162814cd1bc"
id = "8162814cd1bcdaf7f9f995b2a655eb28a7c41c2fc81046ac863e4f6d5f1e6bbf"
image = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666a"
init = false
ipc_mode = "private"
log_driver = "json-file"
logs = false
max_retry_count = 0
memory = 0
memory_swap = 0
must_run = true
name = "tutorial"
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
wait_timeout = 60

    ports {
        external = 8000
        internal = 80
        ip       = "0.0.0.0"
        protocol = "tcp"
    }

}

```

### Output of `terraform state list`

```markdown
docker_container.nginx
docker_image.nginx
```

### Output of `terraform apply` after changes

```markdown
docker_image.nginx: Refreshing
state... [id=sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666anginx:latest]
docker_container.nginx: Refreshing state... [id=8162814cd1bcdaf7f9f995b2a655eb28a7c41c2fc81046ac863e4f6d5f1e6bbf]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the
following symbols:
-/+ destroy and then create replacement

Terraform will perform the following actions:

# docker_container.nginx must be replaced

-/+ resource "docker_container" "nginx" {
+ bridge = (known after apply)
~ command = [
- "nginx",
- "-g",
- "daemon off;",
] -> (known after apply)
+ container_logs = (known after apply)
- cpu_shares = 0 -> null
- dns = [] -> null
- dns_opts = [] -> null
- dns_search = [] -> null
~ entrypoint = [
- "/docker-entrypoint.sh",
] -> (known after apply)
~ env = [] -> (known after apply)
+ exit_code = (known after apply)
- group_add = [] -> null
~ hostname = "8162814cd1bc" -> (known after apply)
~ id = "8162814cd1bcdaf7f9f995b2a655eb28a7c41c2fc81046ac863e4f6d5f1e6bbf" -> (known after apply)
~ init = false -> (known after apply)
~ ipc_mode = "private" -> (known after apply)
~ log_driver = "json-file" -> (known after apply)
- log_opts = {} -> null
- max_retry_count = 0 -> null
- memory = 0 -> null
- memory_swap = 0 -> null
name = "tutorial"
~ network_data = [
- {
- gateway = "172.17.0.1"
- global_ipv6_address = ""
- global_ipv6_prefix_length = 0
- ip_address = "172.17.0.2"
- ip_prefix_length = 16
- ipv6_gateway = ""
- mac_address = "02:42:ac:11:00:02"
- network_name = "bridge"
},
] -> (known after apply)
- network_mode = "default" -> null
- privileged = false -> null
- publish_all_ports = false -> null
~ runtime = "runc" -> (known after apply)
~ security_opts = [] -> (known after apply)
~ shm_size = 64 -> (known after apply)
~ stop_signal = "SIGQUIT" -> (known after apply)
~ stop_timeout = 0 -> (known after apply)
- storage_opts = {} -> null
- sysctls = {} -> null
- tmpfs = {} -> null
# (14 unchanged attributes hidden)

      ~ ports {
          ~ external = 8000 -> 8080 # forces replacement
            # (3 unchanged attributes hidden)
        }
    }

Plan: 1 to add, 0 to change, 1 to destroy.

Do you want to perform these actions?
Terraform will perform the actions described above.
Only 'yes' will be accepted to approve.

Enter a value: yes

docker_container.nginx: Destroying... [id=8162814cd1bcdaf7f9f995b2a655eb28a7c41c2fc81046ac863e4f6d5f1e6bbf]
docker_container.nginx: Destruction complete after 1s
docker_container.nginx: Creating...
docker_container.nginx: Creation complete after 1s [id=f67e0747bb827c2ba874393f1424e511bf8651814b7219a41c984b359eb33617]

Apply complete! Resources: 1 added, 0 changed, 1 destroyed.
```

### Output of `terraform output`

```markdown
container_id = "2c4bf14ee7712f879ebf6326a616dbac822d3b647e869be9d38f4017fb8bbbaf"
image_id = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666anginx:latest"
```

## Yandex Cloud

### Output of `terraform apply`

```markdown
Terraform used the selected providers to generate the following execution plan. Resource actions are indicated
with the following symbols:
+ create
Terraform will perform the following actions:
# yandex_compute_disk.boot-disk-1 will be created
+ resource "yandex_compute_disk" "boot-disk-1" {
    + block_size  = 4096
    + created_at  = (known after apply)
    + folder_id   = (known after apply)
    + id          = (known after apply)
    + image_id    = "fd8t8vqitgjou20saanq"
    + name        = "boot-disk-1"
    + product_ids = (known after apply)
    + size        = 20
    + status      = (known after apply)
    + type        = "network-hdd"
    + zone        = "ru-central1-a"
    }
# yandex_compute_instance.vm-1 will be created
+ resource "yandex_compute_instance" "vm-1" {
    + created_at                = (known after apply)
    + folder_id                 = (known after apply)
    + fqdn                      = (known after apply)
    + gpu_cluster_id            = (known after apply)
    + hostname                  = (known after apply)
    + id                        = (known after apply)
    + maintenance_grace_period  = (known after apply)
    + maintenance_policy        = (known after apply)
    + metadata                  = {
        + "ssh-keys" = <<-EOT
                ubuntu:ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIOa7qiTifRZeFREx3ukKUmI2kKK2BAMl3jRYbd+0STxn vladimir314v@gmail.com
            EOT
        }
    + name                      = "terraform1"
    + network_acceleration_type = "standard"
    + platform_id               = "standard-v1"
    + service_account_id        = (known after apply)
    + status                    = (known after apply)
    + zone                      = "ru-central1-a"
    + boot_disk {
        + auto_delete = true
        + device_name = (known after apply)
        + disk_id     = (known after apply)
        + mode        = (known after apply)
        }
    + network_interface {
        + index              = (known after apply)
        + ip_address         = (known after apply)
        + ipv4               = true
        + ipv6               = (known after apply)
        + ipv6_address       = (known after apply)
        + mac_address        = (known after apply)
        + nat                = true
        + nat_ip_address     = (known after apply)
        + nat_ip_version     = (known after apply)
        + security_group_ids = (known after apply)
        + subnet_id          = (known after apply)
        }
    + resources {
        + core_fraction = 100
        + cores         = 2
        + memory        = 2
        }
    }
# yandex_vpc_network.network-1 will be created
+ resource "yandex_vpc_network" "network-1" {
    + created_at                = (known after apply)
    + default_security_group_id = (known after apply)
    + folder_id                 = (known after apply)
    + id                        = (known after apply)
    + labels                    = (known after apply)
    + name                      = "network1"
    + subnet_ids                = (known after apply)
    }
# yandex_vpc_subnet.subnet-1 will be created
+ resource "yandex_vpc_subnet" "subnet-1" {
    + created_at     = (known after apply)
    + folder_id      = (known after apply)
    + id             = (known after apply)
    + labels         = (known after apply)
    + name           = "subnet1"
    + network_id     = (known after apply)
    + v4_cidr_blocks = [
        + "192.168.10.0/24",
        ]
    + v6_cidr_blocks = (known after apply)
    + zone           = "ru-central1-a"
    }
Plan: 4 to add, 0 to change, 0 to destroy.
Changes to Outputs:
+ external_ip_address_vm_1 = (known after apply)
+ internal_ip_address_vm_1 = (known after apply)
Do you want to perform these actions?
Terraform will perform the actions described above.
Only 'yes' will be accepted to approve.
Enter a value: yes
yandex_vpc_network.network-1: Creating...
yandex_compute_disk.boot-disk-1: Creating...
yandex_vpc_network.network-1: Creation complete after 2s [id=enpm579u5mn0fd3f7dmo]
yandex_vpc_subnet.subnet-1: Creating...
yandex_vpc_subnet.subnet-1: Creation complete after 0s [id=e9bqt7i476ec6btt1m4m]
yandex_compute_disk.boot-disk-1: Creation complete after 6s [id=fhmgcvu2ld689l09aimp]
yandex_compute_instance.vm-1: Creating...
yandex_compute_instance.vm-1: Still creating... [10s elapsed]
yandex_compute_instance.vm-1: Still creating... [20s elapsed]
yandex_compute_instance.vm-1: Still creating... [30s elapsed]
yandex_compute_instance.vm-1: Creation complete after 30s [id=fhmamghpkdpq8tp2s49d]
Apply complete! Resources: 4 added, 0 changed, 0 destroyed.
Outputs:
external_ip_address_vm_1 = "155.160.40.14"
internal_ip_address_vm_1 = "192.168.10.7"
```

### Output of `terraform state list`

```markdown
yandex_compute_disk.boot-disk-1
yandex_compute_instance.vm-1
yandex_vpc_network.network-1
yandex_vpc_subnet.subnet-1
```

### Output of `terraform state show yandex_compute_instance.vm-1`

```markdown
# yandex_compute_instance.vm-1:

resource "yandex_compute_instance" "vm-1" {
    created_at                = "2024-02-27T20:41:12Z"
    folder_id                 = "8045ffb6736203e80d50"
    fqdn                      = "db751b249c18ee60ca94.auto.internal"
    id                        = "db751b249c18ee60ca94"
    metadata                  = {
        "ssh-keys" = <<-EOT
            ubuntu:ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIOa7qiTifRZeFREx3ukKUmI2kKK2BAMl3jRYbd+0STxn vladimir314v@gmail.com
        EOT
    }
    name                      = "terraform1"
    network_acceleration_type = "standard"
    platform_id               = "standard-v1"
    status                    = "running"
    zone                      = "ru-central1-a"
    boot_disk {
        auto_delete = true
        device_name = "c7c7a0bc2578b05ef450"
        disk_id     = "c7c7a0bc2578b05ef450"
        mode        = "READ_WRITE"
        initialize_params {
            block_size = 4096
            image_id   = "fd8t8vqitgjou20saanq"
            name       = "boot-disk-1"
            size       = 20
            type       = "network-hdd"
        }
    }
    metadata_options {
        aws_v1_http_endpoint = 1
        aws_v1_http_token    = 2
        gce_http_endpoint    = 1
        gce_http_token       = 1
    }
    network_interface {
        index              = 0
        ip_address         = "192.168.10.7"
        ipv4               = true
        ipv6               = false
        mac_address        = "d0:0d:ab:42:39:a3"
        nat                = true
        nat_ip_address     = "155.160.40.14"
        nat_ip_version     = "IPV4"
        security_group_ids = []
        subnet_id          = "535a066de42d1ba555e4"
    }
    placement_policy {
        host_affinity_rules       = []
        placement_group_partition = 0
    }
    resources {
        core_fraction = 100
        cores         = 2
        gpus          = 0
        memory        = 2
    }
    scheduling_policy {
        preemptible = false
    }
}
```

### Output of `terraform output`

```markdown
external_ip_address_vm_1 = "155.160.40.14"
internal_ip_address_vm_1 = "192.168.10.7"
```

## Best Practises

1. Use Version Control: Store your Terraform configurations in a version control system like Git. This allows you to
   track changes, collaborate with others, and revert to previous states if needed.

2. Modularization: Organize your Terraform code into reusable modules. This promotes code reusability, reduces
   duplication, and simplifies maintenance.

3. Provider Versions: Specify provider versions in your Terraform configurations to ensure consistency and prevent
   breaking changes when providers are updated.

4. State Management: Use remote state storage for Terraform state files. This enables collaboration among team members
   and ensures state integrity.

5. Environment Separation: Maintain separate environments (e.g., dev, staging, prod) for your infrastructure. Use
   variables and conditional logic to manage environment-specific configurations.

6. Immutable Infrastructure: Embrace the concept of immutable infrastructure by recreating resources instead of
   modifying them in place. This promotes consistency, reproducibility, and reduces the risk of configuration drift.

7. Dependency Management: Declare dependencies explicitly in your Terraform configurations to ensure resources are
   created and destroyed in the correct order.

8. Variable Management: Use input variables to parameterize your Terraform configurations. This makes your code more
   flexible and reusable across different environments.

9. Sensitive Data Handling: Avoid hardcoding sensitive information like passwords and access keys directly in your
   Terraform code. Instead, use environment variables or a secret management solution.

10. Testing: Implement automated testing for your Terraform code using tools like Terratest or Kitchen-Terraform. This
    helps catch errors early and ensures the correctness of your infrastructure.

11. Documentation: Document your Terraform code, including descriptions of resources, variables, and modules. This makes
    it easier for others to understand and maintain the code.

12. Monitoring and Logging: Set up monitoring and logging for your Terraform deployments to track changes, detect
    issues, and troubleshoot problems effectively.