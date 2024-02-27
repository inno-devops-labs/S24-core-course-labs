terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 4.0"
    }
  }
}

provider "github" {
  token = var.token
  organization = var.organization
}

resource "github_repository" "repo" {
  name               = var.name
  description        = var.description
  visibility         = "public"
  has_issues         = true
  has_wiki           = true
  auto_init          = true
  license_template   = "mit"
  gitignore_template = "VisualStudio"
}

resource "github_branch_default" "main" {
  repository = github_repository.repo.name
  branch     = "main"
}

resource "github_branch_protection" "default" {
  repository_id                   = github_repository.repo.id
  pattern                         = github_branch_default.main.branch
  require_conversation_resolution = true
  enforce_admins                  = true

  required_pull_request_reviews {
    required_approving_review_count = 1
  }
}

resource "github_team" "team1" {
  name = var.team1
}

resource "github_team" "team2" {
  name = var.team2
}

resource "github_team_repository" "team1_repo" {
  team_id    = github_team.team1.id
  repository = github_repository.repo.name
  permission = "pull"
}

resource "github_team_repository" "team2_repo" {
  team_id    = github_team.team2.id
  repository = github_repository.repo.name
  permission = "admin"
}