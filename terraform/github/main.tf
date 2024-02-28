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

# Create and initialise a public GitHub Repository with MIT license and a Visual Studio .gitignore file (incl. issues and wiki)
resource "github_repository" "repo" {
  name             = "devops-course-terraform-lab"
  description      = "Terraform lab for DevOps course"
  visibility       = "public"
  has_issues       = true
  auto_init        = true
  license_template = "mit"
}

resource "github_repository" "S24-core-course-labs" {
  name        = "S24-core-course-labs"
  description = "Repo for Innopolis University DevOps course S24"
}

# Set default branch 'master'
resource "github_branch_default" "main" {
  repository = github_repository.repo.name
  branch     = "main"
}

# Create branch protection rule to protect the default branch. (Use "github_branch_protection_v3" resource for Organisation rules)
resource "github_branch_protection" "default" {
  repository_id                   = github_repository.repo.id
  pattern                         = github_branch_default.main.branch
  require_conversation_resolution = true
  enforce_admins                  = true

  required_pull_request_reviews {
    required_approving_review_count = 1
  }
}
