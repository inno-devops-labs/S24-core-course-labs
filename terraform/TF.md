## Docker

### Best Practices

#### Organizational Best Practices

- **Logical Segmentation of Resources:** The Terraform configuration is meticulously organized into separate files, such as `variables.tf` for variable declarations, `output.tf` for output values, among others. This structure facilitates ease of navigation and management of the infrastructure code.

- **Modularity and Reusability:** By decomposing the Terraform code into modular components, the configurations foster reusability and simplify the process of managing complex infrastructures. This modular approach aids in keeping the codebase clean and comprehensible.

#### Code Quality and Maintenance

- **Code Formatting and Validation:** The Terraform configurations have been refined using the `terraform fmt` command, which ensures that the code adheres to Terraform's formatting standards. Additionally, the `terraform validate` command has been employed to scrutinize the code for errors, further bolstering the code's quality and readability.

- **Version Pinning for Reliability:** To safeguard the infrastructure from potential disruptions caused by provider updates, version pinning is meticulously applied. By locking the versions of Terraform providers, we ensure a stable and predictable deployment environment.

#### Summary

These practices underscore a commitment to high-quality infrastructure as code. Through careful organization, modular design, strict code quality checks, and version control, the Terraform configurations are poised to support scalable, flexible, and reliable infrastructure deployments. By adhering to these principles, the codebase not only facilitates ease of use and maintenance but also ensures that the infrastructure remains robust against the evolving landscape of provider updates and enhancements.


### Commands Output

```console
$ terraform state list
docker_container.app
docker_image.app
```

```console
$ terraform state show docker_container.app
# docker_container.app:
resource "docker_container" "app" {
    attach                                      = false
    command                                     = []
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    entrypoint                                  = [
        "python",
        "app.py",
    ]
    env                                         = []
    hostname                                    = "476df821c902"
    id                                          = "476df821c902003b67fb47876217ccc8b148d5a11c8008883df38a694a1180df"
    image                                       = "sha256:a9eee15f45da3b91fe22a0fc15b35db6134a4bb5dbbfc08b71e4c94c3a36981c"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "moscowtime-web-app"
    network_data                                = [
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
    network_mode                                = "default"
    privileged                                  = false
    publish_all_ports                           = false
    read_only                                   = false
    remove_volumes                              = true
    restart                                     = "no"
    rm                                          = false
    runtime                                     = "runc"
    security_opts                               = []
    shm_size                                    = 64
    start                                       = true
    stdin_open                                  = false
    stop_timeout                                = 0
    tty                                         = false
    user                                        = "appuser"
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/app"

    ports {
        external = 8000
        internal = 8080
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
```

```console
$ terraform state show docker_image.app
# docker_image.app:
resource "docker_image" "app" {
    id           = "sha256:a9eee15f45da3b91fe22a0fc15b35db6134a4bb5dbbfc08b71e4c94c3a36981cnabuki/moscowtime-web:latest"
    image_id     = "sha256:a9eee15f45da3b91fe22a0fc15b35db6134a4bb5dbbfc08b71e4c94c3a36981c"
    keep_locally = false
    name         = "nabuki/moscowtime-web:latest"
    repo_digest  = "nabuki/moscowtime-web@sha256:b6cf9958dab002926aae0b956ff2f6a4c23a73ba47dbe79fdf6eb29be3d145f3"
}
```

```console
$ terraform output
container_id = "476df821c902003b67fb47876217ccc8b148d5a11c8008883df38a694a1180df"
image_id = "sha256:a9eee15f45da3b91fe22a0fc15b35db6134a4bb5dbbfc08b71e4c94c3a36981cnabuki/moscowtime-web:latest"
```

## Yandex Cloud

### Best Practices

#### `main.tf` Best Practices

- **Provider Configuration with Variables:**

    ```hcl
    provider "yandex" {
      zone      = var.zone
      token     = var.token
      cloud_id  = var.cloud_id
      folder_id = var.folder_id
    }
    ```
    Utilizing variables for provider configuration enhances flexibility and reusability across different environments or projects.

- **Resource Declaration:**

    Resources such as `yandex_compute_disk`, `yandex_compute_instance`, `yandex_vpc_network`, and `yandex_vpc_subnet` are defined with clear naming conventions and properties, illustrating a structured approach to resource management.

- **Use of Metadata for SSH Keys:**

    ```hcl
    metadata = {
      ssh-keys = "ubuntu:${file("~/.ssh/id_ed25519.pub")}"
    }
    ```
    Embedding SSH keys through metadata for compute instances enhances security and access control.

#### `output.tf` Best Practices

