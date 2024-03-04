terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 5.0"
    }
  }
}

provider "github" {
  #owner = var.github_organization
}

resource "github_repository" "devops-terraform" {
  name               = "devops-terraform"
  description        = "some description"
  visibility         = "public"
  has_issues         = true
  has_wiki           = false
  auto_init          = true
  license_template   = "mit"
  gitignore_template = "Python"
}

resource "github_repository" "S24-core-course-labs" {
  name               = "S24-core-course-labs"
}

resource "github_branch_default" "master" {
  repository = github_repository.devops-terraform.name
  branch     = "master"
}

resource "github_branch_protection" "default" {
  repository_id                   = github_repository.devops-terraform.id
  pattern                         = github_branch_default.master.branch
  require_conversation_resolution = true
  enforce_admins                  = true

  required_pull_request_reviews {
    required_approving_review_count = 1
  }
}


