### Main.tf ###

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
  token = file("C:/DevOps/gh_token.txt")
}

resource "github_repository" "repo" {
  name               = "DevOps-S24-core-course-labs-terraformed"
  description        = "Repository updated using terraform"
  visibility         = "public"
}

#Set default branch 'main'
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
    required_approving_review_count = 0
  }
}