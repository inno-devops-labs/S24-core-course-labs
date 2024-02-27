// New Repository
terraform {
  required_providers {
    github = {
      source  = "intergrations/github"
      version = "~> 5.0"
    }
  }
}

resource "github_repository" "iac_lab" {
  name             = "iac_lab"
  description      = "Test github repository"
  auto_init        = true
  visibility       = "public"
  has_issues       = true
  has_wiki         = true
  license_template = "mit"
}


resource "github_branch_default" "main" {
  repository = github_repository.iac_lab.name
  branch     = "main"
}

resource "github_branch_protection" "default" {
  repository_id                   = github_repository.iac_lab.id
  pattern                         = github_branch_default.main.branch
  require_conversation_resolution = true
  enforce_admins                  = true

  required_pull_request_reviews {
    required_approving_review_count = 1
  }
}

// Imported Repository
resource "github_repository" "S24-core-course-labs" {
  name = "S24-core-course-labs"
  lifecycle {
    prevent_destroy = true
  }
}

# Branch protection
resource "github_branch_protection" "devops" {
  repository_id                   = github_repository.S24-core-course-labs.id
  pattern                         = "main"
  require_conversation_resolution = true
  enforce_admins                  = true

  required_pull_request_reviews {
    required_approving_review_count = 1
  }

  lifecycle {
    prevent_destroy = true
  }
}


provider "github" {
}

