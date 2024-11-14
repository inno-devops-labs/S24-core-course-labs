terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 5.0"
    }
  }
}

resource "github_repository" "example_repo" {
  name        = "labs-aksinya"
  description = "Terraform-managed repository"
  visibility  = "public"
}

resource "github_branch_protection" "main_branch_protection" {
  repository_id   = github_repository.example_repo.node_id  # Update here
  pattern         = "main"
  enforce_admins  = true

  required_status_checks {
    strict   = true
    contexts = []
  }
}