- **Output Values for Resource Attributes:**

    ```hcl
    output "internal_ip_address_vm_1" {
      value = yandex_compute_instance.vm-1.network_interface.0.ip_address
    }

    output "external_ip_address_vm_1" {
      value = yandex_compute_instance.vm-1.network_interface.0.nat_ip_address
    }
    ```
    Specifying outputs for both internal and external IP addresses of a compute instance provides essential information for subsequent operations or dependencies.

#### `variables.tf` Best Practices

- **Variable Definitions with Descriptions and Defaults:**

    Each variable is accompanied by a description, and where applicable, a default value. This practice not only enhances the readability of the code but also provides context and defaults for essential configurations.

    ```hcl
    variable "zone" {
      description = "Zone"
      type        = string
      default     = "ru-central1-a"
    }
    ```

    Including descriptions and default values (where suitable) makes the configuration more user-friendly and self-documenting.

#### Summary

The Terraform configurations for Yandex Cloud infrastructure deployment demonstrate adherence to several best practices, including modularization, use of variables for flexible configurations, descriptive naming of resources, security practices through metadata, and clear output definitions. These practices ensure the code is maintainable, scalable, and adaptable to various deployment scenarios, thereby facilitating efficient infrastructure management.

### Commands Output

```console
$ terraform state list
yandex_compute_disk.boot-disk-1
yandex_compute_instance.vm-1
yandex_vpc_network.network-1
yandex_vpc_subnet.subnet-1
```

```console
$ terraform state show yandex_compute_disk.boot-disk-1
# yandex_compute_disk.boot-disk-1:
resource "yandex_compute_disk" "boot-disk-1" {
    block_size  = 4096
    created_at  = "2024-02-26T22:41:47Z"
    folder_id   = "b1go42d8nahe3jt1ksa7"
    id          = "fhmucnpgo6ploakfu5u4"
    image_id    = "fd8hnnsnfn3v88bk0k1o"
    name        = "boot-disk-1"
    product_ids = [
        "f2ej6hk1qmuqu40ku14r",
    ]
    size        = 20
    status      = "ready"
    type        = "network-hdd"
    zone        = "ru-central1-a"

    disk_placement_policy {}
}
```

