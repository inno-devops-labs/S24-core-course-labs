variable "token" {
  type        = string
  description = "Specifies the GitHub PAT token or `GITHUB_TOKEN`"
  sensitive   = true
}

terraform {
  required_version = ">= 0.13"
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 5.0"
    }
  }
}

provider "github" {
  token = var.token
}

resource "github_repository" "repo" {
  name             = "S24-core-course-labs"
  description      = "Code description"
  visibility       = "public"
  has_issues       = true
  has_wiki         = true
  auto_init        = true
  license_template = "mit"
}

resource "github_branch" "master" {
  repository    = github_repository.repo.name
  branch        = "master"
  source_branch = "main"
}

resource "github_branch_default" "master" {
  repository = github_repository.repo.name
  branch     = github_branch.master.branch
}

resource "github_branch_protection" "default" {
  repository_id                   = github_repository.repo.id
  pattern                         = github_branch_default.master.branch
  require_conversation_resolution = true
  enforce_admins                  = true

  required_pull_request_reviews {
    required_approving_review_count = 1
  }
}
