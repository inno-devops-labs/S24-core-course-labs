# Docker example local setup part

## `terraform apply` output

```
Terraform used the selected providers to generate the following execution plan.
Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # docker_container.nginx will be created
  + resource "docker_container" "nginx" {
      + attach                                      = false
      + bridge                                      = (known after apply)
      + command                                     = (known after apply)
      + container_logs                              = (known after apply)
      + container_read_refresh_timeout_milliseconds = 15000
      + entrypoint                                  = (known after apply)
      + env                                         = (known after apply)
      + exit_code                                   = (known after apply)
      + hostname                                    = (known after apply)
      + id                                          = (known after apply)
      + image                                       = (known after apply)
      + init                                        = (known after apply)
      + ipc_mode                                    = (known after apply)
      + log_driver                                  = (known after apply)
      + logs                                        = false
      + must_run                                    = true
      + name                                        = "ExampleNginxContainer"
      + network_data                                = (known after apply)
      + read_only                                   = false
      + remove_volumes                              = true
      + restart                                     = "no"
      + rm                                          = false
      + runtime                                     = (known after apply)
      + security_opts                               = (known after apply)
      + shm_size                                    = (known after apply)
      + start                                       = true
      + stdin_open                                  = false
      + stop_signal                                 = (known after apply)
      + stop_timeout                                = (known after apply)
      + tty                                         = false
      + wait                                        = false
      + wait_timeout                                = 60

      + ports {
          + external = 8000
          + internal = 80
          + ip       = "0.0.0.0"
          + protocol = "tcp"
        }
    }

  # docker_image.nginx will be created
  + resource "docker_image" "nginx" {
      + id           = (known after apply)
      + image_id     = (known after apply)
      + keep_locally = false
      + name         = "nginx"
      + repo_digest  = (known after apply)
    }

Plan: 2 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + container_id = (known after apply)
  + image_id     = (known after apply)

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes 

docker_image.nginx: Creating...
docker_image.nginx: Creation complete after 7s [id=sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666anginx]
docker_container.nginx: Creating...
docker_container.nginx: Creation complete after 1s [id=2f59f2bdf3be7e76463727be0665758a02bb71b0f9c963c99470e518cc8eb74c]

Apply complete! Resources: 2 added, 0 changed, 0 destroyed.

Outputs:

container_id = "2f59f2bdf3be7e76463727be0665758a02bb71b0f9c963c99470e518cc8eb74c"
image_id = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666anginx"

```

## `terraform state list` output

```
docker_container.nginx
docker_image.nginx
```

## `terraform state show docker_container.nginx` output

```
# docker_container.nginx:
resource "docker_container" "nginx" {
    attach                                      = false
    command                                     = [
        "nginx",
        "-g",
        "daemon off;",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    entrypoint                                  = [
        "/docker-entrypoint.sh",
    ]
    env                                         = []
    hostname                                    = "2f59f2bdf3be"
    id                                          = "2f59f2bdf3be7e76463727be0665758a02bb71b0f9c963c99470e518cc8eb74c"
    image                                       = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666a"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "ExampleNginxContainer"
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
    stop_signal                                 = "SIGQUIT"
    stop_timeout                                = 0
    tty                                         = false
    wait                                        = false
    wait_timeout                                = 60

    ports {
        external = 8000
        internal = 80
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}

```

## `terraform state show docker_image.nginx` output

```
# docker_image.nginx:
resource "docker_image" "nginx" {
    id           = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666anginx"
    image_id     = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666a"
    keep_locally = false
    name         = "nginx"
    repo_digest  = "nginx@sha256:c26ae7472d624ba1fafd296e73cecc4f93f853088e6a9c13c0d52f6ca5865107"
}

```

## `terraform output` output

```
container_id = "2f59f2bdf3be7e76463727be0665758a02bb71b0f9c963c99470e518cc8eb74c"
image_id = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666anginx"
```

# Virtualbox setup

## `terraform apply` output

```

Terraform used the selected providers to generate the following execution plan.
Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # virtualbox_vm.vm1 will be created
  + resource "virtualbox_vm" "vm1" {
      + cpus      = 1
      + id        = (known after apply)
      + image     = "https://app.vagrantup.com/shekeriev/boxes/ubuntu-20-04-server/versions/0.2/providers/virtualbox/unknown/vagrant.box"
      + memory    = "512 mib"
      + name      = "ExampleAppServerInstance"
      + status    = "running"
      + user_data = "test"

      + network_adapter {
          + device                 = "IntelPro1000MTDesktop"
          + host_interface         = "vboxnet1"
          + ipv4_address           = (known after apply)
          + ipv4_address_available = (known after apply)
          + mac_address            = (known after apply)
          + status                 = (known after apply)
          + type                   = "hostonly"
        }
    }

Plan: 1 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + IPAddress = (known after apply)

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

virtualbox_vm.vm1: Creating...
virtualbox_vm.vm1: Still creating... [10s elapsed]
virtualbox_vm.vm1: Still creating... [20s elapsed]
virtualbox_vm.vm1: Still creating... [30s elapsed]
virtualbox_vm.vm1: Still creating... [40s elapsed]
virtualbox_vm.vm1: Still creating... [50s elapsed]
virtualbox_vm.vm1: Still creating... [1m0s elapsed]
virtualbox_vm.vm1: Still creating... [1m10s elapsed]
virtualbox_vm.vm1: Still creating... [1m20s elapsed]
virtualbox_vm.vm1: Still creating... [1m30s elapsed]
virtualbox_vm.vm1: Still creating... [1m40s elapsed]
virtualbox_vm.vm1: Still creating... [1m50s elapsed]
virtualbox_vm.vm1: Still creating... [2m0s elapsed]
virtualbox_vm.vm1: Still creating... [2m10s elapsed]
virtualbox_vm.vm1: Still creating... [2m20s elapsed]
virtualbox_vm.vm1: Creation complete after 2m22s [id=f9eea154-9b99-4858-be82-093432bbeb2f]

Apply complete! Resources: 1 added, 0 changed, 0 destroyed.

Outputs:

IPAddress = "192.168.57.3"
```

## `terraform state list` output

```
virtualbox_vm.vm1
```

## `terraform state show virtualbox_vm.vm1` output

```
# virtualbox_vm.vm1:
resource "virtualbox_vm" "vm1" {
    cpus      = 1
    id        = "f9eea154-9b99-4858-be82-093432bbeb2f"
    image     = "https://app.vagrantup.com/shekeriev/boxes/ubuntu-20-04-server/versions/0.2/providers/virtualbox/unknown/vagrant.box"
    memory    = "512 mib"
    name      = "ExampleAppServerInstance"
    status    = "running"
    user_data = "test"

    network_adapter {
        device                 = "IntelPro1000MTDesktop"
        host_interface         = "vboxnet1"
        ipv4_address           = "192.168.57.3"
        ipv4_address_available = "yes"
        mac_address            = "0800276AA97C"
        status                 = "up"
        type                   = "hostonly"
    }
}
```

## `virtualbox output` output

```
IPAddress = "192.168.57.3"
```

# Best practices

+ Separate terraform files to keep clear logical structure
+ Use environment variables to pass sensitive data
+ Use outputs for vital runtime info
+ Format tf files using `terraform fmt`