```console
$ terraform state show yandex_compute_instance.vm-1
# yandex_compute_instance.vm-1:
resource "yandex_compute_instance" "vm-1" {
    created_at                = "2024-02-26T22:41:57Z"
    folder_id                 = "b1go42d8nahe3jt1ksa7"
    fqdn                      = "fhm3ic1qks8ibepbjjg4.auto.internal"
    id                        = "fhm3ic1qks8ibepbjjg4"
    metadata                  = {
        "ssh-keys" = <<-EOT
            ubuntu:ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIGIQcNLErVe6Au22kY/YIRAtKnpOqS0lgbxEOQGlVaqB nabuki@LAPTOP-6UP0H37T
        EOT
    }
    name                      = "terraform1"
    network_acceleration_type = "standard"
    platform_id               = "standard-v1"
    status                    = "running"
    zone                      = "ru-central1-a"

    boot_disk {
        auto_delete = true
        device_name = "fhmucnpgo6ploakfu5u4"
        disk_id     = "fhmucnpgo6ploakfu5u4"
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
        ip_address         = "192.168.10.10"
        ipv4               = true
        ipv6               = false
        mac_address        = "d0:0d:39:30:3a:a7"
        nat                = true
        nat_ip_address     = "51.250.78.242"
        nat_ip_version     = "IPV4"
        security_group_ids = []
        subnet_id          = "e9br45ol393470oqud3m"
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

```console
$ terraform state show yandex_vpc_network.network-1
# yandex_vpc_network.network-1:
resource "yandex_vpc_network" "network-1" {
    created_at                = "2024-02-26T22:37:50Z"
    default_security_group_id = "enpvur6835nb7ph5g333"
    folder_id                 = "b1go42d8nahe3jt1ksa7"
    id                        = "enp9a5sk2a2b3avrngkg"
    labels                    = {}
    name                      = "network1"
    subnet_ids                = [
        "e9br45ol393470oqud3m",
    ]
}
```

```console
$ terraform state show yandex_vpc_subnet.subnet-1
# yandex_vpc_subnet.subnet-1:
resource "yandex_vpc_subnet" "subnet-1" {
    created_at     = "2024-02-26T22:37:52Z"
    folder_id      = "b1go42d8nahe3jt1ksa7"
    id             = "e9br45ol393470oqud3m"
    labels         = {}
    name           = "subnet1"
    network_id     = "enp9a5sk2a2b3avrngkg"
    v4_cidr_blocks = [
        "192.168.10.0/24",
    ]
    v6_cidr_blocks = []
    zone           = "ru-central1-a"
}
```

```console
$ terraform output
external_ip_address_vm_1 = "51.250.78.242"
internal_ip_address_vm_1 = "192.168.10.10"
```

## Github

### Best Practices

#### `main.tf` Best Practices

- **Provider Configuration with Required Version:**

    ```hcl
    terraform {
      required_providers {
        github = {
          source  = "integrations/github"
          version = "~> 6.0"
        }
      }
    }
    ```
    This block ensures that the GitHub provider is used with a specific version, promoting consistency and reliability in Terraform operations.

- **Resource Management for GitHub:**

    The configuration manages GitHub resources such as repositories, branch defaults, and branch protection settings. Each resource is declared with comprehensive settings, reflecting a detailed and thoughtful approach to resource configuration.

    ```hcl
    resource "github_repository" "repo" {
      name        = "terraform_test"
      description = "Testing terraform github"
      visibility  = "public"
      ...
    }
    ```

    This demonstrates a careful consideration of repository features and settings, ensuring that the GitHub repository is configured with desired properties like visibility, issue tracking, and initialization state.

- **Security and Workflow Enhancements:**

    The configuration enforces best practices such as branch protection to secure the repository's main branch, requiring pull request reviews and conversation resolutions, which are critical for maintaining a high standard of code quality and collaboration.

    ```hcl
    resource "github_branch_protection" "default" {
      ...
      require_conversation_resolution = true
      enforce_admins                  = true
      ...
    }
    ```

#### `variables.tf` Best Practices

- **Sensitive Variable Handling:**

    ```hcl
    variable "token" {
      type        = string
      description = "Specifies the GitHub PAT token or `GITHUB_TOKEN`"
      sensitive   = true
    }
    ```
    The token variable is marked as sensitive, ensuring that its value is treated with an appropriate level of security, avoiding accidental exposure in logs or outputs.

#### Summary

These Terraform configurations showcase a well-organized and secure approach to managing GitHub resources. By utilizing best practices such as provider version pinning, comprehensive resource configuration, and sensitive variable handling, the configurations ensure that GitHub repositories and their associated settings are managed in a secure, efficient, and reliable manner. This approach not only enhances the code's maintainability but also aligns with best practices for security and collaboration within GitHub projects.

### Commands Output

```console
$ terraform import "github_repository.repo" "terraform_test"
var.token
  Specifies the GitHub PAT token or `GITHUB_TOKEN`

  Enter a value: 

github_repository.repo: Importing from ID "terraform_test"...
github_repository.repo: Import prepared!
  Prepared github_repository for import
```

```console
$ terraform apply
var.token
  Specifies the GitHub PAT token or `GITHUB_TOKEN`

  Enter a value: 

github_repository.repo: Refreshing state... [id=terraform_test]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the
following symbols:
  + create
  ~ update in-place

Terraform will perform the following actions:

  # github_branch_default.main will be created
  + resource "github_branch_default" "main" {
      + branch     = "main"
      + etag       = (known after apply)
      + id         = (known after apply)
      + rename     = false
      + repository = "terraform_test"
    }

  # github_branch_protection.default will be created
  + resource "github_branch_protection" "default" {
      + allows_deletions                = false
      + allows_force_pushes             = false
      + enforce_admins                  = true
      + id                              = (known after apply)
      + lock_branch                     = false
      + pattern                         = "main"
      + repository_id                   = "terraform_test"
      + require_conversation_resolution = true
      + require_signed_commits          = false
      + required_linear_history         = false

      + required_pull_request_reviews {
          + require_last_push_approval      = false
          + required_approving_review_count = 1
        }
    }

  # github_repository.repo will be updated in-place
  ~ resource "github_repository" "repo" {
      ~ auto_init                   = false -> true
      + description                 = "Testing terraform github"
        id                          = "terraform_test"
        name                        = "terraform_test"
        # (32 unchanged attributes hidden)

        # (1 unchanged block hidden)
    }

Plan: 2 to add, 1 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

github_repository.repo: Modifying... [id=terraform_test]
github_repository.repo: Modifications complete after 2s [id=terraform_test]
github_branch_default.main: Creating...
github_branch_default.main: Creation complete after 1s [id=terraform_test]
github_branch_protection.default: Creating...
github_branch_protection.default: Creation complete after 4s [id=BPR_kwDOLYmp8s4C0rZM]

Apply complete! Resources: 2 added, 1 changed, 0 destroyed.
```