terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 5.0"
    }
  }
}

provider "github" {
  token = var.github-token
}

resource "github_repository" "core-course-labs" {
  name        = "iu_devops"
  description = "Innopolis University — DevOps (Spring 2024)"
  visibility  = "public"
  has_issues  = false
  has_wiki    = false
  auto_init   = false
}

resource "github_branch_default" "core-course-labs" {
  repository = github_repository.core-course-labs.name
  branch     = "main"
}

resource "github_branch_protection" "core-course-labs_main" {
  repository_id                   = github_repository.core-course-labs.id
  pattern                         = "main"
  require_conversation_resolution = true
}
