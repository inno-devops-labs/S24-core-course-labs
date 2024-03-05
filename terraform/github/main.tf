provider "github" {
   token = var.github_token
}


terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 4.0"
    }
  }
}


resource "github_repository" "S24-DevOps-labs" {
  name               = "TerraformCheck"
  description        = "Repository for DevOps lab grading"
  visibility         = "public"
  has_issues         = true
  has_wiki           = true
  auto_init          = true
  license_template   = "mit"
  gitignore_template = "Python"
}


resource "github_branch_default" "main" {
  repository = github_repository.S24-DevOps-labs.name
  branch     = "main"
}

resource "github_branch_protection" "default" {
  repository_id                   = github_repository.S24-DevOps-labs.id
  pattern                         = github_branch_default.main.branch
  require_conversation_resolution = true
  enforce_admins                  = true

  required_pull_request_reviews {
    required_approving_review_count = 1
  }
}