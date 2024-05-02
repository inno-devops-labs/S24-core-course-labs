terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 6.0"
    }
  }
}

provider "github" {
  owner = "kolayne-IU-assignments"
}

resource "github_team" "team1" {
  name        = "Team1"
  description = "First team"
  privacy     = "closed"
}

resource "github_team" "team2" {
  name        = "Team2"
  description = "Second team"
  privacy     = "closed"
}

resource "github_team_members" "team1_members" {
  team_id = github_team.team1.id

  members {
    username = "kolayne"
    role     = "maintainer"
  }
}

resource "github_team_repository" "team1_repo" {
  team_id = github_team.team1.id
  repository = "S24-core-course-labs"
  permission = "triage"
}

resource "github_team_members" "team2_members" {
  team_id = github_team.team2.id
  members {
    username = "kolayne"
    role     = "maintainer"
  }
}

resource "github_team_repository" "team2_repo" {
  team_id = github_team.team2.id
  repository = "S24-core-course-labs"
  permission = "pull"
}
