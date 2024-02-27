## Terraform

## Docker provider

### terraform state list

- `docker_container.nginx`
- `docker_image.nginx`

### terraform state show docker_container.nginx

```hcl
resource "docker_container" "nginx" {
  attach  = false
  command = [
    "nginx",
    "-g",
    "daemon off;",
  ]
  container_read_refresh_timeout_milliseconds = 15000
  cpu_shares                                  = 0
  entrypoint                                  = [
    "/docker-entrypoint.sh",
  ]
  env             = []
  hostname        = "adf93084c3af"
  id              = "adf93084c3afeee55fc418a290db6751358b083a2d6acf57efdba784ffcc1b6f"
  image           = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666a"
  init            = false
  ipc_mode        = "private"
  log_driver      = "json-file"
  logs            = false
  max_retry_count = 0
  memory          = 0
  memory_swap     = 0
  must_run        = true
  name            = "tutorial"
  network_data    = [
    {
      gateway                   = "172.17.0.1"
      global_ipv6_address       = ""
      global_ipv6_prefix_length = 0
      ip_address                = "172.17.0.2"
      ip_prefix_length          = 16
      ipv6_gateway              = ""
      mac_address               = "02:42:ac:11:00:02"
      network_name              = "bridge"
    },
  ]
  network_mode      = "default"
  privileged        = false
  publish_all_ports = false
  read_only         = false
  remove_volumes    = true
  restart           = "no"
  rm                = false
  runtime           = "runc"
  security_opts     = []
  shm_size          = 64
  start             = true
  stdin_open        = false
  stop_signal       = "SIGQUIT"
  stop_timeout      = 0
  tty               = false
  wait              = false
  wait_timeout      = 60

  ports {
    external = 8000
    internal = 80
    ip       = "0.0.0.0"
    protocol = "tcp"
  }
}
```

### terraform state show docker_container.nginx

```hcl
resource "docker_image" "nginx" {
  id           = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666anginx:latest"
  image_id     = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666a"
  keep_locally = false
  name         = "nginx:latest"
  repo_digest  = "nginx@sha256:c26ae7472d624ba1fafd296e73cecc4f93f853088e6a9c13c0d52f6ca5865107"
}
```

### after changing port number from 8000 to 8080, and running terraform apply:

```
docker_image.nginx: Refreshing state... [id=sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666anginx:latest]
docker_container.nginx: Refreshing state... [id=adf93084c3afeee55fc418a290db6751358b083a2d6acf57efdba784ffcc1b6f]
```

So, after changing terraform.tf file and running terraform apply, it destroyed old container and created the new one
with changes.

### Utilizing variables

to change name of the container, I created variables.tf file with the following content:

```
variable "container_name" {
  description = "Value of the name for the Docker container"
  type        = string
  default     = "ExampleNginxContainer"
}
```

then, in main.tf this line:

```hcl
name = "tutorial"
```

to

```hcl
name = var.container_name
```

then I run terraform apply -var "container_name=YetAnotherName". That's what i got:

```hcl
-/+ resource "docker_container" "nginx" {
+ bridge = (known after apply)
~ command                                     = [
- "nginx",
- "-g",
- "daemon off;",
] -> (known after apply)
+ container_logs = (known after apply)
- cpu_shares = 0 -> null
- dns = [] -> null
- dns_opts = [
] -> null
- dns_search = [] -> null
~ entrypoint                                  = [
- "/docker-entrypoint.sh",
] -> (known after apply)
~ env = [] -> (known after apply)
+ exit_code = (known after apply)
- group_add = [] -> null
~ hostname = "7b6742a2dbbc" -> (known after apply)
~ id = "7b6742a2dbbc49e1834a53099893348ad2e294caff7c8cc61dfffa288f5485d3" -> (known after apply)
~ init = false -> (known after apply)
~ ipc_mode = "private" -> (known after apply)
~ log_driver = "json-file" -> (known after apply)
- log_opts = {} -> null
- max_retry_count = 0 -> null
- memory = 0 -> null
- memory_swap = 0 -> null
~ name = "ExampleNginxContainer" -> "YetAnotherName" # forces replacement
~ network_data = [
- {
- gateway = "172.17.0.1"
- global_ipv6_address = ""
- global_ipv6_prefix_length = 0
- ip_address = "172.17.0.2"
- ip_prefix_length = 16
- ipv6_gateway = ""
- mac_address = "02:42:ac:11:00:02"
- network_name              = "bridge"
},
] -> (known after apply)
- network_mode = "default" -> null
- privileged = false -> null
- publish_all_ports = false -> null
~ runtime = "runc" -> (known after apply)
~ security_opts = [
] -> (known after apply)
~ shm_size = 64 -> (known after apply)
~ stop_signal = "SIGQUIT" -> (known after apply)
~ stop_timeout = 0 -> (known after apply)
- storage_opts = {} -> null
- sysctls = {} -> null
- tmpfs = {} -> null
# (14 unchanged attributes hidden)

# (1 unchanged block hidden)
}
```

