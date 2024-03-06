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
  owner = var.owner
}


resource "github_repository" "example_repo" {
  name               = "example-repo"
  description        = "An example repository managed by Terraform"
  visibility         = "public"
  has_issues         = true
  has_wiki           = true
  auto_init          = true
  license_template   = "mit"
  gitignore_template = "VisualStudio"
}

resource "github_team" "dev_team" {
  name        = "Dev Team"
  description = "Development team with write access to repositories"
  privacy     = "closed"
}

resource "github_team" "qa_team" {
  name        = "QA Team"
  description = "QA team with read access to repositories"
  privacy     = "closed"
}

resource "github_team" "ops_team" {
  name        = "Ops Team"
  description = "Operations team with admin access to repositories"
  privacy     = "closed"
}

resource "github_team_repository" "dev_team_repo" {
  team_id    = github_team.dev_team.id
  repository = github_repository.example_repo.name
  permission = "push" # Write access
}

resource "github_team_repository" "qa_team_repo" {
  team_id    = github_team.qa_team.id
  repository = github_repository.example_repo.name
  permission = "pull" # Read access
}

resource "github_team_repository" "ops_team_repo" {
  team_id    = github_team.ops_team.id
  repository = github_repository.example_repo.name
  permission = "admin" # Admin access
}
