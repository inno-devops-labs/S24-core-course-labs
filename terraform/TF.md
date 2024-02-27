# Terraform

## Infrastructures

### Docker

```bash
> terraform show
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
    hostname                                    = "b2f6e5313557"
    id                                          = "b2f6e5313557815aa7d8e809f4b29b137b51c62578a694cfe63833dc798d26b2"
    image                                       = "sha256:61395b4c586da2b9b3b7ca903ea6a448e6783dfdd7f768ff2c1a0f3360aaba99"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "tutorial"
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

# docker_image.nginx:
resource "docker_image" "nginx" {
    id           = "sha256:61395b4c586da2b9b3b7ca903ea6a448e6783dfdd7f768ff2c1a0f3360aaba99nginx:latest"
    image_id     = "sha256:61395b4c586da2b9b3b7ca903ea6a448e6783dfdd7f768ff2c1a0f3360aaba99"
    keep_locally = false
    name         = "nginx:latest"
    repo_digest  = "nginx@sha256:32da30332506740a2f7c34d5dc70467b7f14ec67d912703568daff790ab3f755"
}
```

```bash
> terraform state list
docker_container.nginx
docker_image.nginx
```

```bash
> terraform output
container_id = "cef2761b51942d36f4c767571c18add6e20c52c7baaa50a18632a37d33d6fc9a"
image_id = "sha256:61395b4c586da2b9b3b7ca903ea6a448e6783dfdd7f768ff2c1a0f3360aaba99nginx:latest"
```

### VK Cloud

```bash
> terraform show
# data.vkcs_compute_flavor.compute:
data "vkcs_compute_flavor" "compute" {
    disk         = 20
    extra_specs  = {
        "agg_common"     = "true"
        "hw:cpu_sockets" = "1"
        "mcs:cpu_type"   = "standard"
    }
    flavor_id    = "25ae869c-be29-4840-8e12-99e046d2dbd4"
    id           = "25ae869c-be29-4840-8e12-99e046d2dbd4"
    is_public    = true
    name         = "Basic-1-2-20"
    ram          = 2048
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
    floating_ip = "95.163.251.14"
    id          = "95.163.251.14/225da104-7288-4737-a9ce-1d5603a0f420/"
    instance_id = "225da104-7288-4737-a9ce-1d5603a0f420"
    region      = "RegionOne"
}

# vkcs_compute_instance.compute:
resource "vkcs_compute_instance" "compute" {
    access_ip_v4        = "192.168.199.27"
    all_metadata        = {}
    all_tags            = []
    availability_zone   = "MS1"
    flavor_id           = "25ae869c-be29-4840-8e12-99e046d2dbd4"
    flavor_name         = "Basic-1-2-20"
    force_delete        = false
    id                  = "225da104-7288-4737-a9ce-1d5603a0f420"
    image_id            = "Attempt to boot from volume - no image supplied"
    key_pair            = "keypair-terraform"
    name                = "compute-instance"
    power_state         = "active"
    region              = "RegionOne"
    security_groups     = [
        "default",
        "security_group",
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
        fixed_ip_v4    = "192.168.199.27"
        mac            = "fa:16:3e:bc:7c:54"
        name           = "net"
        uuid           = "98cc9a30-b34b-4b8b-a074-5f0d6d4a9024"
    }
}

# vkcs_networking_floatingip.fip:
resource "vkcs_networking_floatingip" "fip" {
    address = "95.163.251.14"
    id      = "48024815-e12c-4f52-b186-d0f6d5d540c7"
    pool    = "ext-net"
    region  = "RegionOne"
    sdn     = "neutron"
}

# vkcs_networking_network.network:
resource "vkcs_networking_network" "network" {
    admin_state_up        = true
    all_tags              = []
    id                    = "98cc9a30-b34b-4b8b-a074-5f0d6d4a9024"
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
        "3859d743-62cd-44d1-8fab-d5f1c6aac7f5",
        "c7f81796-df09-4bf6-b218-d9ca196e800e",
    ]
    all_tags               = []
    dns_assignment         = [
        {
            "hostname"   = "host-192-168-199-23"
            "ip_address" = "192.168.199.23"
        },
    ]
    id                     = "68805959-02f4-474a-a8cd-635d9a9769ce"
    mac_address            = "fa:16:3e:ae:0c:18"
    name                   = "port_1"
    network_id             = "98cc9a30-b34b-4b8b-a074-5f0d6d4a9024"
    port_security_enabled  = true
    region                 = "RegionOne"
    sdn                    = "neutron"
    tags                   = []

    fixed_ip {
        ip_address = "192.168.199.23"
        subnet_id  = "81e8d120-2447-4d71-9277-02763fffbde6"
    }
}

# vkcs_networking_port_secgroup_associate.port:
resource "vkcs_networking_port_secgroup_associate" "port" {
    all_security_group_ids = [
        "3859d743-62cd-44d1-8fab-d5f1c6aac7f5",
        "c7f81796-df09-4bf6-b218-d9ca196e800e",
    ]
    enforce                = false
    id                     = "68805959-02f4-474a-a8cd-635d9a9769ce"
    port_id                = "68805959-02f4-474a-a8cd-635d9a9769ce"
    region                 = "RegionOne"
    sdn                    = "neutron"
    security_group_ids     = [
        "3859d743-62cd-44d1-8fab-d5f1c6aac7f5",
    ]
}

# vkcs_networking_router.router:
resource "vkcs_networking_router" "router" {
    admin_state_up      = true
    all_tags            = []
    external_network_id = "298117ae-3fa4-4109-9e08-8be5602be5a2"
    id                  = "3b9dbe0e-701a-48d3-9298-0130c3df2205"
    name                = "router"
    region              = "RegionOne"
    sdn                 = "neutron"
    tags                = []
}

# vkcs_networking_router_interface.db:
resource "vkcs_networking_router_interface" "db" {
    id        = "8ae1331f-c5ee-4e0f-98a4-ed4cdfb4cdbf"
    port_id   = "8ae1331f-c5ee-4e0f-98a4-ed4cdfb4cdbf"
    region    = "RegionOne"
    router_id = "3b9dbe0e-701a-48d3-9298-0130c3df2205"
    sdn       = "neutron"
    subnet_id = "81e8d120-2447-4d71-9277-02763fffbde6"
}

# vkcs_networking_secgroup.secgroup:
resource "vkcs_networking_secgroup" "secgroup" {
    all_tags    = []
    description = "terraform security group"
    id          = "3859d743-62cd-44d1-8fab-d5f1c6aac7f5"
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
    id                = "73ae8f71-8715-4077-b6d9-c26a6cde2b51"
    port_range_max    = 22
    port_range_min    = 22
    protocol          = "tcp"
    region            = "RegionOne"
    remote_ip_prefix  = "0.0.0.0/0"
    sdn               = "neutron"
    security_group_id = "3859d743-62cd-44d1-8fab-d5f1c6aac7f5"
}

# vkcs_networking_secgroup_rule.secgroup_rule_2:
resource "vkcs_networking_secgroup_rule" "secgroup_rule_2" {
    direction         = "ingress"
    ethertype         = "IPv4"
    id                = "86b9b6ec-07d0-4fae-9e33-104915cc570a"
    port_range_max    = 3389
    port_range_min    = 3389
    protocol          = "tcp"
    region            = "RegionOne"
    remote_ip_prefix  = "0.0.0.0/0"
    sdn               = "neutron"
    security_group_id = "3859d743-62cd-44d1-8fab-d5f1c6aac7f5"
}

# vkcs_networking_subnet.subnetwork:
resource "vkcs_networking_subnet" "subnetwork" {
    all_tags        = []
    cidr            = "192.168.199.0/24"
    dns_nameservers = []
    enable_dhcp     = true
    gateway_ip      = "192.168.199.1"
    id              = "81e8d120-2447-4d71-9277-02763fffbde6"
    name            = "subnet_1"
    network_id      = "98cc9a30-b34b-4b8b-a074-5f0d6d4a9024"
    no_gateway      = false
    region          = "RegionOne"
    sdn             = "neutron"
    tags            = []

    allocation_pool {
        end   = "192.168.199.254"
        start = "192.168.199.2"
    }
}
```

