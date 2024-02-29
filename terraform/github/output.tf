output "repo_id" {
  value = github_repository.devops-lab-repo.id
}

output "repo_name" {
  value = github_repository.devops-lab-repo.name
}

output "repo_branch" {
  value = github_branch_default.main.branch
}