As you can see, name changed to specified value, we can verify that container actually changed its name by running
`docker -ps`:

```
812a18558c2e   e4720093a3c1           "/docker-entrypoint.…"   About a minute ago   Up About a minute   0.0.0.0:8080->80/tcp                             YetAnotherName
```

### Outputs

to have outputs, I created `outputs.tf` with the following content:

```hcl
output "container_id" {
  description = "ID of the Docker container"
  value       = docker_container.nginx.id
}

output "image_id" {
  description = "ID of the Docker image"
  value       = docker_image.nginx.id
}
```

after applying new configuration, and running terraform output i got:

```
container_id = "36181fc3ba3fc169286f2dea3d38d4ac3974a7710996344937fc243f37752f0c"
image_id = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666anginx:latest"
```

## Yandex cloud provider

### `terraform state list`

- `yandex_compute_disk.boot-disk-1`
- `yandex_compute_disk.boot-disk-2`
- `yandex_compute_instance.vm-1`
- `yandex_compute_instance.vm-2`
- `yandex_vpc_network.network-1`
- `yandex_vpc_subnet.subnet-1`

### `terraform state show yandex_compute_disk.boot-disk-1`

```hcl
# yandex_compute_disk.boot-disk-1:
resource "yandex_compute_disk" "boot-disk-1" {
  block_size  = 4096
  created_at  = "2024-02-27T15:20:28Z"
  folder_id   = "b1gpm02sqk05p186sj6g"
  id          = "fhmi7f8kcn3u77tue3uf"
  image_id    = "fd8hnnsnfn3v88bk0k1o"
  name        = "boot-disk-1"
  product_ids = [
    "f2ej6hk1qmuqu40ku14r",
  ]
  size   = 20
  status = "ready"
  type   = "network-hdd"
  zone   = "ru-central1-a"

  disk_placement_policy {}
}
```

### `terraform state show yandex_compute_instance.vm-1`

