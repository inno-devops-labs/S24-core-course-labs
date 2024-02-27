terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 5.0"
    }
  }
}

provider "github" {
  token = var.token
  owner = var.organization
}

resource "github_team" "some_team" {
  name        = var.team_name_1
  description = var.team_description_1
  privacy     = "closed"
}

resource "github_team" "some_other_team" {
  name        = var.team_name_2
  description = var.team_description_2
  privacy     = "closed"
}

resource "github_team_repository" "team1_repo" {
  team_id    = github_team.some_team.id
  repository = var.github_repository
  permission = "push"
}

resource "github_team_repository" "team2_repo" {
  team_id    = github_team.some_other_team.id
  repository = var.github_repository
  permission = "pull"
}
