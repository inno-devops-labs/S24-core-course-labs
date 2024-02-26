## Docker Infrastructure Using Terraform

The output of the `terraform show` command:

```shell
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
    hostname                                    = "3ec1370483b3"
    id                                          = "3ec1370483b322ae6b433adead58bf7610583b85807059a30cab13b6049d0ab4"
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
        external = 8080
        internal = 80
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}

# docker_image.nginx:
resource "docker_image" "nginx" {
    id           = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666anginx:latest"
    image_id     = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666a"
    keep_locally = false
    name         = "nginx:latest"
    repo_digest  = "nginx@sha256:c26ae7472d624ba1fafd296e73cecc4f93f853088e6a9c13c0d52f6ca5865107"
}


Outputs:

container_id = "3ec1370483b322ae6b433adead58bf7610583b85807059a30cab13b6049d0ab4"
image_id = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666anginx:latest"

```

The output of the `terraform state list` command:
```shell
docker_container.nginx
docker_image.nginx
```


A part of the log with the applied changes:
```shell
docker_image.nginx: Refreshing state... [id=sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666anginx:latest]
docker_container.nginx: Refreshing state... [id=445f983f4aae884e41fe97f6ae0e6e88a035baabb3d24f747311f62615e6b7be]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
-/+ destroy and then create replacement

Terraform will perform the following actions:

  # docker_container.nginx must be replaced
-/+ resource "docker_container" "nginx" {
      + bridge                                      = (known after apply)
      ~ command                                     = [
          - "nginx",
          - "-g",
          - "daemon off;",
        ] -> (known after apply)
      + container_logs                              = (known after apply)
      - cpu_shares                                  = 0 -> null
      - dns                                         = [] -> null
      - dns_opts                                    = [] -> null
      - dns_search                                  = [] -> null
      ~ entrypoint                                  = [
          - "/docker-entrypoint.sh",
        ] -> (known after apply)
      ~ env                                         = [] -> (known after apply)
      + exit_code                                   = (known after apply)
      - group_add                                   = [] -> null
      ~ hostname                                    = "445f983f4aae" -> (known after apply)
      ~ id                                          = "445f983f4aae884e41fe97f6ae0e6e88a035baabb3d24f747311f62615e6b7be" -> (known after apply)
      ~ init                                        = false -> (known after apply)
      ~ ipc_mode                                    = "private" -> (known after apply)
      ~ log_driver                                  = "json-file" -> (known after apply)
      - log_opts                                    = {} -> null
      - max_retry_count                             = 0 -> null
      - memory                                      = 0 -> null
      - memory_swap                                 = 0 -> null
      ~ name                                        = "YetAnotherName" -> "ExampleNginxContainer" # forces replacement
      ~ network_data                                = [
          - {
              - gateway                   = "172.17.0.1"
              - global_ipv6_address       = ""
              - global_ipv6_prefix_length = 0
              - ip_address                = "172.17.0.2"
              - ip_prefix_length          = 16
              - ipv6_gateway              = ""
              - mac_address               = "02:42:ac:11:00:02"
              - network_name              = "bridge"
            },
        ] -> (known after apply)
      - network_mode                                = "default" -> null
      - privileged                                  = false -> null
      - publish_all_ports                           = false -> null
      ~ runtime                                     = "runc" -> (known after apply)
      ~ security_opts                               = [] -> (known after apply)
      ~ shm_size                                    = 64 -> (known after apply)
      ~ stop_signal                                 = "SIGQUIT" -> (known after apply)
      ~ stop_timeout                                = 0 -> (known after apply)
      - storage_opts                                = {} -> null
      - sysctls                                     = {} -> null
      - tmpfs                                       = {} -> null
        # (14 unchanged attributes hidden)

        # (1 unchanged block hidden)
    }

Plan: 1 to add, 0 to change, 1 to destroy.

Changes to Outputs:
  + container_id = (known after apply)
  + image_id     = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666anginx:latest"

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

docker_container.nginx: Destroying... [id=445f983f4aae884e41fe97f6ae0e6e88a035baabb3d24f747311f62615e6b7be]
docker_container.nginx: Destruction complete after 1s
docker_container.nginx: Creating...
docker_container.nginx: Creation complete after 2s [id=3ec1370483b322ae6b433adead58bf7610583b85807059a30cab13b6049d0ab4]

Apply complete! Resources: 1 added, 0 changed, 1 destroyed.

Outputs:

container_id = "3ec1370483b322ae6b433adead58bf7610583b85807059a30cab13b6049d0ab4"
image_id = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666anginx:latest"
```

