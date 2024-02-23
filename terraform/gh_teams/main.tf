terraform {
  required_version = "~> 1.7.3"
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 4.0"
    }
  }
}

provider "github" {
  token = var.token # or `GITHUB_TOKEN`
  owner = "S24-demo-org"
}

resource "github_repository" "devops_s23_demo" {
  name               = "Demo-DevOps-S23-repo"
  description        = "Demo repo for the course"
  visibility         = "public"
  has_issues         = true
  has_wiki           = false
  auto_init          = true
  license_template   = "mit"
  gitignore_template = "VisualStudio"
}

resource "github_team" "developers" {
  name        = "Developers"
  description = "Developers of the project"
  privacy     = "closed"
}

resource "github_team" "admins" {
  name        = "Admins"
  description = "Admins of the project"
  privacy     = "closed"
}

resource "github_team_membership" "devs_membership" {
  team_id  = github_team.developers.id
  username = "WinnerJust"
  role     = "member"
}

resource "github_team_membership" "admins_membership" {
  team_id  = github_team.admins.id
  username = "FK12344321"
  role     = "member"
}

resource "github_team_repository" "devs_bind" {
  team_id    = github_team.developers.id
  repository = "Demo-DevOps-S23-repo"
  permission = "maintain"
}

resource "github_team_repository" "admins_bind" {
  team_id    = github_team.developers.id
  repository = "Demo-DevOps-S23-repo"
  permission = "admin"
}