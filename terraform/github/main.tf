terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 5.3"
    }
  }
}

provider "github" {
  owner = var.github_organization
  token = var.token
}

resource "github_repository" "core-course-labs" {
  name          = "core-course-labs"
  description   = ""
  visibility    = "public"
  has_issues    = false
  has_wiki      = true
  auto_init     = false
  has_downloads = true
  has_projects  = true
}

resource "github_branch_default" "main" {
  repository = github_repository.core-course-labs.name
  branch     = "main"
}

resource "github_branch_protection" "default" {
  repository_id                   = github_repository.core-course-labs.id
  pattern                         = github_branch_default.main.branch
  require_conversation_resolution = true
  enforce_admins                  = true

  required_pull_request_reviews {
    required_approving_review_count = 1
  }
}