Utilize input variables to rename your Docker container:
```shell
terraform apply -var "container_name=YetAnotherName"
```

```shell
docker_image.nginx: Refreshing state... [id=sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666anginx:latest]
docker_container.nginx: Refreshing state... [id=3ec1370483b322ae6b433adead58bf7610583b85807059a30cab13b6049d0ab4]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
-/+ destroy and then create replacement

Terraform will perform the following actions:

  # docker_container.nginx must be replaced
-/+ resource "docker_container" "nginx" {
      + bridge                                      = (known after apply)
      ~ command                                     = [
          - "nginx",
          - "-g",
          - "daemon off;",
        ] -> (known after apply)
      + container_logs                              = (known after apply)
      - cpu_shares                                  = 0 -> null
      - dns                                         = [] -> null
      - dns_opts                                    = [] -> null
      - dns_search                                  = [] -> null
      ~ entrypoint                                  = [
          - "/docker-entrypoint.sh",
        ] -> (known after apply)
      ~ env                                         = [] -> (known after apply)
      + exit_code                                   = (known after apply)
      - group_add                                   = [] -> null
      ~ hostname                                    = "3ec1370483b3" -> (known after apply)
      ~ id                                          = "3ec1370483b322ae6b433adead58bf7610583b85807059a30cab13b6049d0ab4" -> (known after apply)
      ~ init                                        = false -> (known after apply)
      ~ ipc_mode                                    = "private" -> (known after apply)
      ~ log_driver                                  = "json-file" -> (known after apply)
      - log_opts                                    = {} -> null
      - max_retry_count                             = 0 -> null
      - memory                                      = 0 -> null
      - memory_swap                                 = 0 -> null
      ~ name                                        = "ExampleNginxContainer" -> "YetAnotherName" # forces replacement
      ~ network_data                                = [
          - {
              - gateway                   = "172.17.0.1"
              - global_ipv6_address       = ""
              - global_ipv6_prefix_length = 0
              - ip_address                = "172.17.0.2"
              - ip_prefix_length          = 16
              - ipv6_gateway              = ""
              - mac_address               = "02:42:ac:11:00:02"
              - network_name              = "bridge"
            },
        ] -> (known after apply)
      - network_mode                                = "default" -> null
      - privileged                                  = false -> null
      - publish_all_ports                           = false -> null
      ~ runtime                                     = "runc" -> (known after apply)
      ~ security_opts                               = [] -> (known after apply)
      ~ shm_size                                    = 64 -> (known after apply)
      ~ stop_signal                                 = "SIGQUIT" -> (known after apply)
      ~ stop_timeout                                = 0 -> (known after apply)
      - storage_opts                                = {} -> null
      - sysctls                                     = {} -> null
      - tmpfs                                       = {} -> null
        # (14 unchanged attributes hidden)

        # (1 unchanged block hidden)
    }

Plan: 1 to add, 0 to change, 1 to destroy.

Changes to Outputs:
  ~ container_id = "3ec1370483b322ae6b433adead58bf7610583b85807059a30cab13b6049d0ab4" -> (known after apply)

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

docker_container.nginx: Destroying... [id=3ec1370483b322ae6b433adead58bf7610583b85807059a30cab13b6049d0ab4]
docker_container.nginx: Destruction complete after 1s
docker_container.nginx: Creating...
docker_container.nginx: Creation complete after 2s [id=107c6c7646ae1cfda2665c1f84ea18b198526c5455d9c23600113c3bb91819b5]

Apply complete! Resources: 1 added, 0 changed, 1 destroyed.

Outputs:

container_id = "107c6c7646ae1cfda2665c1f84ea18b198526c5455d9c23600113c3bb91819b5"
image_id = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666anginx:latest"
```

The output of the `terraform output` command:

```shell
container_id = "107c6c7646ae1cfda2665c1f84ea18b198526c5455d9c23600113c3bb91819b5"
image_id = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666anginx:latest"
```

## VK Cloud

The output of the `terraform show` command:

