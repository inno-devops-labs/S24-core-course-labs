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

resource "github_repository" "repo" {
  name        = "sample-repo"
  description = "Sample Lab4 DevOps"
  visibility  = "public"
  has_issues  = true
  has_wiki    = true
  auto_init   = true
  has_downloads = true
  has_projects  = true
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

resource "github_team_membership" "membership_for_dzendos" {
  team_id  = github_team.man.id
  username = "dzendos"
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