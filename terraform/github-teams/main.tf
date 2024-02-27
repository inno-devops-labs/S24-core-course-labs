terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 6.0.0"
    }
  }
}

provider "github" {
  token = var.token
  owner = var.organization
}

resource "github_team" "developers" {
  name        = "Developers"
  privacy     = "closed"
}

resource "github_team" "managers" {
  name        = "Managers"
  privacy     = "closed"
}

resource "github_team_membership" "membership_for_profectus" {
  team_id  = github_team.developers.id
  username = "profectus"
  role     = "member"
}

resource "github_team_repository" "developeres_bind" {
  team_id    = github_team.developers.id
  repository = var.repo
  permission = "maintain"
}

resource "github_team_repository" "managers_bind" {
  team_id    = github_team.managers.id
  repository = var.repo
  permission = "admin"
}