```shell
# data.vkcs_compute_flavor.compute:
data "vkcs_compute_flavor" "compute" {
    disk         = 10
    extra_specs  = {
        "agg_common"     = "true"
        "hw:cpu_sockets" = "1"
        "mcs:cpu_type"   = "standard"
    }
    flavor_id    = "df3c499a-044f-41d2-8612-d303adc613cc"
    id           = "df3c499a-044f-41d2-8612-d303adc613cc"
    is_public    = true
    name         = "Basic-1-1-10"
    ram          = 1024
    rx_tx_factor = 1
    swap         = 0
    vcpus        = 1
}

# data.vkcs_images_image.compute:
data "vkcs_images_image" "compute" {
    checksum         = "6d4ade04c95ed136e8c0f2832ee31cd2"
    container_format = "bare"
    created_at       = "2022-08-15T14:12:15Z"
    disk_format      = "raw"
    file             = "/v2/images/b75595ca-4e1d-47e0-8e95-7a02edc0e242/file"
    id               = "b75595ca-4e1d-47e0-8e95-7a02edc0e242"
    metadata         = {}
    min_disk_gb      = 0
    min_ram_mb       = 0
    most_recent      = false
    name             = "Ubuntu-22.04-202208"
    owner            = "9d013ed7c41e4bf38dd91f899e40185a"
    protected        = false
    region           = "RegionOne"
    schema           = "/v2/schemas/image"
    size_bytes       = 3758096384
    tags             = []
    updated_at       = "2022-08-16T06:01:24Z"
    visibility       = "public"
}

# data.vkcs_networking_network.extnet:
data "vkcs_networking_network" "extnet" {
    admin_state_up       = "true"
    all_tags             = [
        "dm.semenov",
        "rivalsec123qwerty",
    ]
    external             = true
    id                   = "298117ae-3fa4-4109-9e08-8be5602be5a2"
    name                 = "ext-net"
    private_dns_domain   = "openstacklocal."
    region               = "RegionOne"
    sdn                  = "neutron"
    shared               = "true"
    subnets              = [
        "01009166-1de2-413d-995c-8c2272f1bc19",
        "0dbaf324-1c17-4c51-ab6f-817a2223a097",
        "13b6afaa-a0da-4ffb-8061-f7b28d318fdf",
        "191efdda-cd5a-4327-987d-1eb1b5b32b4d",
        "1e68063b-96e0-45bc-b010-579e9aabb485",
        "1ea7f321-4ed0-4ae7-a136-a0226b9c5969",
        "2267f99b-83a5-49b6-ba19-e0cbac642583",
        "389a5241-76e3-48b9-89f5-5b0a938cf8b3",
        "41d17c6b-d2cf-4bd2-8784-f8a846656c3b",
        "489f81ad-2a0c-449d-8aed-1876ddbd7840",
        "5a66e4b1-1676-444e-94cf-eb37ac80d464",
        "62a77e13-ccc0-44b7-8cac-0567163a8a3b",
        "7f876978-01fe-43ab-8c77-7e6e32cd28c4",
        "888682e5-abdd-4274-853f-b091115cce84",
        "94640c6b-6298-40d0-8c71-6aab8716d48f",
        "aa2689f9-a208-4bf2-bed0-c20dab001467",
        "b1911f6b-9185-45fd-a0c2-424b0c9155ce",
        "b2298251-6be3-444b-b213-59c66e25346b",
        "b5502dbd-18c7-4f44-857a-5819265bbbdc",
        "be8539d5-eeff-4eaa-8048-9f7c3dbc8804",
        "be9cabcf-c5f8-4e88-9e27-c5ba80f4a638",
        "c4f89da6-529f-4a08-9df1-6b95842a07b9",
        "c6fafdba-deb7-4ad0-83fd-ec893dedfb69",
        "cbd9c937-5339-42df-b0a7-edfb2ccfee59",
        "d10ef821-cba1-476c-bcfd-582632939e80",
        "d5f70b09-6d49-445b-99f1-184d366decf6",
        "ec5d4a62-5039-460c-833f-7084a19794d2",
    ]
    tenant_id            = "c9fe9505fdde4de680679748c7cfee7e"
    vkcs_services_access = false
}

# vkcs_compute_floatingip_associate.fip:
resource "vkcs_compute_floatingip_associate" "fip" {
    floating_ip = "212.233.95.12"
    id          = "212.233.95.12/d3009ee1-a0ee-405b-af04-48d2700f195a/"
    instance_id = "d3009ee1-a0ee-405b-af04-48d2700f195a"
    region      = "RegionOne"
}

# vkcs_compute_instance.compute:
resource "vkcs_compute_instance" "compute" {
    access_ip_v4        = "192.168.199.17"
    all_metadata        = {}
    all_tags            = []
    availability_zone   = "MS1"
    flavor_id           = "df3c499a-044f-41d2-8612-d303adc613cc"
    flavor_name         = "Basic-1-1-10"
    force_delete        = false
    id                  = "d3009ee1-a0ee-405b-af04-48d2700f195a"
    image_id            = "Attempt to boot from volume - no image supplied"
    key_pair            = "Ubuntu-Basic-1-2-20GB-oUTkU7oa"
    name                = "compute-instance"
    power_state         = "active"
    region              = "RegionOne"
    security_groups     = [
        "default",
        "ssh",
    ]
    stop_before_destroy = false

    block_device {
        boot_index            = 0
        delete_on_termination = true
        destination_type      = "volume"
        source_type           = "image"
        uuid                  = "b75595ca-4e1d-47e0-8e95-7a02edc0e242"
        volume_size           = 8
        volume_type           = "ceph-ssd"
    }

    network {
        access_network = false
        fixed_ip_v4    = "192.168.199.17"
        mac            = "fa:16:3e:38:f5:85"
        name           = "net"
        uuid           = "b4e306f8-3c2b-4489-87b0-1b438ff18977"
    }
}

# vkcs_networking_floatingip.fip:
resource "vkcs_networking_floatingip" "fip" {
    address = "212.233.95.12"
    id      = "ee19f1d4-5b98-4545-b752-8baab563464a"
    pool    = "ext-net"
    region  = "RegionOne"
    sdn     = "neutron"
}

# vkcs_networking_network.network:
resource "vkcs_networking_network" "network" {
    admin_state_up        = true
    all_tags              = []
    id                    = "b4e306f8-3c2b-4489-87b0-1b438ff18977"
    name                  = "net"
    port_security_enabled = true
    private_dns_domain    = "mcs.local."
    region                = "RegionOne"
    sdn                   = "neutron"
    tags                  = []
    vkcs_services_access  = false
}

# vkcs_networking_port.port:
resource "vkcs_networking_port" "port" {
    admin_state_up         = true
    all_fixed_ips          = [
        "192.168.199.23",
    ]
    all_security_group_ids = [
        "c040fa53-c03c-459d-b3b5-6788b1596702",
        "da8ddebd-fe49-42e3-9100-a9369d20f1cf",
    ]
    all_tags               = []
    dns_assignment         = [
        {
            "hostname"   = "host-192-168-199-23"
            "ip_address" = "192.168.199.23"
        },
    ]
    id                     = "c2fe8ab7-8540-4a10-89bc-524f0262e9b0"
    mac_address            = "fa:16:3e:3f:10:c0"
    name                   = "port_1"
    network_id             = "b4e306f8-3c2b-4489-87b0-1b438ff18977"
    port_security_enabled  = true
    region                 = "RegionOne"
    sdn                    = "neutron"
    tags                   = []

    fixed_ip {
        ip_address = "192.168.199.23"
        subnet_id  = "8fa611c7-9a91-47ab-8be3-e941f024f724"
    }
}

# vkcs_networking_port_secgroup_associate.port:
resource "vkcs_networking_port_secgroup_associate" "port" {
    all_security_group_ids = [
        "c040fa53-c03c-459d-b3b5-6788b1596702",
        "da8ddebd-fe49-42e3-9100-a9369d20f1cf",
    ]
    enforce                = false
    id                     = "c2fe8ab7-8540-4a10-89bc-524f0262e9b0"
    port_id                = "c2fe8ab7-8540-4a10-89bc-524f0262e9b0"
    region                 = "RegionOne"
    sdn                    = "neutron"
    security_group_ids     = [
        "c040fa53-c03c-459d-b3b5-6788b1596702",
    ]
}

# vkcs_networking_router.router:
resource "vkcs_networking_router" "router" {
    admin_state_up      = true
    all_tags            = []
    external_network_id = "298117ae-3fa4-4109-9e08-8be5602be5a2"
    id                  = "79f986c6-dc95-43d3-8c57-56eebd827157"
    name                = "router"
    region              = "RegionOne"
    sdn                 = "neutron"
    tags                = []
}

# vkcs_networking_router_interface.db:
resource "vkcs_networking_router_interface" "db" {
    id        = "dd00a3eb-6e73-4354-8439-5d904d8d87d5"
    port_id   = "dd00a3eb-6e73-4354-8439-5d904d8d87d5"
    region    = "RegionOne"
    router_id = "79f986c6-dc95-43d3-8c57-56eebd827157"
    sdn       = "neutron"
    subnet_id = "8fa611c7-9a91-47ab-8be3-e941f024f724"
}

# vkcs_networking_secgroup.secgroup:
resource "vkcs_networking_secgroup" "secgroup" {
    all_tags    = []
    description = "terraform security group"
    id          = "c040fa53-c03c-459d-b3b5-6788b1596702"
    name        = "security_group"
    region      = "RegionOne"
    sdn         = "neutron"
    tags        = []
}

# vkcs_networking_secgroup_rule.secgroup_rule_1:
resource "vkcs_networking_secgroup_rule" "secgroup_rule_1" {
    description       = "secgroup_rule_1"
    direction         = "ingress"
    ethertype         = "IPv4"
    id                = "803e6639-23f0-47b3-aab9-273a4185e2db"
    port_range_max    = 22
    port_range_min    = 22
    protocol          = "tcp"
    region            = "RegionOne"
    remote_ip_prefix  = "0.0.0.0/0"
    sdn               = "neutron"
    security_group_id = "c040fa53-c03c-459d-b3b5-6788b1596702"
}

# vkcs_networking_secgroup_rule.secgroup_rule_2:
resource "vkcs_networking_secgroup_rule" "secgroup_rule_2" {
    direction         = "ingress"
    ethertype         = "IPv4"
    id                = "2978aeea-0e5a-414e-b0aa-0ca8e94154b7"
    port_range_max    = 3389
    port_range_min    = 3389
    protocol          = "tcp"
    region            = "RegionOne"
    remote_ip_prefix  = "0.0.0.0/0"
    sdn               = "neutron"
    security_group_id = "c040fa53-c03c-459d-b3b5-6788b1596702"
}

# vkcs_networking_subnet.subnetwork:
resource "vkcs_networking_subnet" "subnetwork" {
    all_tags        = []
    cidr            = "192.168.199.0/24"
    dns_nameservers = []
    enable_dhcp     = true
    gateway_ip      = "192.168.199.1"
    id              = "8fa611c7-9a91-47ab-8be3-e941f024f724"
    name            = "subnet_1"
    network_id      = "b4e306f8-3c2b-4489-87b0-1b438ff18977"
    no_gateway      = false
    region          = "RegionOne"
    sdn             = "neutron"
    tags            = []

    allocation_pool {
        end   = "192.168.199.254"
        start = "192.168.199.2"
    }
}


Outputs:

instance_fip = "212.233.95.12"
```