```hcl
# yandex_compute_instance.vm-1:
resource "yandex_compute_instance" "vm-1" {
  created_at = "2024-02-27T15:20:38Z"
  folder_id  = "b1gpm02sqk05p186sj6g"
  fqdn       = "fhm5qu02evss3f0tr1si.auto.internal"
  id         = "fhm5qu02evss3f0tr1si"
  metadata   = {
    "user-data" = <<-EOT
            users:
              - name: djhovi
                groups: sudo
                shell: /bin/bash
                sudo: 'ALL=(ALL) NOPASSWD:ALL'
                ssh-authorized-keys:
                  - ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIP/CazbzhPKYe/63IuhdNPmB8s0z70dtf63WU44ucvbE
        EOT
  }
  name                      = "terraform1"
  network_acceleration_type = "standard"
  platform_id               = "standard-v1"
  status                    = "running"
  zone                      = "ru-central1-a"

  boot_disk {
    auto_delete = true
    device_name = "fhmi7f8kcn3u77tue3uf"
    disk_id     = "fhmi7f8kcn3u77tue3uf"
    mode        = "READ_WRITE"

    initialize_params {
      block_size = 4096
      image_id   = "fd8hnnsnfn3v88bk0k1o"
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
    ip_address         = "192.168.10.21"
    ipv4               = true
    ipv6               = false
    mac_address        = "d0:0d:5d:78:02:77"
    nat                = true
    nat_ip_address     = "158.160.121.240"
    nat_ip_version     = "IPV4"
    security_group_ids = []
    subnet_id          = "e9bruhioecg11jtsm403"
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

### `terraform state show yandex_vpc_network.network-1`

```hcl
# yandex_vpc_network.network-1:
resource "yandex_vpc_network" "network-1" {
  created_at                = "2024-02-27T15:13:38Z"
  default_security_group_id = "enprua4jubkdkrk0a215"
  folder_id                 = "b1gpm02sqk05p186sj6g"
  id                        = "enp0c9697bbds0ltg003"
  labels                    = {}
  name                      = "network1"
  subnet_ids                = [
    "e9bruhioecg11jtsm403",
  ]
}
```

### `terraform state show yandex_vpc_subnet.subnet-1`

```hcl
# yandex_vpc_subnet.subnet-1:
resource "yandex_vpc_subnet" "subnet-1" {
  created_at     = "2024-02-27T15:13:41Z"
  folder_id      = "b1gpm02sqk05p186sj6g"
  id             = "e9bruhioecg11jtsm403"
  labels         = {}
  name           = "subnet1"
  network_id     = "enp0c9697bbds0ltg003"
  v4_cidr_blocks = [
    "192.168.10.0/24",
  ]
  v6_cidr_blocks = []
  zone           = "ru-central1-a"
}
```

### Variables & changing

I used a variable to define preferred data center to use:

```
variable "zone" {
  description = "Value of the name for the data center"
  type        = string
  default     = "ru-central1-a"
}
```

after running `terraform apply --var "zone=ru-central1-b"` we can verify that zone has changed by checking state of some
resource, for example `terraform state show yandex_vpc_subnet.subnet-1`:

```
# yandex_compute_disk.boot-disk-1:
resource "yandex_compute_disk" "boot-disk-1" {
    block_size  = 4096
    created_at  = "2024-02-27T16:04:35Z"
    folder_id   = "b1gpm02sqk05p186sj6g"
    id          = "epdht9pbgdb2fgcptcjd"
    image_id    = "fd8hnnsnfn3v88bk0k1o"
    name        = "boot-disk-1"
    product_ids = [
        "f2ej6hk1qmuqu40ku14r",
    ]
    size        = 20
    status      = "ready"
    type        = "network-hdd"
    zone        = "ru-central1-b"**

    disk_placement_policy {}
}
```

as we can see, zone has changed

### Outputs

in my case, `terraform output` would print external and internal ips:

- `external_ip_address_vm_1 = "84.252.139.78"`
- `external_ip_address_vm_2 = "84.252.142.15"`
- `internal_ip_address_vm_1 = "192.168.10.16"`
- `internal_ip_address_vm_2 = "192.168.10.10"`

## Github provider

### Output

`terraform import "github_repository.repo" "gg"`

```
var.token
  Github oauth token

  Enter a value: 

github_repository.repo: Importing from ID "gg"...
github_repository.repo: Import prepared!
  Prepared github_repository for import
github_repository.repo: Refreshing state... [id=gg]

Import successful!

The resources that were imported are shown above. These resources are now in
your Terraform state and will henceforth be managed by Terraform.

```

`terraform apply`

```
var.token
  Github oauth token

  Enter a value: 

github_repository.repo: Refreshing state... [id=lab04_import]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # github_branch_default.master will be created
  + resource "github_branch_default" "master" {
      + branch     = "master"
      + etag       = (known after apply)
      + id         = (known after apply)
      + rename     = false
      + repository = "lab04_import"
    }

  # github_branch_protection.default will be created
  + resource "github_branch_protection" "default" {
      + allows_deletions                = false
      + allows_force_pushes             = false
      + enforce_admins                  = true
      + id                              = (known after apply)
      + lock_branch                     = false
      + pattern                         = "master"
      + repository_id                   = "lab04_import"
      + require_conversation_resolution = true
      + require_signed_commits          = false
      + required_linear_history         = false

      + required_pull_request_reviews {
          + require_last_push_approval      = false
          + required_approving_review_count = 1
        }
    }

Plan: 2 to add, 0 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

github_branch_default.master: Creating...
github_branch_default.master: Creation complete after 3s [id=lab04_import]
github_branch_protection.default: Creating...
github_branch_protection.default: Creation complete after 6s [id=BPR_kwDOFsnuSc4C0vCz]
```

### Best practices applied

- **Use Variables**: I utilized variables to parameterize my Terraform configurations. This made code more flexible
  and allowed easier configuration management across environments
- **Test Infrastructure**: I used `terraform fmt` for formatting, `terraform validate` for syntax validation
- **Security Considerations** Sensitve resources like access tokens were either stored as env variables or defined
  during execution