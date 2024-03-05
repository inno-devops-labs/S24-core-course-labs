terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 5.17"
    }
  }
}

provider "github" {
}

resource "github_repository" "repo-devops-terraform" {
  name        = "devops-terraform"
  description = "smth"
  visibility  = "public"
  auto_init   = true
}

resource "github_branch" "master" {
  repository = github_repository.repo-devops-terraform.name
  branch     = "master"
  depends_on = [github_repository.repo-devops-terraform]
}

resource "github_branch_default" "master-default" {
  repository = github_repository.repo-devops-terraform.name
  branch     = github_branch.master.branch
  depends_on = [github_branch.master]
}

resource "github_branch_protection" "default" {
  repository_id                   = github_repository.repo-devops-terraform.id
  pattern                         = github_branch.master.branch
  require_conversation_resolution = true
  enforce_admins                  = true

  required_pull_request_reviews {
    required_approving_review_count = 1
  }
}

resource "github_repository" "S24-DevOps-course-labs" {
  name = "S24-DevOps-course-labs"
}
