resource "github_team" "developers" {
  name        = "developers"
  description = "Developers team"
}

resource "github_team" "contributors" {
  name        = "contributors"
  description = "Contributors team"
}

# Define team permissions on repositories within the organization
resource "github_team_repository" "developers_access" {
  team_id    = github_team.developers.id
  repository = "devops-terraform-example" # Replace with the repository name
  permission = "push"                     # Developers team has push access
}

resource "github_team_repository" "contributors_access" {
  team_id    = github_team.contributors.id
  repository = "devops-terraform-example" # Replace with the repository name
  permission = "pull"                     # Contributors team has pull access
}