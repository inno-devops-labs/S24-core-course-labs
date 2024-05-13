
### Main.tf ###

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
  owner = "roukaya-org"
}

#Create and initialise a public GitHub Repository with MIT license and a Visual Studio .gitignore file (incl. issues and wiki)
resource "github_repository" "repo" {
  name               = "test"
  description        = "Some desc for some test"
  visibility         = "public"
  has_issues         = true
  has_wiki           = true
  auto_init          = true
  license_template   = "mit"
  gitignore_template = "VisualStudio"
}

#Set default branch 'master'
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

resource "github_team" "my_team1" {
  name        = "my_team_1"
  description = "First team"
}

resource "github_team" "my_team2" {
  name        = "my_team_2"
  description = "Second team"
}

resource "github_team_repository" "my_team1_repo" {
  team_id    = github_team.my_team1.id
  repository = github_repository.repo.name
  permission = "push"
}

resource "github_team_repository" "my_team2_repo" {
  team_id    = github_team.my_team2.id
  repository = github_repository.repo.name
  permission = "admin"
}