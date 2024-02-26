terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 5.36.0"
    }
  }
}

provider "github" {
    token = var.token
}

resource "github_repository" "repo" {
  name               = "devops-repo"
  description        = "devops lab repo"
  visibility         = "public"
  has_issues         = true
  has_wiki           = true
  auto_init          = true
  allow_rebase_merge = false
  allow_squash_merge = false
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

resource "github_repository" "core" {
  description = "core repository"
  auto_init   = true
  name        = "devops-test"
  visibility  = "public"
}

resource "github_branch_default" "core_main" {
  repository = github_repository.core.name
  branch     = "main"
}