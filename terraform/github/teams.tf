resource "github_team" "developers" {
  name        = "developers"
  description = "dev team"
}

resource "github_team" "testers" {
  name        = "testers"
  description = "test team"
}

resource "github_team_repository" "developers_attach" {
  team_id    = github_team.developers.id
  repository = github_repository.demo.id
  permission = "maintain"
}

resource "github_team_repository" "testers_attach" {
  team_id    = github_team.testers.id
  repository = github_repository.demo.id
  permission = "triage"
}

