provider "github" {
  token = file("C:/DevOps/gh_token.txt")
  owner = "DevOpsCourse-S24-Terraform"
}
# Organization url: https://github.com/DevOpsCourse-S24-Terraform

resource "github_repository" "example-repo" {
  name        = "example-repo"
  description = "My new repository for use with Terraform"
}
# example-repo: https://github.com/DevOpsCourse-S24-Terraform/example-repo

resource "github_team" "example-team" {
  name        = "example-team"
  description = "My new team for use with Terraform"
  privacy     = "closed"
}
# example-team: https://github.com/orgs/DevOpsCourse-S24-Terraform/teams/example-team

resource "github_team" "admin-team" {
  name        = "admin-team"
  description = "My new team for use with Terraform"
  privacy     = "closed"
}
# Admin team: https://github.com/orgs/DevOpsCourse-S24-Terraform/teams/admin-team

resource "github_team_repository" "example-team-repo" {
  team_id    = github_team.example-team.id
  repository = github_repository.example-repo.name
  permission = "push"
}
# Example team repositories: https://github.com/orgs/DevOpsCourse-S24-Terraform/teams/example-team/repositories

resource "github_team_repository" "example-admin-team-repo" {
  team_id    = github_team.admin-team.id
  repository = github_repository.example-repo.name
  permission = "admin"
}
# Admin team repositories: https://github.com/orgs/DevOpsCourse-S24-Terraform/teams/admin-team/repositories

# Tutorial: https://www.hashicorp.com/blog/managing-github-with-terraform
# Since I this repository not in organization, I didn't extend terraform_github.
# I wrote a new one for organization