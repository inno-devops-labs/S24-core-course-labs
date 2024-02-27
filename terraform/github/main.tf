terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 4.0"
    }
  }

}

provider "github" {
  token        = var.GITHUB_TOKEN
  owner = var.organization_name
}

#Create and initialise a public GitHub Repository with MIT license and a Visual Studio .gitignore file (incl. issues and wiki)
resource "github_repository" "repo" {

  name               = var.repository_name
  description        = var.repository_description
  visibility         = "public"
  has_issues         = true
  has_projects       = true
  has_wiki           = true
  auto_init          = true
  license_template   = "mit"
  gitignore_template = "VisualStudio"
}

#Set default branch 'main'
resource "github_branch_default" "main" {
  repository = github_repository.repo.name
  branch     = "main"
}

#Create branch protection rule to protect the default branch. (Use "github_branch_protection_v3" resource for Organisation rules)
resource "github_branch_protection" "default" {
  repository_id                   = github_repository.repo.id
  pattern                         = github_branch_default.main.branch
  require_conversation_resolution = true
  enforce_admins                  = true

  required_pull_request_reviews {
    required_approving_review_count = 1
  }
}

resource "github_team" "team1" {
  name        = "Team 1"
  description = "My new team 1 for use with Terraform"
  privacy     = "closed"
}

resource "github_team_repository" "team-repo1" {
  team_id    = github_team.team1.id
  repository = github_repository.repo.name
  permission = "pull"
}

resource "github_team" "team2" {
  name        = "Team 2"
  description = "My new team 2 for use with Terraform"
  privacy     = "closed"
}

resource "github_team_repository" "team-repo2" {
  team_id    = github_team.team2.id
  repository = github_repository.repo.name
  permission = "push"
}

resource "github_team" "team3" {
  name        = "Team 3"
  description = "My new team 3 for use with Terraform"
  privacy     = "closed"
}

resource "github_team_repository" "team-repo3" {
  team_id    = github_team.team3.id
  repository = github_repository.repo.name
  permission = "admin"
}
