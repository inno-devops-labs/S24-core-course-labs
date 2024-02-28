# Terraform

## Docker

### Commands Outputs:

1. `terraform state show`

   Gives the following output:

   ```bash
   # docker_container.python-app:
   resource "docker_container" "python-app" {
       attach                                      = false
       command                                     = [
           "python",
           "-m",
           "flask",
           "run",
           "--host=0.0.0.0",
       ]
       container_read_refresh_timeout_milliseconds = 15000
       cpu_shares                                  = 0
       entrypoint                                  = []
       env                                         = []
       hostname                                    = "27fa92256d1a"
       id                                          = "27fa92256d1a2832d5cbced716060016629c3726326f3b1a8f49ad3e27ee66c0"
       image                                       = "sha256:1a52404b19db4fab9045f988fed1d536e8c4533e41a59943fe1cf166c1bbd53e"
       init                                        = false
       ipc_mode                                    = "private"
       log_driver                                  = "json-file"
       logs                                        = false
       max_retry_count                             = 0
       memory                                      = 0
       memory_swap                                 = 0
       must_run                                    = true
       name                                        = "python-app"
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
       user                                        = "user"
       wait                                        = false
       wait_timeout                                = 60
       working_dir                                 = "/app"

       ports {
           external = 8000
           internal = 80
           ip       = "0.0.0.0"
           protocol = "tcp"
       }
   }
   ```

2. `terraform state list`

   Gives the following output:

   ```bash
   docker_container.python-app
   ```

Now, the docker container is running and the Moscow Time python app is hosted on the port:

```bash
http://localhost:5000/
```

### Utilizing input variables:

Created the file

```bash
variables.tf
```

The 4 variables defined here are

- The Docker container name
- The Docker container image
- The internal port
- The external port

### Outputs:

`terraform output`

Gives the following output:

```bash
container_id = "a56007b1c5f51ad891bf28e4c26337cf9863dcb0e6cbdb3150c58db42cacae92"
image_id = "python-app"
```

## AWS

### Commands Outputs:

1. `terraform state show`

   Gives the following output:

   ```bash
   # aws_instance.app_server:
   resource "aws_instance" "app_server" {
       ami                                  = "ami-830c94e3"
       arn                                  = "arn:aws:ec2:us-west-2:654654554951:instance/i-0de5e2db4fe2ce378"
       associate_public_ip_address          = true
       availability_zone                    = "us-west-2b"
       cpu_core_count                       = 1
       cpu_threads_per_core                 = 1
       disable_api_stop                     = false
       disable_api_termination              = false
       ebs_optimized                        = false
       get_password_data                    = false
       hibernation                          = false
       id                                   = "i-0de5e2db4fe2ce378"
       instance_initiated_shutdown_behavior = "stop"
       instance_state                       = "running"
       instance_type                        = "t2.micro"
       ipv6_address_count                   = 0
       ipv6_addresses                       = []
       monitoring                           = false
       placement_partition_number           = 0
       primary_network_interface_id         = "eni-0bc356c299d211e2f"
       private_dns                          = "ip-172-31-25-208.us-west-2.compute.internal"
       private_ip                           = "172.31.25.208"
       public_dns                           = "ec2-35-87-106-97.us-west-2.compute.amazonaws.com"
       public_ip                            = "35.87.106.97"
       secondary_private_ips                = []
       security_groups                      = [
           "default",
       ]
       source_dest_check                    = true
       subnet_id                            = "subnet-0a16c191fca6d4396"
       tags                                 = {
           "Name" = "LabAppServerInstance"
       }
       tags_all                             = {
           "Name" = "LabAppServerInstance"
       }
       tenancy                              = "default"
       user_data_replace_on_change          = false
       vpc_security_group_ids               = [
           "sg-0dffd75e2f67cbb94",
       ]

       capacity_reservation_specification {
           capacity_reservation_preference = "open"
       }

       cpu_options {
           core_count       = 1
           threads_per_core = 1
       }

       credit_specification {
           cpu_credits = "standard"
       }

       enclave_options {
           enabled = false
       }

       maintenance_options {
           auto_recovery = "default"
       }

       metadata_options {
           http_endpoint               = "enabled"
           http_put_response_hop_limit = 1
           http_tokens                 = "optional"
           instance_metadata_tags      = "disabled"
       }

       private_dns_name_options {
           enable_resource_name_dns_a_record    = false
           enable_resource_name_dns_aaaa_record = false
           hostname_type                        = "ip-name"
       }

       root_block_device {
           delete_on_termination = true
           device_name           = "/dev/sda1"
           encrypted             = false
           iops                  = 0
           tags                  = {}
           throughput            = 0
           volume_id             = "vol-0684df6603c568499"
           volume_size           = 8
           volume_type           = "standard"
       }
   }


   Outputs:

   aws-instance-app-server-id = "i-0de5e2db4fe2ce378"
   PS D:\VSCodeProjects\DevOps\S24-core-course-labs\terraform\AWS>
   ```

