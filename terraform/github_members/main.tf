terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 5.0.0"
    }
  }
}

provider "github" {
  token = var.token
  owner = var.organization
}

resource "github_team" "dev" {
  name        = "Dev"
  privacy     = "closed"
}

resource "github_team" "man" {
  name        = "Man"
  privacy     = "closed"
}

resource "github_team_membership" "membership_for_y0szx" {
  team_id  = github_team.dev.id
  username = "y0szx"
  role     = "member"
}

resource "github_team_membership" "membership_for_nikitagrigorenko" {
  team_id  = github_team.man.id
  username = "nikitagrigorenko"
  role     = "member"
}

resource "github_team_repository" "dev_bind" {
  team_id    = github_team.dev.id
  repository = var.repo
  permission = "maintain"
}

resource "github_team_repository" "man_bind" {
  team_id    = github_team.man.id
  repository = var.repo
  permission = "admin"
}