The output of the `terraform state list` command:

```shell
data.vkcs_compute_flavor.compute
data.vkcs_images_image.compute
data.vkcs_networking_network.extnet
vkcs_compute_floatingip_associate.fip
vkcs_compute_instance.compute
vkcs_networking_floatingip.fip
vkcs_networking_network.network
vkcs_networking_port.port
vkcs_networking_port_secgroup_associate.port
vkcs_networking_router.router
vkcs_networking_router_interface.db
vkcs_networking_secgroup.secgroup
vkcs_networking_secgroup_rule.secgroup_rule_1
vkcs_networking_secgroup_rule.secgroup_rule_2
vkcs_networking_subnet.subnetwork
```

A part of the log with the applied changes:

```shell
data.vkcs_networking_network.extnet: Reading...
data.vkcs_compute_flavor.compute: Reading...
data.vkcs_images_image.compute: Reading...
vkcs_networking_secgroup.secgroup: Refreshing state... [id=c040fa53-c03c-459d-b3b5-6788b1596702]
vkcs_networking_network.network: Refreshing state... [id=b4e306f8-3c2b-4489-87b0-1b438ff18977]
data.vkcs_compute_flavor.compute: Read complete after 1s [id=df3c499a-044f-41d2-8612-d303adc613cc]
data.vkcs_images_image.compute: Read complete after 1s [id=b75595ca-4e1d-47e0-8e95-7a02edc0e242]
vkcs_networking_subnet.subnetwork: Refreshing state... [id=8fa611c7-9a91-47ab-8be3-e941f024f724]
vkcs_networking_secgroup_rule.secgroup_rule_1: Refreshing state... [id=803e6639-23f0-47b3-aab9-273a4185e2db]
vkcs_networking_secgroup_rule.secgroup_rule_2: Refreshing state... [id=2978aeea-0e5a-414e-b0aa-0ca8e94154b7]
vkcs_compute_instance.compute: Refreshing state... [id=d3009ee1-a0ee-405b-af04-48d2700f195a]
vkcs_networking_port.port: Refreshing state... [id=c2fe8ab7-8540-4a10-89bc-524f0262e9b0]
data.vkcs_networking_network.extnet: Read complete after 1s [id=298117ae-3fa4-4109-9e08-8be5602be5a2]
vkcs_networking_floatingip.fip: Refreshing state... [id=ee19f1d4-5b98-4545-b752-8baab563464a]
vkcs_networking_router.router: Refreshing state... [id=79f986c6-dc95-43d3-8c57-56eebd827157]
vkcs_networking_port_secgroup_associate.port: Refreshing state... [id=c2fe8ab7-8540-4a10-89bc-524f0262e9b0]
vkcs_networking_router_interface.db: Refreshing state... [id=dd00a3eb-6e73-4354-8439-5d904d8d87d5]
vkcs_compute_floatingip_associate.fip: Refreshing state... [id=212.233.95.12/d3009ee1-a0ee-405b-af04-48d2700f195a/]

No changes. Your infrastructure matches the configuration.

Terraform has compared your real infrastructure against your configuration and found no differences, so no changes are needed.
╷
│ Warning: Argument is deprecated
│
│   with vkcs_networking_secgroup_rule.secgroup_rule_1,
│   on network.tf line 34, in resource "vkcs_networking_secgroup_rule" "secgroup_rule_1":
│   34:    ethertype = "IPv4"
│
│ Only IPv4 can be used as ethertype. This argument is deprecated, please do not use it.
│
│ (and 3 more similar warnings elsewhere)
╵

Apply complete! Resources: 0 added, 0 changed, 0 destroyed.

Outputs:

instance_fip = "212.233.95.12"
ubuntu@ubuntu-basic-1-2-20gb:~/dev-ops-inno/terraform/vk-cloud$ nano main.tf
ubuntu@ubuntu-basic-1-2-20gb:~/dev-ops-inno/terraform/vk-cloud$ sudo terraform apply
data.vkcs_images_image.compute: Reading...
vkcs_networking_secgroup.secgroup: Refreshing state... [id=c040fa53-c03c-459d-b3b5-6788b1596702]
vkcs_networking_network.network: Refreshing state... [id=b4e306f8-3c2b-4489-87b0-1b438ff18977]
data.vkcs_compute_flavor.compute: Reading...
data.vkcs_networking_network.extnet: Reading...
vkcs_networking_secgroup_rule.secgroup_rule_2: Refreshing state... [id=2978aeea-0e5a-414e-b0aa-0ca8e94154b7]
vkcs_networking_secgroup_rule.secgroup_rule_1: Refreshing state... [id=803e6639-23f0-47b3-aab9-273a4185e2db]
data.vkcs_images_image.compute: Read complete after 0s [id=b75595ca-4e1d-47e0-8e95-7a02edc0e242]
data.vkcs_compute_flavor.compute: Read complete after 0s [id=df3c499a-044f-41d2-8612-d303adc613cc]
vkcs_networking_subnet.subnetwork: Refreshing state... [id=8fa611c7-9a91-47ab-8be3-e941f024f724]
vkcs_compute_instance.compute: Refreshing state... [id=d3009ee1-a0ee-405b-af04-48d2700f195a]
vkcs_networking_port.port: Refreshing state... [id=c2fe8ab7-8540-4a10-89bc-524f0262e9b0]
data.vkcs_networking_network.extnet: Read complete after 1s [id=298117ae-3fa4-4109-9e08-8be5602be5a2]
vkcs_networking_floatingip.fip: Refreshing state... [id=ee19f1d4-5b98-4545-b752-8baab563464a]
vkcs_networking_router.router: Refreshing state... [id=79f986c6-dc95-43d3-8c57-56eebd827157]
vkcs_networking_port_secgroup_associate.port: Refreshing state... [id=c2fe8ab7-8540-4a10-89bc-524f0262e9b0]
vkcs_networking_router_interface.db: Refreshing state... [id=dd00a3eb-6e73-4354-8439-5d904d8d87d5]
vkcs_compute_floatingip_associate.fip: Refreshing state... [id=212.233.95.12/d3009ee1-a0ee-405b-af04-48d2700f195a/]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  ~ update in-place

Terraform will perform the following actions:

  # vkcs_compute_instance.compute will be updated in-place
  ~ resource "vkcs_compute_instance" "compute" {
        id                  = "d3009ee1-a0ee-405b-af04-48d2700f195a"
      ~ name                = "compute-instance" -> "vk-devops"
        tags                = []
        # (13 unchanged attributes hidden)

        # (2 unchanged blocks hidden)
    }

Plan: 0 to add, 1 to change, 0 to destroy.
╷
│ Warning: Argument is deprecated
│
│   with vkcs_networking_secgroup_rule.secgroup_rule_1,
│   on network.tf line 34, in resource "vkcs_networking_secgroup_rule" "secgroup_rule_1":
│   34:    ethertype = "IPv4"
│
│ Only IPv4 can be used as ethertype. This argument is deprecated, please do not use it.
│
│ (and 3 more similar warnings elsewhere)
╵

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

vkcs_compute_instance.compute: Modifying... [id=d3009ee1-a0ee-405b-af04-48d2700f195a]
vkcs_compute_instance.compute: Modifications complete after 2s [id=d3009ee1-a0ee-405b-af04-48d2700f195a]

Apply complete! Resources: 0 added, 1 changed, 0 destroyed.

Outputs:

instance_fip = "212.233.95.12"
```

