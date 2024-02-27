terraform {
  required_version = "~> 1.2"
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 4.0"
    }
  }
}

provider "github" {
  token = file("token") # or `GITHUB_TOKEN`
}

#Create and initialise a public GitHub Repository with MIT license and a Visual Studio .gitignore file (incl. issues and wiki)
resource "github_repository" "S24-DevOps" {
  name               = "S24-DevOps"
  description        = "My awesome codebase"
  visibility         = "public"
}

#Set default branch 'master'
resource "github_branch_default" "main" {
  repository = github_repository.S24-DevOps.name
  branch     = "main"
}

#Create branch protection rule to protect the default branch. (Use "github_branch_protection_v3" resource for Organisation rules)
resource "github_branch_protection" "default" {
  repository_id                   = github_repository.S24-DevOps.id
  pattern                         = github_branch_default.main.branch
  require_conversation_resolution = true
  enforce_admins                  = true

  required_pull_request_reviews {
    required_approving_review_count = 1
  }
}