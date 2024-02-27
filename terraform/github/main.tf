# Source: https://dev.to/pwd9000/manage-and-maintain-github-with-terraform-2k86


terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 6.0"
    }
  }
}

variable "token" {
  description = "GitHub PAT"
  type        = string
  sensitive   = true
}


provider "github" {
  token = var.token
}


resource "github_repository" "repo" {
  name               = "DevOps-Lab04-TF"
  description        = "The repository for Terraform Lab04"
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

# Protect the main branch
resource "github_branch_protection" "default" {
  repository_id                   = github_repository.repo.id
  pattern                         = github_branch_default.main.branch
  require_conversation_resolution = true
  enforce_admins                  = true

  required_pull_request_reviews {
    required_approving_review_count = 1
  }
}