The output of the `terraform output` command:

```shell
instance_fip = "212.233.95.12"
```

## Terraform for GitHub

The output of `terraform init` command:

```shell
Initializing the backend...

Initializing provider plugins...
- Finding integrations/github versions matching "~> 4.0"...
- Installing integrations/github v4.31.0...
- Installed integrations/github v4.31.0 (unauthenticated)

Terraform has created a lock file .terraform.lock.hcl to record the provider
selections it made above. Include this file in your version control repository
so that Terraform can guarantee to make the same selections by default when
you run "terraform init" in the future.

╷
│ Warning: Incomplete lock file information for providers
│
│ Due to your customized provider installation methods, Terraform was forced to calculate lock file checksums locally for the following providers:
│   - integrations/github
│
│ The current .terraform.lock.hcl file only includes checksums for linux_amd64, so Terraform running on another platform will fail to install these providers.
│
│ To calculate additional checksums for another platform, run:
│   terraform providers lock -platform=linux_amd64
│ (where linux_amd64 is the platform to generate)
╵

Terraform has been successfully initialized!

You may now begin working with Terraform. Try running "terraform plan" to see
any changes that are required for your infrastructure. All Terraform commands
should now work.

If you ever set or change modules or backend configuration for Terraform,
rerun this command to reinitialize your working directory. If you forget, other
commands will detect it and remind you to do so if necessary.

```

