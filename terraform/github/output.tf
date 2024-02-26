output "repository_name" {
  value = github_repository.test-devops-terraform-repo.name
}

output "repository_id" {
  value = github_repository.test-devops-terraform-repo.id
}

output "default_branch" {
  value = github_branch_default.main.branch
}
