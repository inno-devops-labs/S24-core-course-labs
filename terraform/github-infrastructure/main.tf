terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 5.0"
    }
  }
}

resource "github_repository" "matskevich" {
  name        = "Matskevich"
  description = "Repository description with Terraform"
  visibility  = "public"
}

# Define branch protection rules for the default branch
resource "github_branch_protection" "main_branch_protection" {
  repository_id   = github_repository.matskevich.node_id
  pattern         = "main"
  enforce_admins  = true

  required_status_checks {
    strict   = true
    contexts = []
  }
}

output "repository_url" {
  value       = github_repository.matskevich.html_url
  description = "URL of the GitHub repository"
}