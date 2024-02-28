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
  owner = var.organization
}

resource "github_team" "dev" {
  name = "Best Developers ever"
  privacy = "closed"
}

resource "github_team" "managers" {
  name = "Best Managers ever"
  privacy = "closed"
}

resource "github_team_membership" "member_for_developers" {
  team_id  = github_team.dev.id
  username = "timur-harin"
  role     = "member"
}


resource "github_team_membership" "member_for_manager" {
  team_id  = github_team.managers.id
  username = "timur-harin"
  role     = "member"
}


resource "github_team_repository" "develop_permission" {
  team_id    = github_team.dev.id
  repository = var.repository
  permission = "admin"
}


resource "github_team_repository" "manager_permission" {
  team_id    = github_team.managers.id
  repository = var.repository
  permission = "maintain"
}
