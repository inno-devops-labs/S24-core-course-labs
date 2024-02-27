terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 6.0"
    }
  }
}

provider "github" {
  token = var.token
  owner = "devops-lab4-snejugal"
}

resource "github_organization_settings" "org" {
  name = "devops-lab4-snejugal"
  company = "devops-lab4-snejugal"
  billing_email = "contact@snejugal.ru"
}

resource "github_repository" "repo" {
  name        = "nice-repo"
  description = "The awesome bonus task"
  visibility  = "public"
  has_issues  = true
  has_wiki    = true
}

resource "github_team" "team_1" {
  name        = "team 1"
}

resource "github_team" "team_2" {
  name        = "team 2"
}

resource "github_team_repository" "team_1" {
  team_id    = github_team.team_1.id
  repository = github_repository.repo.id
  permission = "pull"
}

resource "github_team_repository" "team_2" {
  team_id    = github_team.team_2.id
  repository = github_repository.repo.id
  permission = "maintain"
}