```bash
> terraform state list
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

```bash
> terraform output
instance_fip = "95.163.251.14"
```

### Github

```bash
> terraform show 
# github_branch_default.main:
resource "github_branch_default" "main" {
    branch     = "main"
    id         = "devops-engineering-course"
    rename     = false
    repository = "devops-engineering-course"
}

# github_branch_protection.default:
resource "github_branch_protection" "default" {
    allows_deletions                = false
    allows_force_pushes             = false
    blocks_creations                = false
    enforce_admins                  = true
    force_push_bypassers            = []
    id                              = "BPR_kwDOKO4CUc4CgWzs"
    lock_branch                     = false
    pattern                         = "main"
    push_restrictions               = []
    repository_id                   = "devops-engineering-course-terraform"
    require_conversation_resolution = true
    require_signed_commits          = false
    required_linear_history         = false

    required_pull_request_reviews {
        dismiss_stale_reviews           = false
        dismissal_restrictions          = []
        pull_request_bypassers          = []
        require_code_owner_reviews      = false
        require_last_push_approval      = false
        required_approving_review_count = 1
        restrict_dismissals             = false
    }
}

# github_repository.repo:
resource "github_repository" "repo" {
    allow_auto_merge            = false
    allow_merge_commit          = true
    allow_rebase_merge          = true
    allow_squash_merge          = true
    allow_update_branch         = false
    archived                    = false
    auto_init                   = true
    default_branch              = "main"
    delete_branch_on_merge      = false
    etag                        = "W/\"8730d189851e0e570e1c9bed03574bf1e16790fb3aa44783a551e78b6768799e\""
    full_name                   = "Majorro/devops-engineering-course"
    git_clone_url               = "git://github.com/Majorro/devops-engineering-course.git"
    has_discussions             = false
    has_downloads               = false
    has_issues                  = false
    has_projects                = false
    has_wiki                    = false
    html_url                    = "https://github.com/Majorro/devops-engineering-course"
    http_clone_url              = "https://github.com/Majorro/devops-engineering-course.git"
    id                          = "devops-engineering-course"
    is_template                 = false
    merge_commit_message        = "PR_TITLE"
    merge_commit_title          = "MERGE_MESSAGE"
    name                        = "devops-engineering-course"
    node_id                     = "R_kgDOKO4CUQ"
    primary_language            = "C#"
    private                     = false
    repo_id                     = 686686801
    squash_merge_commit_message = "COMMIT_MESSAGES"
    squash_merge_commit_title   = "COMMIT_OR_PR_TITLE"
    ssh_clone_url               = "git@github.com:Majorro/devops-engineering-course.git"
    svn_url                     = "https://github.com/Majorro/devops-engineering-course"
    topics                      = []
    visibility                  = "public"
    vulnerability_alerts        = false

    security_and_analysis {
        secret_scanning {
            status = "disabled"
        }
        secret_scanning_push_protection {
            status = "disabled"
        }
    }
}
```

```bash
> terraform state list  
github_branch_default.main
github_branch_protection.default
github_repository.repo
```

## Best practices

- `terraform fmt` to format `.tf` files
- `terraform validate` to check syntax
- scoping
- separation of terraform items to different files
- variables for secrets
