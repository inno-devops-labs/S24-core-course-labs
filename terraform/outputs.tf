output "python_container_id" {
  description = "Python container ID"
  value       = module.app_python.container_id
}

output "github_repo_name" {
  value = module.github.repo_name
}