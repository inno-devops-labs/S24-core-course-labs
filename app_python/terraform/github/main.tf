terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 6.0"
    }
  }
}

provider "github" {
  token = var.token
  owner = "RinRi-D"
}

resource "github_repository" "S24-core-course-labs" {
  name               = "S24-core-course-labs"
  description        = "core-course-labs"
  visibility         = "public"
  has_issues         = true
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
