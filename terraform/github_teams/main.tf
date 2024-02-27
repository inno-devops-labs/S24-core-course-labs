terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 4.0"
    }
  }
}

provider "github" {
  token = var.token # or `GITHUB_TOKEN`
  owner = var.org
}

resource "github_team" "developers" {
  name    = "developers"
  privacy = "closed"
}

resource "github_team_membership" "mem_devs" {
  team_id  = github_team.developers.id
  username = "y0szx"
  role     = "member"
}

resource "github_team_repository" "bind_devs" {
  team_id    = github_team.developers.id
  repository = var.name
  permission = "maintain"
}
