terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 5.0.0"
    }
  }
}

resource "github_team" "developer" {
  name        = "Developer"
  privacy     = "closed"
}


resource "github_team_membership" "membership" {
  team_id  = github_team.developer.id
  username = "LaithAlebrahim"
  role     = "member"
}


resource "github_team_repository" "add_developer" {
  team_id    = github_team.developer.id
  repository = var.repo
  permission = "admin"
}
