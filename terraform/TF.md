# Terraform

## Output of `terraform state show`

```markdown
(venv) PS D:\Study\DevOps\terraform\docker> terraform state show docker_container.nginx

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

## Output of `terraform state list`

```markdown
(venv) PS D:\Study\DevOps\terraform\docker> terraform state list
docker_container.nginx
docker_image.nginx
```

## Output of `terraform apply` after changes

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

## Output of `terraform output`

```markdown
(venv) PS D:\Study\DevOps\terraform\docker> terraform output
container_id = "2c4bf14ee7712f879ebf6326a616dbac822d3b647e869be9d38f4017fb8bbbaf"
image_id = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666anginx:latest"
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