The output for `terraform aply` command:

```shell
Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # github_branch_default.master will be created
  + resource "github_branch_default" "master" {
      + branch     = "main"
      + id         = (known after apply)
      + repository = "DevOps-2024"
    }

  # github_branch_protection.default will be created
  + resource "github_branch_protection" "default" {
      + allows_deletions                = false
      + allows_force_pushes             = false
      + blocks_creations                = false
      + enforce_admins                  = true
      + id                              = (known after apply)
      + pattern                         = "main"
      + repository_id                   = (known after apply)
      + require_conversation_resolution = true
      + require_signed_commits          = false
      + required_linear_history         = false

      + required_pull_request_reviews {
          + required_approving_review_count = 1
        }
    }

  # github_repository.repo will be created
  + resource "github_repository" "repo" {
      + allow_auto_merge            = false
      + allow_merge_commit          = true
      + allow_rebase_merge          = true
      + allow_squash_merge          = true
      + archived                    = false
      + auto_init                   = true
      + branches                    = (known after apply)
      + default_branch              = (known after apply)
      + delete_branch_on_merge      = false
      + description                 = "IU DevOps course lab4"
      + etag                        = (known after apply)
      + full_name                   = (known after apply)
      + git_clone_url               = (known after apply)
      + gitignore_template          = "VisualStudio"
      + has_issues                  = true
      + has_wiki                    = true
      + html_url                    = (known after apply)
      + http_clone_url              = (known after apply)
      + id                          = (known after apply)
      + license_template            = "mit"
      + merge_commit_message        = "PR_TITLE"
      + merge_commit_title          = "MERGE_MESSAGE"
      + name                        = "DevOps-2024"
      + node_id                     = (known after apply)
      + private                     = (known after apply)
      + repo_id                     = (known after apply)
      + squash_merge_commit_message = "COMMIT_MESSAGES"
      + squash_merge_commit_title   = "COMMIT_OR_PR_TITLE"
      + ssh_clone_url               = (known after apply)
      + svn_url                     = (known after apply)
      + visibility                  = "public"
    }

Plan: 3 to add, 0 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

github_repository.repo: Creating...
github_repository.repo: Creation complete after 6s [id=DevOps-2024]
github_branch_default.master: Creating...
github_branch_default.master: Creation complete after 1s [id=DevOps-2024]
github_branch_protection.default: Creating...
github_branch_protection.default: Creation complete after 4s [id=BPR_kwDOLYT7s84C0l_B]

Apply complete! Resources: 3 added, 0 changed, 0 destroyed.
```

