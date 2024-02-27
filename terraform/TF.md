# Terraform

## terraform output

```
container_id = {
  "attach" = false
  "bridge" = ""
  "capabilities" = toset([])
  "cgroupns_mode" = tostring(null)
  "command" = tolist([])
  "container_logs" = tostring(null)
  "container_read_refresh_timeout_milliseconds" = 15000
  "cpu_set" = ""
  "cpu_shares" = 0
  "destroy_grace_seconds" = tonumber(null)
  "devices" = toset([])
  "dns" = toset(null) /* of string */
  "dns_opts" = toset(null) /* of string */
  "dns_search" = toset(null) /* of string */
  "domainname" = ""
  "entrypoint" = tolist([
    "sh",
    "-c",
    "python -m uvicorn app:app --host 0.0.0.0 --port 8080",
  ])
  "env" = toset([])
  "exit_code" = tonumber(null)
  "gpus" = tostring(null)
  "group_add" = toset(null) /* of string */
  "healthcheck" = tolist(null) /* of object */
  "host" = toset([])
  "hostname" = "b7a4f39a632b"
  "id" = "b7a4f39a632b2f5d665b22546a5c5a35b0a74f8ec130b909a9a8712978ed8f5a"
  "image" = "sha256:d60ad1041249e6d6132ee06c7007c71fc36fe6cbcbd6e1a2473c3005981ce2bf"
  "init" = false
  "ipc_mode" = "private"
  "labels" = toset([])
  "log_driver" = "json-fhttps://github.com/y4cer/S24-core-course-labs/pull/4ile"
  "log_opts" = tomap(null) /* of string */
  "logs" = false
  "max_retry_count" = 0
  "memory" = 0
  "memory_swap" = 0
  "mounts" = toset([])
  "must_run" = true
  "name" = "app_python"
  "network_data" = tolist([
    {
      "gateway" = "172.17.0.1"
      "global_ipv6_address" = ""
      "global_ipv6_prefix_length" = 0
      "ip_address" = "17https://github.com/y4cer/S24-core-course-labs/pull/42.17.0.2"
      "ip_prefix_length" = 16
      "ipv6_gateway" = ""
      "mac_address" = "02:42:ac:11:00:02"
      "network_name" = "bridge"
    },
  ])
  "network_mode" = "default"
  "networks_advanced" = toset([])
  "pid_mode" = ""
  "ports" = tolist([
    {
      "external" = 80
      "internal" = 8080
      "ip" = "0.0.0.0"
      "protocol" = "tcp"
    },
  ])
  "privileged" = false
  "publish_all_ports" = false
  "read_only" = false
  "remove_volumes" = true
  "restart" = "no"
  "rm" = false
  "runtime" = "runc"
  "security_opts" = toset([])
  "shm_size" = 64
  "start" = truehttps://github.com/y4cer/S24-core-course-labs/pull/4
  "stdin_open" = false
  "stop_signal" = ""
  "stop_timeout" = 0
  "storage_opts" = tomap(null) /* of string */
  "sysctls" = tomap(null) /* of string */
  "tmpfs" = tomap(null) /* of string */
  "tty" = false
  "ulimit" = toset([])
  "upload" = toset([])
  "user" = "user"https://github.com/y4cer/S24-core-course-labs/pull/4
  "userns_mode" = ""
  "volumes" = toset([])
  "wait" = false
  "wait_timeout" = 60
  "working_dir" = "/app_python"
}
image_id = {
  "build" = toset([])
  "force_remove" = tobool(null)
  "id" = "sha256:d60ad1041249e6d6132ee06c7007c71fc36fe6cbcbd6e1a2473c3005981ce2bfy4cerr/app_python"
  "image_id" = "sha256:d60ad1041249e6d6132ee06c7007c71fc36fe6cbcbd6e1a2473c3005981ce2bf"
  "keep_locally" = false
  "name" = "y4cerr/app_python"
  "platform" = tostring(null)
  "pull_triggers" = toset(null) /* of string */
  "repo_digest" = "y4cerr/app_python@sha256:ba5e02ff79d0de09be7ded975fdd62504d28b9190909cf8438d2fe09d46eb45f"
  "triggers" = tomap(null) /* of string */
}
```

## Best practices

I followed these best practices:

- Used git version control
- Split configuration into several files (`main.tf`, `variables.tf`,
  `terraform.tfvars`)
- Use variables and outputs
