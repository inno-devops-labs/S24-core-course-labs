output "repository_name" {
  value = github_repository.devops-test.name
}

output "repository_id" {
  value = github_repository.devops-test.id
}

output "default_branch" {
  value = github_branch_default.main.branch
}