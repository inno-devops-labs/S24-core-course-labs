terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 5.0"
    }
  }
}

provider "github" {
  owner = var.org
}

resource "github_repository" "repo" {
  name             = "DevOps-Lab04-repo"
  description      = "Using terraform with Github providers including teams"
  visibility       = "public"
  has_issues       = true
  has_wiki         = false
  auto_init        = true
  license_template = "mit"
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

resource "github_team" "managers" {
  name        = "managers"
  description = "The management team"
}

resource "github_team" "developers" {
  name        = "developers"
  description = "The development team"
}

resource "github_team_repository" "managers_attach" {
  team_id    = github_team.managers.id
  repository = github_repository.repo.id
  permission = "maintain"
}

resource "github_team_repository" "developers_attach" {
  team_id    = github_team.developers.id
  repository = github_repository.repo.id
  permission = "triage"
}
