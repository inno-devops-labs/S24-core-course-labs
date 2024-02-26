resource "github_repository" "devops-lab-4" {
  name             = "devops-lab-4"
  description      = "GitHub repository test"
  visibility       = "public"
  has_issues       = true
  has_wiki         = true
  auto_init        = true
  license_template = "mit"
}


resource "github_branch_default" "main" {
  repository = github_repository.devops-lab-4.name
  branch     = "main"
}

resource "github_branch_protection" "default" {
  repository_id                   = github_repository.devops-lab-4.id
  pattern                         = github_branch_default.main.branch
  require_conversation_resolution = true
  enforce_admins                  = true

  required_pull_request_reviews {
    required_approving_review_count = 1
  }
}

provider "github" {
  token = var.github_token
}

variable "github_token" {
  description = "GitHub token"
}