terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 4.0"
    }
  }
}

provider "github" {
  token = var.token # or `GITHUB_TOKEN`
}

resource "github_repository" "core-course-labs" {
  name        = "S24-core-course-labs"
  description = "Devops labs"
  visibility  = "public"

  has_wiki      = true
  has_issues    = false
  has_downloads = true
  has_projects  = true
}
