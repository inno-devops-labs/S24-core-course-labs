terraform {
  required_version = "~> 1.7.4"
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 4.0"
    }
  }
}

provider "github" {
  token = var.token
  owner = "s24-devops-organization"
}

# Create and initialise a public GitHub Repository with MIT license and a Visual Studio .gitignore file (incl. issues and wiki)
resource "github_repository" "repo" {
  name               = "Terraform-Devops-Repo"
  description        = "s24-devops-terraform-repo"
  visibility         = "public"
  has_issues         = true
  has_wiki           = true
  auto_init          = true
  license_template   = "mit"
  gitignore_template = "VisualStudio"
}

# Create a team for each row in the CSV file
resource "github_team" "all" {
  for_each = {
    for team in csvdecode(file("teams.csv")) : team.name => team
  }

  name                      = each.value.name
  description               = each.value.description
  privacy                   = each.value.privacy
  create_default_maintainer = true
}

# Add each team to the repository with the permissions specified in the CSV file
resource "github_team_repository" "all" {
  for_each = {
    for team in csvdecode(file("teams.csv")) : team.name => team
  }

  team_id    = github_team.all[each.key].id
  repository = github_repository.repo.name
  permission = each.value.permission
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
