terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 5.36.0"
    }
  }
}

provider "github" {
  owner = var.github_organization
  token = var.token
}

resource "github_team" "devs" {
  name        = "devs"
  privacy     = "closed"
}

resource "github_team" "devops" {
  name        = "devops"
  privacy     = "closed"
}

resource "github_team" "managers" {
  name        = "managers"
  privacy     = "closed"
}

resource "github_repository" "example_repo" {
  name        = var.repository
  description = "example"
  visibility  = "public"
}

resource "github_team_membership" "membership" {
  team_id  = github_team.devs.id
  username = "adarika"
  role     = "member"
}

resource "github_team_repository" "developers" {
  team_id    = github_team.devs.id
  repository = github_repository.example_repo.name
  permission = "maintain"
}