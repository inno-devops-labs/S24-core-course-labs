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


resource "github_repository" "devops24" {
  name               = "devops24"
  description        = "my repo for devops course"
  visibility         = "public"
}



resource "github_branch_default" "main" {
  repository = github_repository.devops24.name
  branch     = "main"
}

resource "github_branch_protection" "default" {
  repository_id                   = github_repository.devops24.id
  pattern                         = github_branch_default.main.branch
  require_conversation_resolution = true
  enforce_admins                  = true

  required_pull_request_reviews {
    required_approving_review_count = 1
  }
}