The output for `terraform apply command` after importing my existing GitHub repository:

```shell
github_repository.new: Refreshing state... [id=new]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create
  ~ update in-place

Terraform will perform the following actions:

  # github_branch_default.master will be created
  + resource "github_branch_default" "master" {
      + branch     = "main"
      + id         = (known after apply)
      + repository = "DevOps-2024"
    }

  # github_branch_protection.default will be created
  + resource "github_branch_protection" "default" {
      + allows_deletions                = false
      + allows_force_pushes             = false
      + blocks_creations                = false
      + enforce_admins                  = true
      + id                              = (known after apply)
      + pattern                         = "main"
      + repository_id                   = (known after apply)
      + require_conversation_resolution = true
      + require_signed_commits          = false
      + required_linear_history         = false

      + required_pull_request_reviews {
          + required_approving_review_count = 1
        }
    }

  # github_repository.new will be updated in-place
  ~ resource "github_repository" "new" {
      - description                 = "sth" -> null
      - has_downloads               = true -> null
      - has_issues                  = true -> null
      - has_projects                = true -> null
      - has_wiki                    = true -> null
        id                          = "new"
        name                        = "new"
      - vulnerability_alerts        = true -> null
        # (26 unchanged attributes hidden)
    }

  # github_repository.repo will be created
  + resource "github_repository" "repo" {
      + allow_auto_merge            = false
      + allow_merge_commit          = true
      + allow_rebase_merge          = true
      + allow_squash_merge          = true
      + archived                    = false
      + auto_init                   = true
      + branches                    = (known after apply)
      + default_branch              = (known after apply)
      + delete_branch_on_merge      = false
      + description                 = "IU DevOps course lab4"
      + etag                        = (known after apply)
      + full_name                   = (known after apply)
      + git_clone_url               = (known after apply)
      + gitignore_template          = "VisualStudio"
      + has_issues                  = true
      + has_wiki                    = true
      + html_url                    = (known after apply)
      + http_clone_url              = (known after apply)
      + id                          = (known after apply)
      + license_template            = "mit"
      + merge_commit_message        = "PR_TITLE"
      + merge_commit_title          = "MERGE_MESSAGE"
      + name                        = "DevOps-2024"
      + node_id                     = (known after apply)
      + private                     = (known after apply)
      + repo_id                     = (known after apply)
      + squash_merge_commit_message = "COMMIT_MESSAGES"
      + squash_merge_commit_title   = "COMMIT_OR_PR_TITLE"
      + ssh_clone_url               = (known after apply)
      + svn_url                     = (known after apply)
      + visibility                  = "public"
    }

Plan: 3 to add, 1 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

github_repository.repo: Creating...
github_repository.new: Modifying... [id=new]
github_repository.repo: Creation complete after 8s [id=DevOps-2024]
github_branch_default.master: Creating...
github_repository.new: Modifications complete after 8s [id=new]
github_branch_default.master: Creation complete after 2s [id=DevOps-2024]
github_branch_protection.default: Creating...
github_branch_protection.default: Creation complete after 4s [id=BPR_kwDOLYUcJM4C0mIX]

Apply complete! Resources: 3 added, 1 changed, 0 destroyed.
```

## Best Practises
1. **Utilization of a Remote Backend**: 
I have adopted the practice of storing Terraform state in a remote backend, specifically VK Cloud. 
This approach facilitates collaboration among team members and enhances the security and integrity of the state files.

2. **Enhanced Token Security**: To maintain the confidentiality of the GitHub token, I employ environment variables for 
its storage. This method ensures that sensitive information is kept secure and is not hard-coded into the Terraform 
configurations.

3. **Management of Input Variables and Outputs**: I systematically define input variables, including those for the 
GitHub token and other modifiable parameters, to streamline the configuration process. Additionally, I leverage outputs
to obtain a direct link to the GitHub repository upon the successful application of changes.
4. **Well-Organized Directory Structure**: The Terraform configurations are meticulously organized within distinct 
directories, each corresponding to its specific platform. This organized structure ensures the configurations are 
easily navigable and maintainable.