terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 5.0"
    }
  }
}

# Configure the GitHub Provider
provider "github" {
  token = var.token
}

resource "github_repository" "example_repo" {
  name               = "example-repo"
  description        = "This is an example repository"
  visibility         = "public"
  has_issues         = true
  has_wiki           = true
  auto_init          = true
  license_template   = "mit"
  gitignore_template = "VisualStudio"
}

resource "github_repository" "S24-DevOps-Labs" {
  name        = "S24-DevOps-Labs"
  description = ""
  visibility  = "public"
}

resource "github_branch_default" "main" {
  repository = github_repository.example_repo.name
  branch     = "main"
}

resource "github_branch_protection" "example_branch_protection" {
  repository_id                   = github_repository.example_repo.id
  pattern                         = github_branch_default.main.branch
  require_conversation_resolution = true
  enforce_admins                  = true
  required_pull_request_reviews {
    required_approving_review_count = 1
  }
}