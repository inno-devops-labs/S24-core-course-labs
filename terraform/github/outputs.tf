output "id" {
  value = github_repository.iac_lab.id
}

output "name" {
  value = github_repository.iac_lab.name
}

output "branch" {
  value = github_branch_default.main.branch
}
