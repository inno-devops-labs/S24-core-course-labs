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


resource "github_repository" "S24-core-course-labs" {
  name               = "S24-core-course-labs"
  description        = "my S24-core-course-labs repo"
  visibility         = "public"
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




