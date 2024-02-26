output "python_container_id" {
  description = "Python container ID"
  value       = module.app_python.container_id
}

output "vm_external_ip" {
  value = module.yandex_cloud.external_ip
}

output "github_repo_name" {
  value = module.github.repo_name
}