2. `terraform state list`

   Gives the following output:

   ```bash
   aws_instance.app_server
   ```

---

### Utilizing input variables:

Created the file

```bash
variables.tf
```

It includes the provider region.

### Outputs:

```bash
terraform output
```

Gives the following output:

```bash
aws-instance-app-server-id = "i-0de5e2db4fe2ce378"
```

## Github

1. `terraform plan -out deploy.tfplan`

   Gives the following output:

   ```bash
   var.token
   Specifies the GitHub PAT token

   Enter a value:


   Terraform used the selected providers to generate the following execution plan. Resource actions are
   indicated with the following symbols:
   + create

   Terraform will perform the following actions:

   # github_branch_default.main will be created
   + resource "github_branch_default" "main" {
       + branch     = "main"
       + etag       = (known after apply)
       + id         = (known after apply)
       + rename     = false
       + repository = "DevOps-Lab04-repo"
       }

   # github_branch_protection.default will be created
   + resource "github_branch_protection" "default" {
       + allows_deletions                = false
       + allows_force_pushes             = false
       + blocks_creations                = false
       + enforce_admins                  = true
       + id                              = (known after apply)
       + lock_branch                     = false
       + pattern                         = "main"
       + repository_id                   = (known after apply)
       + require_conversation_resolution = true
       + require_signed_commits          = false
       + required_linear_history         = false

       + required_pull_request_reviews {
           + require_last_push_approval      = false
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
       + default_branch              = (known after apply)
       + delete_branch_on_merge      = false
       + description                 = "Using terraform with Github providers"
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
       + name                        = "DevOps-Lab04-repo"
       + node_id                     = (known after apply)
       + primary_language            = (known after apply)
       + private                     = (known after apply)
       + repo_id                     = (known after apply)
       + squash_merge_commit_message = "COMMIT_MESSAGES"
       + squash_merge_commit_title   = "COMMIT_OR_PR_TITLE"
       + ssh_clone_url               = (known after apply)
       + svn_url                     = (known after apply)
       + topics                      = (known after apply)
       + visibility                  = "public"
       + web_commit_signoff_required = false
       }

   Plan: 3 to add, 0 to change, 0 to destroy.

   ─────────────────────────────────────────────────────────────────────────────────────────────────────────────

   Saved the plan to: deploy.tfplan

   To perform exactly these actions, run the following command to apply:
       terraform apply "deploy.tfplan"
   ```

2. `terraform apply deploy.tfplan`

   Gives the following output:

   ```bash
   github_repository.repo: Creating...
   github_repository.repo: Creation complete after 5s [id=DevOps-Lab04-repo]
   github_branch_default.main: Creating...
   github_branch_default.main: Creation complete after 2s [id=DevOps-Lab04-repo]
   github_branch_protection.default: Creating...
   github_branch_protection.default: Creation complete after 4s [id=BPR_kwDOLZAMe84C0zQ-]

   Apply complete! Resources: 3 added, 0 changed, 0 destroyed.
   ```

## Best Practices

1. **Validate Before Applying:**

   - Using `terraform validate` to ensure syntax correctness before making any changes.

2. **Format for Readability:**

   - Employing `terraform fmt` to maintain consistent and readable code formatting.

3. **Centralize Variables and Outputs:**

   - Storing variables in `variables.tf` and outputs in `outputs.tf` for easier management and access.

4. **Secure Sensitive Data:**

   - Avoiding storing sensitive information directly in code; prompt for input during `terraform apply` or use secure storage methods like environment variables.

5. **Protect Terraform State:**

   - Keeping Terraform state files (`terraform.tfstate` and `.backup`) out of version control to prevent exposure of sensitive data.

6. **Specify Versioning:**
   - Explicitly declaring Terraform and provider versions to ensure consistent behavior and compatibility.
