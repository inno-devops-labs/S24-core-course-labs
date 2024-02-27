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
}

resource "github_repository" "S24-core-course-labs" {
  name        = "S24-core-course-labs"
  description = "The awesome lab"
  visibility  = "public"
  has_issues  = true
  has_wiki    = true
  auto_init   = true
}

resource "github_branch_default" "main" {
  repository = github_repository.S24-core-course-labs.name
  branch     = "main"
}

resource "github_branch_protection" "default" {
  repository_id                   = github_repository.S24-core-course-labs.id
  pattern                         = github_branch_default.main.branch
  require_conversation_resolution = true
  enforce_admins                  = true

  required_pull_request_reviews {
    required_approving_review_count = 1
  }
}
