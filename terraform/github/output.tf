output "repository_name" {
  value = github_repository.test-terraform.name
}

output "repository_id" {
  value = github_repository.test-terraform.id
}

output "default_branch" {
  value = github_branch_default.main.branch
}